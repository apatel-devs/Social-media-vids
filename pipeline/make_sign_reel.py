import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dl_reel as R, sign_content as L
from _guard import preflight
preflight()
A = pathlib.Path(__file__).resolve().parent.parent / "assets"
# ludum-dare-38-05 carried BOTH yesterday's Dharma Lock reel and the Amy cut
# (Avi asked for the same song on Amy), so it is parked for a while or these
# accounts start to sound like one track. vgma-challenge-25 has never
# shipped anywhere and suits a hook that is a joke before it is a lesson.
# Six of the thirteen cues in assets/audio have been used so far.
TRACK = "vgma-challenge-25.ogg"

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
        p = R.OUT / f"sgc{i}.mp4"; R.clip(h, p, d); clips.append(p); print("clip", i)
    R.join(clips, R.OUT / "sg_reel_silent.mp4")
    R.music(R.OUT / "sg_reel_silent.mp4", A / "audio" / TRACK,
            R.OUT / "dharmalock_sign_REEL.mp4")
    print("done")
