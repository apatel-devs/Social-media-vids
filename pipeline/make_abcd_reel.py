"""Dharma Lock reel — SILENT from 2026-11-23 on.

Avi: "give me these videos without any sound from now on so I can put
trending audio on Both." Both = Dharma Lock and Omni. Omni has always
shipped silent; this is the Dharma Lock reel joining it.

So there is no R.music step here. The joined clip IS the deliverable, and
it carries no audio stream at all - which is correct for this account,
unlike Amy, where stripping audio would have killed the CTA voiceover (see
amy_assemble.py). Nothing on a Dharma Lock reel speaks.

Do not "restore" the music call below. If a future post needs a bed, copy
an older make_*_reel.py instead and leave this pattern alone.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dl_reel as R, abcd_content as L
from _guard import preflight
preflight()

SLIDES = [
 (R.hook(L.HEAD, L.REEL_SUB, "BHAGAVAD GITA"), R.D_HOOK),
 (R.verse(L.V1["source"], L.V1["title"], L.V1["reference"], L.V1["gloss"],
          L.V1["devanagari"], L.V1["translit"], L.V1["translation"]), R.D_SLIDE),
 (R.verse(L.V2["source"], L.V2["title"], L.V2["reference"], L.V2["gloss"],
          L.V2["devanagari"], L.V2["translit"], L.V2["translation"]), R.D_SLIDE),
 (R.closing(L.REEL_CLOSE), R.D_SLIDE),
]

if __name__ == "__main__":
    clips = []
    for i, (h, d) in enumerate(SLIDES, 1):
        p = R.OUT / f"abc2{i}.mp4"; R.clip(h, p, d); clips.append(p); print("clip", i)
    R.join(clips, R.OUT / "dharmalock_abcd_SILENT.mp4")
    print("done")
