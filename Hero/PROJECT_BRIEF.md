# HISPA 20th Anniversary — Animated Website Hero Banner
### Project Brief & Vision (source of truth — read this first)

---

## 1. One-line summary
An animated, infinitely-looping, **full-bleed website hero banner** promoting **HISPA's 2026 Kick-Off & Recruiting Events**, built around a flowing **sinusoidal "wave"** of real HISPA event photography — the literal visual of the tagline *"cultivating the next wave of leaders."*

---

## 2. Purpose, format & behavior
- **Deliverable:** a website **hero banner** (top-of-page section), authored as a single streaming Design Component (`.dc.html`).
- **Campaign:** *strictly* promoting HISPA's **2026 Kick-Off & Recruiting Events** (a drive to recruit professional Role Models). Not a general homepage.
- **Occasion:** HISPA's **20th anniversary**.
- **Motion:** **loops forever** as a live web animation — NOT a video export.
- **Placement / height:** a **shorter banner strip** at the top of the page (NOT full-viewport), so the event details below the fold are immediately visible.
- **Responsive:** **mobile is a hard priority** — the wave and all text must scale cleanly on small screens; CTA stays tappable (≥44px).

---

## 3. About HISPA (context; from the provided invitation PDF)
- Nonprofit that inspires students to discover their potential, embrace education, and achieve success — via professional **Role Models**.
- Founded in **New Jersey, 2007**; expanded to San Antonio TX (2011), NY (2013), FL (2015), Norristown PA (2019).
- Has mobilized **3,500 professionals** as Role Models.
- **4,000+ school visits**; **33,000+ students reached** across NJ, NY, PA, TX, FL.
- **2020 Presidential Award for Excellence in Science, Mathematics and Engineering Mentoring** (highest national STEM mentoring award, White House).
- Programs: HISPA Role Model Program, HISPA Imagine Day, HISPA Youth Conference.
- 2026 Kick-Off tour cities: **Miami, Palm Beach, New Jersey, New York, Pennsylvania**.
- These proof points are held **in reserve** — not all appear in the hero.

---

## 4. Core concept — "The Wave"
- A central **braided ribbon band** shaped as a horizontal **sinusoidal wave** spanning the banner width.
- The band's interior is **filled with a collage of HISPA's real event photos**, following the wave's contour.
- **Full-bleed:** the wave fills the hero; logo, headline, locations, and CTA sit **on top** with legibility protection (scrim/contrast).
- Thematic anchor: the wave *is* "the next wave of leaders."

---

## 5. Visual system

**Brand colors (exact, from the HISPA logo `.fig`):**
| Role | Hex |
|---|---|
| HISPA Blue | `#298CB5` |
| HISPA Green | `#71BD30` (variants `#6EBC35`, `#74D42A`) |
| HISPA Orange | `#E67610` |
| 20th anniversary blue ("th") | `#388DCA` |

**Wave color flow — CHOSEN: Option A, HISPA-brand spectrum.**
Warm → cool, left → right: **orange → gold → green → teal → blue**. **No reds, no purples.**

**Background:** dark, sophisticated — charcoal / deep-navy gradient so the wave pops.

**Typography (LOCKED):**
- **Headline / display:** **Figtree** (warm geometric sans), weights ~600–800.
- **Body / labels / small text:** **Hanken Grotesk** (clean neutral sans), weights ~400–600.
- Both via Google Fonts.

**Logo assets (from `HISPA.fig`, mounted):**
- **Primary HISPA mark:** outstretched-arms figure(s) + "HISPA" wordmark. Component frames: `BlueMan` (`#298CB5`), `GreenMan` (`#71BD30`), `STAR` (orange `#E67610`), `HISPA_Text` wordmark (orange `#E67610`). Node group at `/HISPA`.
- **20th-anniversary lockup:** the **official colored mark supplied by the user** (`brand/anniversary-20th.png`, transparent PNG, 1454×1082) — segmented "20" flowing green / red / gold / cyan / navy with white keylines, a blue "th", and orange "ANNIVERSARY". Used **verbatim** as the focal graphic. *(The earlier flat-green SVG reconstruction from the `.fig` is superseded.)* Note: this anniversary mark uses the fuller brand rainbow; the **wave** stays the restrained warm→cool orange→blue.

---

## 6. Hero composition / layout
- **HISPA logo** — top-left.
- **20th-anniversary lockup** — featured as a focal point.
- **Headline** — *"With our voices, cultivating the next wave of leaders."*
- **Tour locations** — subtle single row beneath the headline: **Miami · Palm Beach · New Jersey · New York · Pennsylvania** (cities only, **no dates**).
- **Primary CTA button** — **"Become a Role Model"** → links to **https://hispakickoff.org**.
- Full-bleed wave background; foreground text sits on a **frosted-glass (glassmorphism) panel** — a subtle `backdrop-filter` blur that softens the busy photographic wave just enough for the text to pop, while the warm→cool colors still bleed through dynamically. (Preferred over a flat scrim.)
- Banner-strip height; below-the-fold content stays visible.
- Mobile: wave + text reflow/scale cleanly.

---

## 7. Motion & animation
- **Overall feel:** **subtle, slow, elegant, premium** — draws the eye without distracting from the photos or the CTA.
- **Wave:** slow, continuous **fluid ripple** across the band (color bands + embedded photos).
- **Photos:** gentle **phase-shift** with **staggered timing** — individual photos surface / fade / drift on slight offset delays from one another (never synchronized), producing a polished, complex, structural, genuinely-flowing feel rather than a uniform pulse.
- **Color:** subtle **pulse** along the bands.
- **Ambient layer — CHOSEN: "Both, dialed down".** Primarily **warm & celebratory** (soft floating light motes, gentle sparkle) with a **faint whisper of a structured grid** for a clean, modern feel. The original brief's binary-code / data-stream elements are **dropped** in favor of human warmth.
- **Accessibility:** **respect `prefers-reduced-motion`** — ease to a near-still, gently-breathing (or fully static) state. Non-negotiable.
- **Loop:** seamless, infinite, stateless (nothing persisted).

---

## 8. Assets inventory
**Event photos** (`uploads/`) — 8 real HISPA photos:
- `54041867626_ce6a8d5006_h.jpg`, `54042319275_c3d6beffd8_h.jpg` — formal group portraits w/ gold **"5000"** balloons + "Pioneers of Change" slide
- `54042317300_fb61c650e6_z.jpg` — large celebratory crowd w/ gold **"1000"** balloons
- `54042319400_80511499b0_h.jpg` — two leaders beside a partner (Merrill/Bank of America) banner
- `54139388866_dd77d92dc5_h.jpg` — youth holding "amazon" bags at a facility tour
- `55172036119_0a140f7f57_c.jpg` — three attendees, "Exploration Day" selfie
- `55170889072_01093c6627_z.jpg` — two attendees, "Exploration Day" arena
- `55295439283_11760d5cbc_z.jpg` — three attendees, networking reception
- (Exact file↔placement mapping finalized at build time by viewing each.)

**Brand:** `HISPA.fig` (mounted) — figure / wordmark / star reconstructed to `brand/logo-*.svg`. **20th mark:** `brand/anniversary-20th.png` (user-supplied official colored lockup, transparent).
**Source context:** `uploads/Copy of NY- HISPA Kick-off 2026 - Invitation .pdf`.

**Note:** some photos contain partner brand marks (Bank of America/Merrill, Amazon, NJIT). Acceptable — these are real partner-event photos, and HISPA celebrates its corporate partners. Crops can de-emphasize third-party logos if desired.

---

## 9. Constraints & non-goals
- **No backend, database, auth, or hosting** — this is a self-contained front-end animation only.
- **No invented or illustrated people** — real HISPA photography only.
- **Stay on-brand:** HISPA blue/green/orange; **no reds or purples** in the wave.
- **Not** a full-viewport hero — a banner strip.
- Delivery format (embed snippet vs standalone file vs handoff) decided in the technical-decisions step.

---

## 10. Open items (build-time details only)
- Photo crop treatment regarding partner logos (Bank of America/Merrill, Amazon, NJIT) — can de-emphasize via cropping if desired.
- Final file↔placement mapping of the 8 photos across the wave.
- (Tour locations = cities only, no dates — decided.)

---

## 11. Technical decisions (agreed, logged as we go)
- **#1 — Rendering:** **Canvas 2D** paints the animated wave (photos, ripple, color pulse, staggered photo drift); the **logo, headline, city row, CTA button, and frosted-glass panel are DOM/CSS layered on top** (fully editable + accessible). *Consequence:* the wave is a single "picture" to the visual editor — **photo swaps happen in code**, not by clicking inside the wave.
- **#2 — Dimensions:** desktop reference **1920×560** (balanced ultra-wide strip; below-the-fold content stays visible). **Mobile:** *ribbon + stacked text* — the wave stays a horizontal band with gentler amplitude and fewer photos; logo / headline / cities / CTA stack inside the frosted panel; banner ~460–520px tall; CTA ≥44px tap target.
- **#3 — Delivery:** ship **both** — a **standalone self-contained HTML** file (drop-in / iframe embed, no developer needed) **and** a **developer handoff package** (clean code + optimized assets + integration notes) for native integration.

---

## 12. Build progress
- **Stage 1 (shell) — DONE.** Dark ground, 1920×560 frame, frosted panel, logo/headline/cities/CTA, brand assets extracted (`brand/`). Official two-figure HISPA logo (`brand/hispa-logo.png`) + official colored 20th mark (`brand/anniversary-20th.png`) supplied by user, used verbatim.
- **Stage 2 (static wave) — DONE.** Canvas photo band (8 photos, `photos/p1–8.jpg`), warm→cool spectrum, feathered edges. Display order `[1,5,4,6,3,8,7,2]`; per-photo `focalY` favors faces over sponsor logos.
- **Stage 3 (motion) — DONE.** Seamless loop: sine ripple, staggered per-cell photo fade, drifting filmstrip, spectrum wash confined to the band, traveling shimmer, warm motes, faint grid. `prefers-reduced-motion` freezes to a still. Tweaks: `motionIntensity`, `colorWash`, `showMotes`. *(User preference observed: they run it very subtle — motionIntensity ~0.1, colorWash ~0.15. Defaults left at 1 / 0.55; user tunes via Tweaks.)*
- **Stage 4 (mobile + perf) — DONE.** Two-stage responsive architecture: desktop stage (1920×560) and a dedicated **mobile stage (390×548)**, switched by container width <640px, each scaled-to-fit. Mobile = ribbon wave up top (gentler amp, top+bottom scrims) + stacked frosted panel (logo, eyebrow, headline, wrapping city row, full-width CTA). Perf: single global rAF loop, paused on tab-hidden (`visibilitychange`) and off-screen (`IntersectionObserver`), rAF-debounced `ResizeObserver` (no console warnings). Verified: mobile renders correctly at 380–390px; console clean.
  - **Load-race hardening (verifier-caught, fixed):** on a cold load `wrap.clientWidth` can read `0` inside `componentDidMount`, which previously forced `mode='mobile'` + `scale(0)` + `height:0` (blank hero). Fixed with three safeguards: (1) **zero-width guard** in `fit()` — a `0`/falsy width retries next frame and never drives mode/scale; (2) wrap **height comes from CSS `aspect-ratio`** (set only from `componentDidMount`/`componentDidUpdate`), never a JS `height`, so it's never collapsed; (3) `fit()` writes **only `transform`** (which doesn't resize the wrap), so the **ResizeObserver calls `fit()` directly** — no rAF debounce to deadlock, and no "ResizeObserver loop" console warning. Verified: desktop cold load correct + clean console; forced `width:0` stays desktop/valid transform; `resize`→narrow switches to mobile (`ar 390/548`, canvas `390×548`) cleanly.
  - *Note for future sessions:* synthetic `wrap.style.width` injection in screenshots does NOT reliably fire the ResizeObserver in the capture sandbox — dispatch a `window 'resize'` event after narrowing, or load fresh at a real narrow viewport, to exercise the real path.
- **Stage 6 (film-reel redesign) — DONE (desktop).** User pivoted the concept: a **flat 2D film wheel** (top-right) with a **genuinely 3D film ribbon** (Three.js / WebGL r128, loaded from jsDelivr) twisting/cascading down out of it. Desktop stage is now **1920×820**. The ribbon = a custom twisting `BufferGeometry` along a CatmullRom zig-zag, textured with the film strip (`buildStrip`), spectrum tint via vertex colors (respects `colorWash`), real lights (warm→cool point lights), `DoubleSide` with darker back face. The wheel = a face-on unlit `CircleGeometry` with a 2D reel-face canvas texture, slowly spinning. Renderer uses `preserveDrawingBuffer:true`. Photo squish fixed (texture repeat was applied twice → ~140 frames; now `repeat≈0.62` → ~5 legible frames). Mobile UNCHANGED: 2D film ribbon on a sine, **reel/wheel hidden** (per user). Robustness: IntersectionObserver only pauses after first real visibility (never blocks initial start); an initial `frame(0)` renders immediately so it's never blank; loop still pauses on tab-hidden.
  - *Verification note:* the preview/capture reports `document.hidden=true`, so the rAF loop stays paused there (correct off-screen behavior); the initial `frame(0)` + `preserveDrawingBuffer` still give a visible static frame to screenshot. On the real visible page it animates.
- **Stage 5/final (polish + delivery) — PENDING:** standalone HTML must be re-bundled (now also inlines three.js) + dev handoff package.
