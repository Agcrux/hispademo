"""Build the web photo set from the event photos in photos/.

TO ADD PHOTOS: drop the image files straight into photos/ and run this script.
Any name works - camera names, "unnamed (1).jpg", whatever. Anything not already
numbered is adopted and renamed to the next free number, because that number is
what ties an original to its web copies. To remove a photo, delete it from
photos/ and re-run; its copies are pruned.

The originals sit alone in photos/. Each {n}.jpg produces two web copies, kept in
their own folders so originals are never mixed in with generated files:

  photos/web/p{n}.jpg      720w  - film-strip frames. The largest strip cell is
                                   214px in a 1672px stage, so it renders ~330 CSS
                                   px on a 2560px display -> ~660 device px at 2x.
  photos/web-lg/p{n}.jpg  1800w  - lightbox only, fetched on click. The lightbox
                                   caps at min(86vw, 940px), ~1880 device px at 2x.

Slot p{n} is always source {n}, so photos/web/p12.jpg is your 12.jpg.

Images are only ever downscaled, never enlarged: sources already smaller than a
tier's target are re-encoded at their native size instead of being upscaled.

The library size is not fixed anywhere. This writes photos/manifest.json listing
exactly the slots that exist, and the pages size themselves from it, so the photo
count follows the folder with no code change.

Beyond the one-time rename of newly-added files, originals are never modified.
"""
import glob, json, os, re
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "photos")
OUT_WEB = os.path.join(SRC, "web")
OUT_WEB_LG = os.path.join(SRC, "web-lg")
MANIFEST = os.path.join(SRC, "manifest.json")

TIERS = [(OUT_WEB, 720, 82), (OUT_WEB_LG, 1800, 86)]
EXTS = (".jpg", ".jpeg", ".png", ".webp")


def source_images():
    """Every image sitting directly in photos/ (never the generated subfolders)."""
    out = []
    for name in os.listdir(SRC):
        path = os.path.join(SRC, name)
        if os.path.isfile(path) and os.path.splitext(name)[1].lower() in EXTS:
            out.append(path)
    return out


def photo_number(path):
    """The {n} of a photos/{n}.jpg original, or None if it is not numbered yet."""
    stem = os.path.splitext(os.path.basename(path))[0]
    return int(stem) if re.fullmatch(r"\d+", stem) else None


images = source_images()
if not images:
    raise SystemExit(f"no images found in {SRC}")

numbered = {photo_number(f): f for f in images if photo_number(f) is not None}
unnumbered = [f for f in images if photo_number(f) is None]

# Adopt anything freshly dropped in, oldest first so it lands in the order it
# arrived. Existing numbers are never reused or reshuffled, so photos already on
# the site keep their slot.
adopted = []
next_free = 1
for path in sorted(unnumbered, key=lambda f: (os.path.getmtime(f), f.lower())):
    while next_free in numbered:
        next_free += 1
    ext = os.path.splitext(path)[1].lower()
    dest = os.path.join(SRC, f"{next_free}{ext}")
    os.rename(path, dest)
    numbered[next_free] = dest
    adopted.append((os.path.basename(path), os.path.basename(dest)))

for out_dir, _, _ in TIERS:
    os.makedirs(out_dir, exist_ok=True)

ids = sorted(numbered)
totals = {out_dir: 0 for out_dir, _, _ in TIERS}
for n in ids:
    base = ImageOps.exif_transpose(Image.open(numbered[n])).convert("RGB")
    for out_dir, target_w, q in TIERS:
        im = base
        w, h = im.size
        if w > target_w:
            im = im.resize((target_w, round(h * target_w / w)), Image.LANCZOS)
        out = os.path.join(out_dir, f"p{n}.jpg")
        im.save(out, "JPEG", quality=q, optimize=True, progressive=True)
        totals[out_dir] += os.path.getsize(out)

# Drop copies whose original is gone, so the site never serves stale slots.
keep = {f"p{n}.jpg" for n in ids}
pruned = 0
for out_dir, _, _ in TIERS:
    for f in glob.glob(os.path.join(out_dir, "p*.jpg")):
        if os.path.basename(f) not in keep:
            os.remove(f)
            pruned += 1

with open(MANIFEST, "w", encoding="utf-8") as fh:
    json.dump({"photos": ids}, fh, separators=(",", ":"))

for old, new in adopted:
    print(f"adopted    {old}  ->  {new}")
for out_dir, target_w, q in TIERS:
    mb = totals[out_dir] / 1024 / 1024
    rel = os.path.relpath(out_dir, ROOT).replace("\\", "/")
    print(f"{rel:<14} {target_w:>5}w q{q}  {len(ids)} photos  "
          f"{mb:6.1f} MB  (avg {totals[out_dir]/len(ids)/1024:5.0f} KB)")
if pruned:
    print(f"pruned {pruned} stale cop{'y' if pruned == 1 else 'ies'}")
print(f"manifest       photos/manifest.json -> {len(ids)} slots")
