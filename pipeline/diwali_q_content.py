# -*- coding: utf-8 -*-
"""
@dharmalockapp — "If Diwali is Ram coming home, why Lakshmi?", 2026-11-05.
Diwali run-up (Dhanteras Fri Nov 6, Diwali Sun Nov 8).

SOURCE OF THE ANGLE
  Avi sent a viral @storyteller_ramesh carousel built on a child's question:
  "Papa, if Diwali is about Shree Ram coming home, why do we worship Laxmi
  Mata?" He asked for the WORDS, not that account's card design - so the
  question and the Samudra Manthan answer carry over, written in our own
  voice on our own template. Their slide copy is NOT reproduced.

FACT CHECK - the sequence is the whole point of this post, so it was checked
against the text rather than against the viral post.
  * Bhagavata Purana 8.7: the halahala poison comes up first and Shiva
    drinks it. SB 8.8.1 opens "pite gare vrsankena" - "when the poison had
    been drunk by Lord Siva" - confirming the poison preceded everything
    below.
  * SB 8.8.1-7: Surabhi, Uchchaihshrava, Airavata, the Kaustubha gem, the
    Parijata, the Apsaras.
  * SB 8.8.8: Lakshmi herself appears. Verified Devanagari and transliteration
    (vedapath.app, srimad-bhagavatam.github.io/canto8/8).
  * SB 8.8.30-34: Varuni, then Dhanvantari last, carrying the amrita.
  So the poison really did come out of that ocean before she did. That is the
  reflection card, and it is load-bearing - do not soften it into a metaphor
  that the text does not support.

  NOT claimed as scripture: that the churning happened on Kartik Amavasya.
  The Puranas do not date it. That link is traditional, so the copy says the
  old story puts her there, not that a verse does.

  Gita 9.22 Devanagari and translation verified at shlokam.org/gita/gita-9-22.
"""
CHIP = "DIWALI"
# Line 3 is kept short on purpose: the temple crop sits bottom-right of the
# card and a longer third line runs into it.
HEAD = [("IF DIWALI IS RAM", False),
        ("COMING HOME,", False),
        ("WHY LAKSHMI?", True)]
BODY = ["A nine year old asked his dad that this week, and it is",
        "a better question than it sounds. Diwali night is Kartik",
        "Amavasya. The old story puts her coming out of the ocean."]
PILL = "BHAGAVATA PURANA"

V1 = dict(
    source="BHAGAVATA PURANA",
    title="Then she came up out of the water",
    reference="CANTO 8, CHAPTER 8, VERSE 8",
    gloss=["Nobody sent for her. The gods and the demons were dragging a",
           "mountain back and forth, and she simply surfaced."],
    devanagari=["ततश्चाविरभूत् साक्षाच्छ्री रमा भगवत्परा ।",
                "रञ्जयन्ती दिश: कान्त्या विद्युत् सौदामनी यथा ॥"],
    translit="Tatas cavirabhut sakshac chri rama bhagavat-para",
    translation="Then the goddess of fortune herself appeared, lighting up every direction, like a flash of lightning.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="I bring what you don't have. I keep what you do",
    reference="CHAPTER 9, VERSE 22",
    gloss=["Yoga is getting what you lack. Kshema is holding on to it.",
           "He says both are his job, not a prize for chasing harder."],
    devanagari=["अनन्याश्चिन्तयन्तो मां ये जनाः पर्युपासते ।",
                "तेषां नित्याभियुक्तानां योगक्षेमं वहाम्यहम् ॥"],
    translit="Ananyas chintayanto mam ye janah paryupasate",
    translation="For the ones who think of me and nothing else, and who stay with it, I bring what they do not have and I keep what they already do.",
)

TURN = ["&ldquo;The poison came out of that",
        "ocean before she did.&rdquo;"]

REEL_SUB = "the poison came out first."
REEL_CLOSE = [("WHAT HAS A KID", False),
              ("ASKED YOU THAT", False),
              ("YOU COULDN'T ANSWER?", True)]
