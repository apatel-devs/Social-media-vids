# Build pipeline code

## Run this before you build or post anything

    python3 pipeline/verify.py

It exits 0 only if every template still renders what it is supposed to.
Every build script calls it automatically and refuses to run if it fails.

**Why this exists.** On 2026-11-02 the build container was wiped. The render
code had never been committed, so the templates were rebuilt from a few lines
of prose notes and came out wrong in almost every respect - wrong aspect
ratio, wrong fonts, wrong structure - and one of those rebuilds was published
before anyone noticed. Avi, 2026-11-03: *"I need to make sure that posts
going forward are never changed... It needs to be saved and taken care of."*

So nothing here depends on anyone remembering anything.

### How the lock works

`reference/originals/` holds the genuine published artifacts - the real Ambe
Ma Omni video, the real Karwa Chauth reel, the real gita_grief carousel
cards. These are the ground truth. They are committed, so no one ever has to
ask Avi for a previous video again.

`reference/golden/` holds this renderer's own frozen output.

`verify.py` re-renders each reference post and checks it twice:

1. **Fidelity** - ink distribution against the real published artifact.
   Catches a catastrophic rebuild: wrong aspect ratio, missing card, content
   in the wrong half of the frame.
2. **Drift lock** - pixel comparison against the committed golden. Strict.
   Any edit that changes output at all fails here and writes a `DIFF_*.png`
   into `out/` showing exactly which pixels moved.

A deliberate change means: look at the diffs, confirm they are right, then
`python3 pipeline/verify.py --bless`. **Never bless to turn a red check
green.** The goldens are the contract.

Paths are resolved relative to the repo, so a fresh `git clone` runs with no
setup.

## Templates

- `dl_cards.py` - @dharmalockapp carousel. **1080x1350 (4:5)**, cream
  `#FFFDF9` page, white card x72-1008 / y212-997 r28, temple crop bottom
  right, rust `#C1440E`, Anton 78px headline split black/rust, body copy 31px
  *outside* the card, outlined source pill. Verse card sits high (y57-613)
  with the phone mockup under it. Reference post: `images/gita_grief`.
- `dl_reel.py` - @dharmalockapp Instagram reel. **Not the carousel rescaled.**
  1080x1920 @ 25fps, white page, card x32-1050 / y300-1478 r34, Anton 94px
  hook, pill and "check it out ->" inside the card, no body paragraph, phone
  scaled 1.37x. Slides joined by **hard cuts** - each plays its own entrance
  animation. Hook 2.84s, content slides ~4.2s. Ends on the question card; no
  CTA poster. Reference: the Karwa Chauth reel.
- `omni_kit.py` - @dharmalock_omnipeace LOCK format, measured off the real
  Ambe Ma post. EB Garamond throughout, Poppins Bold for labels and badge.
  Ships SILENT; Avi posts it natively for the trending sound.
- `amy_caption.py` - @amysharma_dharma caption overlay. Poppins Bold 60px /
  71px, white with a ~7px black stroke, centred, wraps at 780px, block
  centred ~57% down the frame at the neck/collar line. Measured off the
  account's own live grid.

## Worked examples

- `make_ek_cards.py`, `make_ek_reel.py` - the Ekalavya carousel and reel
- `omni_ekalavya.py`, `omni_worry.py` - Omni posts
- `grief_check.py`, `omni_ambe_check.py` - the reference posts as data

## Standing rules the code must not break

- Nothing enters Post Bridge until Avi approves that specific post.
- @dharmalockapp TikTok is carousel only, never a video file.
- @dharmalock_omnipeace ships silent and does not go through Post Bridge.
- @amysharma_dharma has music baked into BOTH cuts; nothing silent there.
- Always pass `scheduled_at` explicitly - omitting it publishes immediately.
- Never post to YouTube.

## The paint-gate (both video renderers)

Recording starts before webfonts paint, so a naive clip pops the header in a
frame or two late. Both renderers gate every animation behind
`body:not(.go) *{animation-play-state:paused !important;}` and trim to the
moment after fonts are ready and two frames have composited. **The
`!important` is load-bearing** - the `animation` shorthand resets
`animation-play-state` to `running` and silently wins otherwise. The tail
wait must exceed the clip by ~900ms or ffmpeg trims past the end.
