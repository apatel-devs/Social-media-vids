"""Ekalavya for @dharmalockapp, in the real template (dl_cards)."""
import sys, shutil, pathlib
sys.path.insert(0,"/home/claude/dl")
import dl_cards as D

G = lambda *c: [chr(int(x,16)) for x in c]
V1_DEV = ["उद्धरेदात्मनात्मानं नात्मानमवसादयेत्।",
          "आत्मैव ह्यात्मनो बन्धुरात्मैव रिपुरात्मनः॥"]
V2_DEV = ["न हि ज्ञानेन सदृशं पवित्रमिह विद्यते।",
          "तत्स्वयं योगसंसिद्धः कालेनात्मनि विन्दति॥"]

D.shot(D.hook_card(
    chip="GITA WISDOM",
    head_lines=[("THEY WOULDN'T TEACH HIM.", False),
                ("HE LEARNED ANYWAY.", True)],
    body_lines=["Drona turned Ekalavya away at the door. So he built a",
                "statue of the man who refused him, and taught himself",
                "in front of it. Then they came for his thumb."],
    pill="MAHABHARATA"), D.OUT/"ek2_1_hook.png")

D.shot(D.verse_card(
    source="BHAGAVAD GITA",
    title="You are your own friend and your own enemy",
    reference="CHAPTER 6, VERSE 5",
    gloss=["Nobody was coming to teach him. Krishna had already said who",
           "the work actually belongs to."],
    devanagari=V1_DEV,
    translit="Uddhared atmanatmanam natmanam avasadayet",
    translation="Pull yourself up. Don't let yourself sink. You are your own best friend, and your own worst enemy.",
    n=1, total=2), D.OUT/"ek2_2_verse1.png")

D.shot(D.verse_card(
    source="BHAGAVAD GITA",
    title="Nothing in this world purifies like knowledge",
    reference="CHAPTER 4, VERSE 38",
    gloss=["He had no teacher and no permission. He still ended up with",
           "the thing they were guarding."],
    devanagari=V2_DEV,
    translit="Na hi jnanena sadrisham pavitram iha vidyate",
    translation="Nothing changes you like really knowing something. Keep going, and one day you find it inside you.",
    n=2, total=2), D.OUT/"ek2_3_verse2.png")

D.shot(D.reflection_card("YOUR TURN",
    ["&ldquo;Nobody handed Ekalavya a teacher.",
     "He started anyway.&rdquo;"]), D.OUT/"ek2_4_refl.png")

shutil.copy("/tmp/pushtest/images/gita_grief/04_cta.png", D.OUT/"ek2_5_cta.png")
print("cards done")
