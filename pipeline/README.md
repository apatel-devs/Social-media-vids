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
- `omni_lock_RECONSTRUCTION.py` — @dharmalock_omnipeace lock format.
  **Rejected by Avi on 2026-11-02** ("absolutely garbage... nothing compared
  to what we had before"). It was built from a four-line prose description of
  a format that had actually been iterated across four variants. Do not treat
  it as the house style. Rebuild against a real posted video from the account
  and replace this file.

Assets all load from `../assets/`.
