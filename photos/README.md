# photos/

Your originals sit here on their own. Everything generated lives in its own
subfolder, built by `_optimize_all.py` in the project root.

| What | Example | Size | Purpose |
|---|---|---|---|
| **Your originals** | `1.jpg` … `47.jpg` | ~122 MB | The masters, straight from the camera. Edit/add/delete these. Never served to the site. |
| **`web/`** | `web/p1.jpg` … | ~3 MB | 720px wide. What the film-strip frames load. `p{n}` always comes from `{n}.jpg`. |
| **`web-lg/`** | `web-lg/p1.jpg` … | ~16 MB | 1800px wide. Loaded **only** when someone clicks a frame to open the lightbox, which displays up to 940px and would look soft off the 720px copy. |
| **`manifest.json`** | — | tiny | The list of slots that exist. The pages read it to size themselves, so the photo count is never hardcoded. |

## Adding or removing a photo

1. Drop the image files straight into `photos/` (this folder — **not** `web/` or
   `web-lg/`). Any filename works: `DSC_0148.jpg`, `unnamed (2).jpg`, whatever.
   To remove one, just delete it.
2. Run `python _optimize_all.py` from the project root.
3. Commit and push — the new files under `photos/web/` and `photos/web-lg/` have
   to be pushed too, or the deployed site won't have them.

The script gives each newly-added file the next free number (that number is what
ties an original to its copies), rebuilds both copy sets, rewrites `manifest.json`,
and deletes copies whose original is gone. Photos already on the site keep their
existing numbers, so nothing gets reshuffled. The strips and the lightbox pick up
the new count on next load — no code change needed.

Accepted inputs: `.jpg`, `.jpeg`, `.png`, `.webp`. The generated copies are always
JPEG regardless.

## Why two generated sizes

Serving the originals directly would mean multi-megabyte downloads per frame; serving
only the small copy would make the lightbox blurry. The frames get the light file, and
only the clicked photo pays for the large one.

## Don't move `web/` or `web-lg/` into Git LFS

Vercel deploys without running `git lfs pull`, so anything LFS-tracked arrives as a
130-byte pointer stub and renders as a broken image. Both folders are deliberately
excluded from LFS in `.gitattributes`. The originals stay in LFS only because the
site never requests them.
