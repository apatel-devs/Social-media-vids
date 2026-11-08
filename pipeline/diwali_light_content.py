# -*- coding: utf-8 -*-
"""
@dharmalockapp — Diwali, 2026-11-08. Second post of the day.
Avi asked for one on light overcoming darkness.

THE HOOK
Darkness has never put out a single flame. Light a match in a dark room and
the dark loses instantly; there is no version of it that runs the other way.
That is the whole post. It is the simplest true thing about the theme and it
is physical, so it lands in one read.

WHY NOT THE OBVIOUS ANGLE
Avi sent @gita.talk's Diwali post as a reference: struck line "Diwali is just
lights and sweets", corrected to "Diwali is a war on darkness", then "the
light isn't in the diya, it's seated in your heart" and "you don't light
diyas to chase the dark away - you light them to remember the light was
always yours", badged Gita 13.17.

The first draft of this file said almost exactly that - the lamp is lit
inside you, you do not beat the dark from outside - and had 13.17 on its
shortlist. Avi's standing rule is that nothing can let his friend say he
copied him, so the angle moved. Three replacements were pitched (the diya
burns out by morning; the lamps face outward; Diwali is set on the new moon)
and Avi rejected all three as too clever: "Keep it simple."

So this one does not argue with his post, and it does not out-think it. It
states the asymmetry and stops. Note it quietly lands somewhere different
anyway: his says Diwali is a war; this says there was never a fight.

FACT CHECK
  * Gita 10.11 Devanagari, transliteration and sense verified at
    shlokam.org/gita/gita-10-11.htm - tamah (darkness), ajnanajam (born of
    ignorance), jnana-dipena bhasvata (by the shining lamp of knowledge).
  * Pavamana mantra = Brihadaranyaka Upanishad 1.3.28. Verse number confirmed
    on swami-krishnananda.org's Brihadaranyaka I.3 commentary, which numbers
    it 28 under Chapter I, Third Brahmana. Devanagari and the standard
    translations cross-checked against Wikipedia's Pavamana Mantra entry.

  NOT printed: the "Om" and the closing "Om shantih shantih shantih". Nearly
  every version online carries them; they are not in the Upanishad's text.

  VERSE NUMBERING: 10.11 is 10.11 in every edition. Gita 13.17 was dropped
  partly for the copying reason above and partly because it is 13.18 wherever
  the arjuna uvaca line is counted, and a good share of this audience reads
  one of those editions.

  NOT claimed: that physics says darkness is "only an absence". The hook is
  an observation anyone can run in their own kitchen, not a science claim,
  and the copy keeps it that way.
"""
CHIP = "DIWALI"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("DARKNESS HAS NEVER", False),
        ("PUT OUT A SINGLE", False),
        ("FLAME.", True)]
BODY = ["Light one match in a dark room and the dark loses.",
        "Now try it the other way around. You cannot. Dark",
        "cannot walk into a lit room and switch it off."]
PILL = "BHAGAVAD GITA"

V1 = dict(
    source="BHAGAVAD GITA",
    title="He does not fight the dark. He lights a lamp",
    reference="CHAPTER 10, VERSE 11",
    gloss=["No battle in this verse. One lamp, and the thing",
           "that was never going to win is already gone."],
    devanagari=["तेषामेवानुकम्पार्थमहमज्ञानजं तमः ।",
                "नाशयाम्यात्मभावस्थो ज्ञानदीपेन भास्वता ॥"],
    translit="Nashayamy atma-bhava-stho jnana-dipena bhasvata",
    translation="I burn off the dark that ignorance made, with one bright lamp of knowing.",
)

V2 = dict(
    source="BRIHADARANYAKA UPANISHAD",
    title="Lead me from the darkness to the light",
    reference="VERSE 1.3.28",
    gloss=["The oldest line about tonight. It is three words",
           "long in Sanskrit and people still say it at 3am."],
    devanagari=["असतो मा सद्गमय ।",
                "तमसो मा ज्योतिर्गमय ।",
                "मृत्योर्मा अमृतं गमय ॥"],
    translit="Asato ma sad gamaya, tamaso ma jyotir gamaya, mrityor ma amritam gamaya",
    translation="Lead me from the unreal to the real, from darkness to light, from death to the life that does not end.",
)

TURN = ["&ldquo;It was never a fair fight.",
        "That is the good news.&rdquo;"]

REEL_SUB = "it has never won once."
REEL_CLOSE = [("WHAT ARE YOU", False),
              ("STILL SITTING", False),
              ("IN THE DARK ABOUT?", True)]
