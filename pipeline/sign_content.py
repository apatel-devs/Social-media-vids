# -*- coding: utf-8 -*-
"""
@dharmalockapp — "You asked for a sign. You ignored the last three."
2026-11-20.

WHY THIS AND NOT THE POST AVI SENT
Avi attached a @gita.talk post this morning - Duryodhana struck through,
"for everyone still explaining themselves to someone who's already decided"
- which is their best performing one yet (172 likes). He sent it without an
instruction. The format is the same struck-line mechanic Omni already uses,
so that part is ours to use freely, but the CLAIM is theirs and the standing
rule is that nothing can let his friend say he copied him. So this takes the
register and nothing else: different character, different subject, and
deliberately not about being unheard by another person, which is the whole
substance of theirs.

THE HOOK
Reader in line one, per the rule the 30-day numbers forced on 2026-11-12.
It is also the first Dharma Lock hook that is funny rather than severe, and
the joke is on a habit the audience will recognise instantly: waiting for a
dramatic sign while ignoring the quiet ones. That lands the app without a
lecture - you do not need a bigger sign, you need the thing that makes you
show up.

FACT CHECK
  * Gita 10.41 verified at shlokam.org/bhagavad-gita/10-41. Devanagari and
    IAST from there. Whatever is splendid, beautiful or powerful springs
    from a fragment of his radiance.
  * Gita 9.26 verified at shlokam.org/bhagavad-gita/9-26/. Devanagari and
    IAST from there. A leaf, a flower, a fruit, water - offered with
    devotion, he accepts it.

  NOT CLAIMED: that any specific event in the reader's life was a sign from
  Bhagwan. 10.41 says what is splendid springs from his radiance; it does
  not license telling someone their missed call was a divine message. The
  copy stays on what the verse says and lets the reader do the applying.

  NOT CLAIMED: that signs are owed, or that failing to notice one is a sin.
  The turn is gentle on purpose - the point of 9.26 here is that the bar for
  starting is a leaf and some water, not a revelation.
"""
CHIP = "BHAGAVAD GITA"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
# Every shipped line 3 has been 23 characters or fewer - keep it that way.
HEAD = [("YOU ASKED FOR A SIGN.", False),
        ("YOU IGNORED", False),
        ("THE LAST THREE.", True)]
BODY = ["Not the big one you are waiting for. The small ones.",
        "The thought you had and did not act on. The person who",
        "said the exact thing you needed to hear."]
PILL = "CHAPTER 10"

V1 = dict(
    source="BHAGAVAD GITA",
    title="Anything that stopped you came from him",
    reference="CHAPTER 10, VERSE 41",
    gloss=["Whatever is beautiful or strong or stops you in",
           "your tracks - he says that is a piece of him."],
    devanagari=["यद्यद्विभूतिमत्सत्त्वं श्रीमदूर्जितमेव वा ।",
                "तत्तदेवावगच्छ त्वं मम तेजोंऽशसम्भवम् ॥"],
    translit="Yad yad vibhutimat sattvam shrimad urjitam eva va",
    translation="Whatever is glorious, beautiful or powerful, know that it springs from a spark of my splendour.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="He will take a leaf and some water",
    reference="CHAPTER 9, VERSE 26",
    gloss=["You are not waiting for a big enough moment.",
           "He already said what the bar is."],
    devanagari=["पत्रं पुष्पं फलं तोयं यो मे भक्त्या प्रयच्छति ।",
                "तदहं भक्त्युपहृतमश्नामि प्रयतात्मनः ॥"],
    translit="Patram pushpam phalam toyam yo me bhaktya prayacchati",
    translation="A leaf, a flower, a fruit, water. Offered to me with love, I take it.",
)

TURN = ["&ldquo;You are not waiting for a sign.",
        "You are waiting to feel ready.&rdquo;"]

REEL_SUB = "all three of them."
REEL_CLOSE = [("YOU DON'T NEED", False),
              ("A BIGGER SIGN.", False),
              ("YOU NEED TO START.", True)]
