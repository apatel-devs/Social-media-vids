import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dl_reel as R, stoppedpraying_content as L
from _guard import preflight
preflight()
A = pathlib.Path(__file__).resolve().parent.parent / "assets"
# This one is reassurance, not a rally. week-5 carried the last Dharma Lock
# reel so it does not go twice running; ludum-dare-38-05 has never shipped
# here and sits under a verse that tells someone they are not lost.
TRACK = "ludum-dare-38-05.ogg"

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
        p = R.OUT / f"spc{i}.mp4"; R.clip(h, p, d); clips.append(p); print("clip", i)
    R.join(clips, R.OUT / "sp_reel_silent.mp4")
    R.music(R.OUT / "sp_reel_silent.mp4", A / "audio" / TRACK,
            R.OUT / "dharmalock_stoppedpraying_REEL.mp4")
    print("done")
