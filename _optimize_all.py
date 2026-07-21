"""Build the web photo set from the event photos in photos/ (1.jpg, 2.jpg, ...).

Each source {n}.jpg produces two web copies, so slot p{n} is always source {n}:

  photos/p{n}.jpg      720w  - film-strip frames. The largest strip cell is 214px
                               in a 1672px stage, so it renders ~330 CSS px on a
                               2560px display -> ~660 device px at 2x DPR.
  photos/lg/p{n}.jpg  1800w  - lightbox only, fetched on click. The lightbox caps
                               at min(86vw, 940px), i.e. ~1880 device px at 2x.

Images are only ever downscaled, never enlarged: sources already smaller than a
tier's target are re-encoded at their native size instead of being upscaled.

The library size is not fixed anywhere. This writes photos/manifest.json listing
exactly the slots that exist, and the pages size themselves from it, so adding or
removing an original is just: drop the file in (or delete it), re-run this script.
Copies whose original is gone are pruned so nothing stale survives.

The originals themselves are never modified.
"""
import glob, json, os, re
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "photos")
OUT_LG = os.path.join(SRC, "lg")
MANIFEST = os.path.join(SRC, "manifest.json")

TIERS = [(SRC, 720, 82), (OUT_LG, 1800, 86)]


def photo_number(path):
    """The {n} of a photos/{n}.jpg original, or None if not a numbered original."""
    stem = os.path.splitext(os.path.basename(path))[0]
    return int(stem) if re.fullmatch(r"\d+", stem) else None


originals = sorted(
    ((photo_number(f), f) for f in glob.glob(os.path.join(SRC, "*.jpg"))
     if photo_number(f) is not None),
)
if not originals:
    raise SystemExit(f"no numbered originals found in {SRC}")

os.makedirs(OUT_LG, exist_ok=True)

totals = {out_dir: 0 for out_dir, _, _ in TIERS}
for n, path in originals:
    base = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    for out_dir, target_w, q in TIERS:
        im = base
        w, h = im.size
        if w > target_w:
            im = im.resize((target_w, round(h * target_w / w)), Image.LANCZOS)
        out = os.path.join(out_dir, f"p{n}.jpg")
        im.save(out, "JPEG", quality=q, optimize=True, progressive=True)
        totals[out_dir] += os.path.getsize(out)

ids = [n for n, _ in originals]

# Drop copies whose original no longer exists, so the folder never serves stale slots.
keep = {f"p{n}.jpg" for n in ids}
pruned = 0
for out_dir, _, _ in TIERS:
    for f in glob.glob(os.path.join(out_dir, "p*.jpg")):
        if os.path.basename(f) not in keep:
            os.remove(f)
            pruned += 1

with open(MANIFEST, "w", encoding="utf-8") as fh:
    json.dump({"photos": ids}, fh, separators=(",", ":"))

for out_dir, target_w, q in TIERS:
    mb = totals[out_dir] / 1024 / 1024
    rel = os.path.relpath(out_dir, ROOT).replace("\\", "/")
    print(f"{rel:<10} {target_w:>5}w q{q}  {len(ids)} photos  "
          f"{mb:6.1f} MB  (avg {totals[out_dir]/len(ids)/1024:5.0f} KB)")
if pruned:
    print(f"pruned {pruned} stale cop{'y' if pruned == 1 else 'ies'}")
print(f"manifest   photos/manifest.json -> {len(ids)} slots")
