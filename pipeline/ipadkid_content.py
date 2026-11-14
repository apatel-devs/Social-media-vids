# -*- coding: utf-8 -*-
"""
@dharmalockapp — "The kids won't put the iPad down. Neither will you."
2026-11-14.

WHOSE IDEA THIS WAS
Avi's. Offered four hooks and he came back with "what about one with desi
iPad kids / screentime", which is a better instinct than any of the four:
Dharma Lock IS a screen-time product, the iPad-kid thing is already a live
joke in this audience, and nobody in the niche points it at the adult.

WHY "THE KIDS" AND NOT "YOUR KID"
Most of this audience are young desi women, not parents. "Your kid" writes
most of them out of the first line, and the first line is the whole job
(see wantsomething_content.py for the rule and the numbers behind it).
"The kids" keeps the joke everyone already knows and still lands the turn
on the reader in line two.

THE TURN
Every screen-time post in this niche scolds children. This one says the
children learned it from the adult holding the phone, and then hands over
a verse that says exactly that, written down two thousand years before the
iPad. The app follows from the argument instead of being bolted on: it
locks YOUR phone, not theirs.

FACT CHECK
  * Gita 3.21 verified at asitis.com/3/21.html. Devanagari and
    transliteration taken from there. "Whatever action is performed by a
    great man, common men follow in his footsteps."
  * Gita 6.26 verified at vivekavani.com/b6v26/. Devanagari, IAST and
    translation from there - wherever the restless mind strays, rein it in
    and bring it back.

  NOT CLAIMED: that 3.21 is about parenting. SHRESHTHA is the great or
  leading person, and the verse is about anyone others take their cue from
  - Krishna's point to Arjuna is about his own conduct as a leader. The
  copy says "whoever they are copying", which is what the text supports.
  Do not let a later rewrite turn this into "the Gita says parents must...".

  NOT CLAIMED: any screen-time statistic. Every number floating around for
  daily phone pickups traces back to one vendor survey or another, they
  disagree wildly, and a made-up figure on a card is the fastest way to get
  the whole post dismissed. The line works without one.
"""
CHIP = "BHAGAVAD GITA"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("THE KIDS WON'T PUT", False),
        ("THE IPAD DOWN.", False),
        ("NEITHER WILL YOU.", True)]
BODY = ["Nobody is born knowing how to sit still. Children copy",
        "whoever they are watching, and the person they are",
        "watching is holding a phone."]
PILL = "CHAPTER 3"

V1 = dict(
    source="BHAGAVAD GITA",
    title="They copy what you do, not what you tell them",
    reference="CHAPTER 3, VERSE 21",
    gloss=["Krishna says people follow whoever they look up to.",
           "Whatever you do becomes the standard in the room."],
    devanagari=["यद्यदाचरति श्रेष्ठस्तत्तदेवेतरो जनः ।",
                "स यत्प्रमाणं कुरुते लोकस्तदनुवर्तते ॥"],
    translit="Yad yad acharati shreshthas tat tad evetaro janah",
    translation="Whatever the one they look up to does, everybody else does too. The standard he sets is the one the world follows.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="When it wanders off, bring it back",
    reference="CHAPTER 6, VERSE 26",
    gloss=["He does not say never get distracted. He says catch it",
           "and bring it back, every single time it goes."],
    devanagari=["यतो यतो निश्चरति मनश्चञ्चलमस्थिरम् ।",
                "ततस्ततो नियम्यैतदात्मन्येव वशं नयेत् ॥"],
    translit="Yato yato nishcharati manash chanchalam asthiram",
    translation="Wherever the restless mind runs off to, catch it there and bring it back.",
)

TURN = ["&ldquo;You cannot hand them a habit",
        "you do not have yourself.&rdquo;"]

REEL_SUB = "they learned it from somebody."
REEL_CLOSE = [("LOCK YOUR OWN PHONE", False),
              ("BEFORE YOU TAKE", False),
              ("ANYBODY ELSE'S.", True)]
