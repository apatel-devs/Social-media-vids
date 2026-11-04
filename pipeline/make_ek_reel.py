import sys; sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import dl_reel as R
from _guard import preflight
preflight()

V1_DEV = ["उद्धरेदात्मनात्मानं नात्मानमवसादयेत्।",
          "आत्मैव ह्यात्मनो बन्धुरात्मैव रिपुरात्मनः॥"]
V2_DEV = ["न हि ज्ञानेन सदृशं पवित्रमिह विद्यते।",
          "तत्स्वयं योगसंसिद्धः कालेनात्मनि विन्दति॥"]

SLIDES = [
 (R.hook([("THEY WOULDN'T", False), ("TEACH HIM.", False), ("HE LEARNED ANYWAY.", True)],
         "he practised in front of a statue.", "MAHABHARATA"), R.D_HOOK),
 (R.verse("BHAGAVAD GITA", "You are your own friend and your own enemy",
          "CHAPTER 6, VERSE 5",
          ["Nobody was coming to teach him. Krishna had already said",
           "who the work actually belongs to."],
          V1_DEV, "Uddhared atmanatmanam natmanam avasadayet",
          "Pull yourself up. Don't let yourself sink. You are your own best friend, and your own worst enemy."), R.D_SLIDE),
 (R.verse("BHAGAVAD GITA", "Nothing in this world purifies like knowledge",
          "CHAPTER 4, VERSE 38",
          ["He had no teacher and no permission. He still ended up",
           "with the thing they were guarding."],
          V2_DEV, "Na hi jnanena sadrisham pavitram iha vidyate",
          "Nothing changes you like really knowing something. Keep going, and one day you find it inside you."), R.D_SLIDE),
 (R.closing([("WHAT ARE YOU", False), ("WAITING FOR SOMEONE", False), ("TO GIVE YOU?", True)]), R.D_SLIDE),
]

if __name__ == "__main__":
    if sys.argv[1:] and sys.argv[1] == "png":
        for i,(h,_) in enumerate(SLIDES,1):
            R.shot(h, R.OUT/f"reel_{i}.png")
        print("stills")
    else:
        clips=[]
        for i,(h,d) in enumerate(SLIDES,1):
            p=R.OUT/f"c{i}.mp4"; R.clip(h,p,d); clips.append(p); print("clip",i)
        R.join(clips, R.OUT/"reel_silent.mp4")
        R.music(R.OUT/"reel_silent.mp4",
                str(__import__("pathlib").Path(__file__).resolve().parent.parent/"assets"/"audio")+"/vgma-challenge-25.ogg",
                R.OUT/"dharmalock_ekalavya_REEL.mp4")
        print("done")
