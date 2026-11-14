import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dl_reel as R, ipadkid_content as L
from _guard import preflight
preflight()
A = pathlib.Path(__file__).resolve().parent.parent / "assets"
# Upbeat but not the hype track - this one is a joke that turns serious, and
# week-6 (140bpm) would make it read as a rant. week-5 has not shipped on
# Dharma Lock and is melodic rather than driving.
TRACK = "week-5---seven-reasons-why-melody.ogg"

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
        p = R.OUT / f"ikc{i}.mp4"; R.clip(h, p, d); clips.append(p); print("clip", i)
    R.join(clips, R.OUT / "ik_reel_silent.mp4")
    R.music(R.OUT / "ik_reel_silent.mp4", A / "audio" / TRACK,
            R.OUT / "dharmalock_ipadkid_REEL.mp4")
    print("done")
