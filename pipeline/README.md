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

- `kit.py` — @dharmalockapp card builders + record/stitch/music.
  25fps (never 30), HOOK 1.8 / VERSE 4.0 / CTA 2.8, cover at 1150ms,
  `slideleft` transitions only, music at volume 0.6 with a 1.0s fade.
  `record_slide()` records the page so the CSS entrance animations are in
  the clip, and trims to the measured first paint.
- `ekalavya.py` — the 2026-11-02 post: hook, two phone-mockup verse cards,
  YOUR TURN card, CTA. `python3 ekalavya.py png` for the TikTok carousel,
  `python3 ekalavya.py video` for the Instagram reel.
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

