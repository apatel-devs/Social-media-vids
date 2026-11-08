import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dl_reel as R, diwali_light_content as L
from _guard import preflight
preflight()
A = pathlib.Path(__file__).resolve().parent.parent / "assets"

# week-31 went on the Chopda Pujan reel a few hours ago, so this takes the
# energetic one - the hook is blunt rather than reflective.
TRACK = "week-6---never-miss-fire.ogg"

SLIDES = [
 (R.hook(L.HEAD, L.REEL_SUB, "DIWALI"), R.D_HOOK),
 (R.verse(L.V1["source"], L.V1["title"], L.V1["reference"], L.V1["gloss"],
          L.V1["devanagari"], L.V1["translit"], L.V1["translation"]), R.D_SLIDE),
 (R.verse(L.V2["source"], L.V2["title"], L.V2["reference"], L.V2["gloss"],
          L.V2["devanagari"], L.V2["translit"], L.V2["translation"]), R.D_SLIDE),
 (R.closing(L.REEL_CLOSE), R.D_SLIDE),
]

if __name__ == "__main__":
    if sys.argv[1:2] == ["png"]:
        for i, (h, _) in enumerate(SLIDES, 1):
            R.shot(h, R.OUT / f"ltreel_{i}.png")
        print("stills")
    else:
        clips = []
        for i, (h, d) in enumerate(SLIDES, 1):
            p = R.OUT / f"ltc{i}.mp4"; R.clip(h, p, d); clips.append(p); print("clip", i)
        R.join(clips, R.OUT / "lt_reel_silent.mp4")
        R.music(R.OUT / "lt_reel_silent.mp4", A / "audio" / TRACK,
                R.OUT / "dharmalock_diwali_light_REEL.mp4")
        print("done")
