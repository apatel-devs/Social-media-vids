#!/usr/bin/env python3
"""
TEMPLATE LOCK. Run this before building or publishing anything.

    python3 pipeline/verify.py

Exits 0 only if every template still renders what it is supposed to render.
Exits 1 and says what moved otherwise. Nothing should be built or posted
from a tree where this fails.

Why it exists
-------------
On 2026-11-02 the build container was wiped. The render code had never been
committed, so the templates were rebuilt from a few lines of prose notes and
came out wrong in almost every respect - wrong aspect ratio, wrong fonts,
wrong structure. One of those rebuilds was published before anyone noticed.
Avi, 2026-11-03: "I need to make sure that posts going forward are never
changed... It needs to be saved and taken care of."

So this does not rely on anyone remembering anything.

Two layers
----------
1. FIDELITY - each template re-renders the real post it was measured from,
   and its ink distribution is compared against the genuine published
   artifact in reference/originals/. This is what stops a rebuild from
   drifting away from the real design - wrong aspect ratio, wrong structure,
   blocks in the wrong place all fail here.

2. DRIFT LOCK - the same renders are compared pixel-by-pixel against the
   goldens in reference/golden/, which are this renderer's own frozen
   output. Any edit that changes what comes out fails here, loudly, even if
   it still passes the fidelity check.

If a change is deliberate, look at the diff images written to out/, confirm
they are right, then regenerate the goldens:

    python3 pipeline/verify.py --bless

Never bless to make a red check go green. The goldens are the contract.
"""
import sys, pathlib, json
import numpy as np
from PIL import Image, ImageFilter

REPO = pathlib.Path(__file__).resolve().parent.parent
ORIG = REPO / "reference" / "originals"
GOLD = REPO / "reference" / "golden"
OUT = REPO / "out"
OUT.mkdir(exist_ok=True)
GOLD.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

PIXEL_TOL = 2.0     # mean abs 0-255 difference allowed against a golden
# Different Chromium builds antialias text slightly differently, which showed
# up as mean ~2.2 between two machines running identical code. Both sides are
# softened before diffing so sub-pixel AA collapses while any real move -
# a changed size, colour or position - still registers far above the tolerance.
COMPARE_BLUR = 1.6


def _profile(path):
    """Coarse ink distribution. Robust to anti-aliasing and compression,
    sensitive to anything structural: aspect ratio, where blocks sit, how
    much of the frame they occupy."""
    a = np.asarray(Image.open(path).convert("L")).astype(float)
    ink = 255.0 - a
    ink[ink < 12] = 0.0                       # ignore paper texture
    h, w = ink.shape
    rows = ink.sum(axis=1)
    cols = ink.sum(axis=0)

    def buckets(v, n):
        idx = (np.arange(len(v)) * n // len(v)).clip(0, n - 1)
        out = np.zeros(n)
        np.add.at(out, idx, v)
        s = out.sum()
        return out / s if s else out

    return (h, w), buckets(rows, 120), buckets(cols, 96)


def _corr(a, b):
    if a.std() == 0 or b.std() == 0:
        return 1.0 if np.allclose(a, b) else 0.0
    return float(np.corrcoef(a, b)[0, 1])


# Floors, not match scores. These renderers are reconstructions, so they do
# not trace the originals pixel for pixel - line breaks and the temple
# watermark legitimately differ. Measured 2026-11-03 against the real posts:
#   carousel hook 0.71/0.80, verse 0.57/1.00, refl 0.89/0.58,
#   omni locked and final both above 0.9.
# The floors exist to catch a catastrophic rebuild - wrong aspect ratio, a
# missing card, content in the wrong half of the frame. Exact drift is the
# golden layer's job, and that one is strict.
ROW_MIN, COL_MIN = 0.50, 0.50
# Absolute floors alone are too loose to protect a --bless: a 40px shift of
# a whole column still clears them. So each render's correlation against the
# real post is also recorded in reference/golden/fidelity.json when blessed,
# and may not fall more than FIDELITY_SLIP below its own baseline.
FIDELITY_SLIP = 0.05
FID_FILE = GOLD / "fidelity.json"


def compare_bands(name, got_png, ref_png, fails, baselines, record):
    """Fidelity: does this still look structurally like the published post?"""
    (gh, gw), grow, gcol = _profile(got_png)
    (rh, rw), rrow, rcol = _profile(ref_png)
    if (gh, gw) != (rh, rw):
        fails.append(f"{name}: renders {gw}x{gh}, the real post is {rw}x{rh}")
        return
    r, c = _corr(grow, rrow), _corr(gcol, rcol)
    record[name] = [round(r, 4), round(c, 4)]
    if r < ROW_MIN or c < COL_MIN:
        fails.append(f"{name}: layout no longer matches the real post "
                     f"(vertical {r:.2f}/{ROW_MIN}, horizontal {c:.2f}/{COL_MIN})")
        return
    base = baselines.get(name)
    if base:
        br, bc = base
        if r < br - FIDELITY_SLIP or c < bc - FIDELITY_SLIP:
            fails.append(f"{name}: drifted away from the real post "
                         f"(vertical {r:.2f} was {br:.2f}, "
                         f"horizontal {c:.2f} was {bc:.2f})")


def compare_golden(name, got_png, fails):
    gp = GOLD / pathlib.Path(got_png).name
    if not gp.exists():
        fails.append(f"{name}: no golden committed ({gp.name}) - run --bless")
        return
    def soft(path):
        im = Image.open(path).convert("RGB")
        return np.asarray(im.filter(
            ImageFilter.GaussianBlur(COMPARE_BLUR))).astype(int)
    a, b = soft(got_png), soft(gp)
    if a.shape != b.shape:
        fails.append(f"{name}: size {a.shape[1]}x{a.shape[0]}, "
                     f"golden is {b.shape[1]}x{b.shape[0]}")
        return
    diff = np.abs(a - b).mean()
    if diff > PIXEL_TOL:
        d = (np.abs(a - b).sum(axis=2) > 24).astype(np.uint8) * 255
        Image.fromarray(d).save(OUT / f"DIFF_{pathlib.Path(got_png).name}")
        fails.append(f"{name}: differs from golden (mean {diff:.2f} > "
                     f"{PIXEL_TOL}) - see out/DIFF_{pathlib.Path(got_png).name}")


def render_all():
    """Re-render the three reference posts. Returns [(name, png, original)]."""
    import dl_cards as C, omni_kit as O, dl_reel as R
    import grief_check as _g          # noqa: F401  (defines the gita_grief post)
    import omni_ambe_check as _o      # noqa: F401  (defines the Ambe Ma post)

    made = []
    # carousel - the real gita_grief post
    C.shot(_g.HOOK, OUT / "v_carousel_hook.png")
    C.shot(_g.VERSE, OUT / "v_carousel_verse.png")
    C.shot(_g.REFL, OUT / "v_carousel_refl.png")
    made += [("carousel hook", OUT / "v_carousel_hook.png", ORIG / "carousel_hook_REAL.png"),
             ("carousel verse", OUT / "v_carousel_verse.png", ORIG / "carousel_verse_REAL.png"),
             ("carousel refl", OUT / "v_carousel_refl.png", ORIG / "carousel_refl_REAL.png")]

    # omni - the real Ambe Ma post, locked state and open state
    html = O.page(**_o.REF)
    O.shot(html, OUT / "v_omni_locked.png", 2.6)
    O.shot(html, OUT / "v_omni_final.png", 9.0)
    made += [("omni locked", OUT / "v_omni_locked.png", ORIG / "omni_locked_REAL.png"),
             ("omni final", OUT / "v_omni_final.png", ORIG / "omni_final_REAL.png")]
    return made


def main():
    bless = "--bless" in sys.argv
    fails = []
    baselines = json.loads(FID_FILE.read_text()) if FID_FILE.exists() else {}
    record = {}
    made = render_all()

    for name, got, orig in made:
        if orig.exists():
            compare_bands(name, got, orig, fails, baselines, record)

    if bless:
        # Blessing is how a deliberate change is accepted. It is NOT a way to
        # silence a failure: if a render no longer resembles the real
        # published post, refuse outright rather than freeze the mistake in
        # as the new contract. That is exactly how a wrong template would
        # become permanent.
        if fails:
            print("REFUSING TO BLESS - these renders no longer match the "
                  "real published posts:\n")
            for f in fails:
                print("  x", f)
            print("\nFix the template first. Blessing here would make the "
                  "break the new baseline.")
            return 1
        for _, got, _o in made:
            Image.open(got).save(GOLD / pathlib.Path(got).name)
        FID_FILE.write_text(json.dumps(record, indent=2, sort_keys=True))
        print(f"blessed {len(made)} goldens into reference/golden/")
        return 0

    for name, got, _o in made:
        compare_golden(name, got, fails)

    if fails:
        print("TEMPLATE CHECK FAILED - do not build or post from this tree\n")
        for f in fails:
            print("  x", f)
        print("\nIf the change was intentional, review the DIFF_* images in "
              "out/ and re-run with --bless.")
        return 1

    print(f"template check passed - {len(made)} renders match both the real "
          f"posts and the committed goldens")
    return 0


if __name__ == "__main__":
    sys.exit(main())
