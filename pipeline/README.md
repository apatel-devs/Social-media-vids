# Build pipeline code

**This folder exists because the render code was lost on 2026-11-02.**

Finished media was always pushed to this repo; the Python that produced it
never was. It lived only in an ephemeral container, and when that container
was wiped, `video_template.py`, `essay_variants.py`, `essay_motion.py`,
`reel_kit.py` and every `make_*.py` went with it. The project's memory files
recorded the format *rules* (durations, fps, card order, the lock format's
description) but not the implementation, so the rebuild below is a
reconstruction, not a recovery.

`git push` over HTTPS works from the build environment even though
`gh api` writes are blocked by the proxy. So: **commit the code here every
time it changes.** Nothing else survives.

## Files

- `dl_cards.py` — @dharmalockapp template, **measured off the real finished
  cards committed in this repo** (`images/gita_grief/*.png`, `videos/*.mp4`)
  after a from-notes rebuild was rejected. Carousel is **1080x1350 (4:5)**,
  the reel is 1080x1920 @ **25fps**. Cream `#FFFDF9` page, white rounded card
  at x72-1008/y212-997 r28, temple crop in its bottom-right, brand rust
  `#C1440E`, Anton 78px headlines split black/rust, body copy 31px *outside*
  the card, outlined source pill. Verse card sits high (y57-613) with the
  phone mockup under it.
- `grief_check.py` — re-renders the real `images/gita_grief` post with
  `dl_cards` so it can be diffed against the committed originals.
  **Run it after any change.**
- `make_ek_cards.py` — the 2026-11-02 Ekalavya carousel, as a worked example.
- `dl_reel.py` — the Instagram reel template, measured 2026-11-03 off the
  real Karwa Chauth reel plus the reels in `videos/`. **The reel is not the
  carousel scaled up:** 1080x1920 @ 25fps, pure white page (the carousel page
  is cream), card x32-1050 / y300-1478 r34, Anton 94px hook, outlined pill
  bottom-left and "check it out ->" bottom-right inside the card, no body
  paragraph, and the phone mockup scaled 1.37x on verse slides. Slides are
  joined by **hard cuts, never a crossfade** — each slide plays its own
  entrance animation and that carries the motion. Measured cut points on the
  reference: 2.84 / 6.88 / 11.28 / 15.68 / 19.92, i.e. hook 2.84s and ~4.2s
  per content slide. The reel ends on the question card; no CTA poster.
- `make_ek_reel.py` — the Ekalavya reel, as a worked example.
- `omni_kit.py` — @dharmalock_omnipeace LOCK format. **Measured off a real
  posted video** (Ambe Ma / Devi Mahatmyam 2), not described from notes: every
  type size, colour, band position and animation timing in its docstring was
  read off the reference frame by frame. Serif is EB Garamond; labels, badge,
  header and handle are Poppins Bold. Ships SILENT — Avi adds a trending sound
  and posts natively.
- `omni_ambe_check.py` — re-renders that exact reference post and diffs the
  vertical position of all 16 text bands against the measured original.
  **Run it after any change to `omni_kit.py`.** Every band should land within
  ~5px. This is the regression test for the template.
- `omni_ekalavya.py` — the 2026-11-02 Omni post, as a worked example of the
  content shape: struck claim, correction, reframe, "WHAT THE TEXT SAYS"
  body in two short paragraphs, closing couplet, source badge.

An earlier `omni_lock_RECONSTRUCTION.py` was built from a four-line prose
description and rejected outright. It is deleted. The lesson: a format that
was iterated over many rounds cannot be recovered from a changelog of
decisions — recover it from an actual artifact.

Assets all load from `../assets/`.

## The paint-gate (both renderers)

Recording starts the moment the browser context is created, so a naive clip
begins before the webfonts have painted — the DHARMA LOCK banner pops in a
frame or two late and the whole thing reads as glitchy. Avi caught this on
2026-11-02: "the dharma lock banner on top should be constant and not a part
of any transition."

Both `kit.py` and `omni_kit.py` now gate every animation:

    body:not(.go) *{animation-play-state:paused !important;}

and the recorder waits for `document.fonts.ready` plus two composited frames,
marks that instant as the trim point, and only then adds `.go`. Frame 0 is
therefore the settled static page with the banner already on it.

**`!important` is load-bearing.** Every animated rule uses the `animation`
shorthand, which resets `animation-play-state` to `running` and silently wins
the cascade over a plain paused declaration. Without it the pause does
nothing and the fades appear to have already finished on frame 0.

Also: the tail wait after the animation must exceed the clip length by ~900ms,
or ffmpeg trims past the end of the recording and the output comes up short.

