"""
Ekalavya — @dharmalockapp, 2026-11-02.

Content model Avi sent: a myth retold as a modern wound (the @gita.talk
Abhimanyu post). NOT Abhimanyu — that is the exact post his friend made and
Avi said on 10/29 "I don't want my friend saying I copied him."

FACT CHECK — Mahabharata, Adi Parva, Sambhava Parva, Section CXXXIV
(Ganguli, ibiblio.org/sripedia m01/m01135): Drona "accepted not the prince as
his pupil in archery, seeing that he was a Nishada"; Ekalavya "made a
clay-image of Drona, and began to worship it"; Drona asked for "the thumb of
thy right hand" and Ekalavya "cut off without ado his thumb."

Verses verified: Gita 6.5 and Gita 4.38. Neither used on this account before.
Copy written to the plain-language bar: short sentences, spoken words.
"""
import sys
sys.path.insert(0, "/home/claude/dl")
import kit as K

BADGE = "MAHABHARATA &middot; ADI PARVA"

HOOK_BIG = ["THEY WOULDN'T", "TEACH HIM.", "HE LEARNED", "ANYWAY."]
HOOK_SMALL = ("They told him no. So he built a statue of the teacher "
              "and taught himself. Then they asked for his thumb.")

V1 = dict(
    label="BHAGAVAD GITA 6.5",
    gloss="NOBODY WAS COMING",
    devanagari=[
        "उद्धरेदात्म"
        "नात्मानं "
        "नात्मानमवसा"
        "दयेत् ।",
        "आत्मैव ह्यात"
        "्मनो बन्धुर"
        "ात्मैव रिपु"
        "रात्मन: ॥"],
    translit="Uddhared atmanatmanam natmanam avasadayet",
    translation="Pull yourself up. Don't let yourself sink. You are your own "
                "best friend, and your own worst enemy.",
)

V2 = dict(
    label="BHAGAVAD GITA 4.38",
    gloss="THE SKILL WAS ALWAYS HIS",
    devanagari=[
        "न हि ज्ञानेन "
        "सदृशं पवित्"
        "रमिह विद्यत"
        "े ।",
        "तत्स्वयं यो"
        "गसंसिद्ध: का"
        "लेनात्मनि व"
        "िन्दति ॥"],
    translit="Na hi jnanena sadrisham pavitram iha vidyate",
    translation="Nothing changes you like really knowing something. "
                "Keep going, and one day you find it inside you.",
)

TURN_TAG = "YOUR TURN"
TURN_Q = ["WHAT ARE YOU", "WAITING FOR", "SOMEONE TO", "<em>GIVE YOU?</em>"]
TURN_SUB = "Nobody handed Ekalavya a teacher. He started anyway."

CARDS = [
    ("1_hook", lambda: K.build_hook_anim(BADGE, HOOK_BIG, HOOK_SMALL),
     K.HOOK_DURATION, 1.8),
    ("2_verse1", lambda: K.build_verse_anim(n=1, total=2, **V1),
     K.VERSE_DURATION, 1.5),
    ("3_verse2", lambda: K.build_verse_anim(n=2, total=2, **V2),
     K.VERSE_DURATION, 1.5),
    ("4_turn", lambda: K.build_dialogue_anim(
        TURN_TAG, "".join(f"<div>{l}</div>" for l in TURN_Q), TURN_SUB),
     K.DIALOGUE_DURATION, 1.5),
    ("5_cta", lambda: K.build_cta_anim(), K.CTA_DURATION, 1.9),
]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "png"
    if mode == "png":
        for name, fn, _d, settle in CARDS:
            K.capture_png(fn(), K.OUT / f"ek_{name}.png", settle_s=settle)
            print("still", name)
    else:
        clips = []
        for name, fn, d, _s in CARDS:
            p = K.OUT / f"clip_{name}.mp4"
            K.record_slide(fn(), d, p)
            clips.append(p)
            print("clip", name)
        K.stitch_clips(clips, K.OUT / "ek_silent.mp4")
        print("stitched")
