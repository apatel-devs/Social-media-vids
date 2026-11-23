# -*- coding: utf-8 -*-
"""
@dharmalockapp — "They called you ABCD." 2026-11-23.

THE VOICE CHANGED HERE. READ THIS BEFORE WRITING THE NEXT ONE.
Avi, 2026-11-23: "how about you sound more like someone who is a young adult,
don't be confusing, be clear short to the point but catch their attention.
'Do they call you ABCD in school', 'feel bad for making fun of that fob'."

So the register is no longer a teacher explaining scripture. It is someone
the reader's own age naming something they lived through. Concretely:

  * Shorter. The body is three lines and they are short lines. If a sentence
    needs a comma to survive, cut it in two.
  * Name the real thing. ABCD. Fob. Gujarati school. Aunties. The specific
    word the reader actually heard is the hook; a general one is not.
  * No scripture in the hook, ever. It is the payoff. This was already the
    rule from 11/12; it matters more now.
  * Still forgiving at the turn. The accusation opens, the verse lets them
    off. That arc is what separates this from the scolding every other
    account in the niche does.

WHY ABCD AND NOT THE FOB LINE FIRST
Avi offered both. ABCD is the better opener for the first post in this voice:
everyone in the audience has heard it, it is said ABOUT them rather than BY
them, and it carries no slur. "Feel bad for making fun of that fob" is a
stronger, riskier post - the reader has to admit to something - and it is
worth doing, but it goes better once the account has established it is on
their side. Keep it for a follow-up.

THE PAYOFF IS ALMOST TOO GOOD A FIT
Gita 4.2 is literally about a chain of transmission breaking over time. For
a diaspora audience that is not an analogy, it is a description: it got
handed down for generations and then stopped somewhere between there and
here. And 4.3 is Krishna starting it again from the top, with no penance
required. Nobody has to be told they failed.

FACT CHECK
  * Gita 4.2 verified at asitis.com/4/2.html. Devanagari and transliteration
    from there. "Evam parampara-praptam... sa kaleneha mahata yogo nastah" -
    handed down through the succession, and over long time that chain broke,
    so the teaching appears lost.
  * Gita 4.3 verified at vidhyamitra.com/bhagavad-gita/4/3 for the
    Devanagari, cross-checked against bhagavad-gita.us/bhagavad-gita-4-3 for
    the transliteration and sense. "That same ancient yoga I declare to you
    today" - he restates it to Arjuna as devotee and friend.

  NOT CLAIMED: that the Gita is about immigration or the diaspora. 4.2 is
  about the parampara, the teacher-to-student succession, and Krishna's
  point is about the knowledge itself, not about anybody's family. The copy
  says the chain broke, which is what the verse says, and lets the reader
  make it about their own house. Do not let a rewrite turn this into
  "Krishna predicted the diaspora".

  NOT CLAIMED: that nobody is at fault, or that anybody is. The copy does
  not blame parents, grandparents, or the reader. "It stopped somewhere" is
  deliberately unattributed.
"""
CHIP = "BHAGAVAD GITA"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("THEY CALLED YOU ABCD.", False),
        ("AMERICAN BORN", False),
        ("CONFUSED DESI.", True)]
BODY = ["You were never confused. The handoff just stopped.",
        "It got passed down for a thousand years, and",
        "somewhere between there and here it skipped you."]
PILL = "CHAPTER 4"

V1 = dict(
    source="BHAGAVAD GITA",
    title="The chain broke. Krishna says so himself",
    reference="CHAPTER 4, VERSE 2",
    gloss=["Handed down teacher to student, generation to",
           "generation. Then over time it was lost."],
    devanagari=["एवं परम्पराप्राप्तमिमं राजर्षयो विदुः ।",
                "स कालेनेह महता योगो नष्टः परन्तप ॥"],
    translit="Sa kaleneha mahata yogo nashtah parantapa",
    translation="This was handed down in succession, and over a long time that chain broke, so the teaching seemed lost.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="So he says it again, from the top",
    reference="CHAPTER 4, VERSE 3",
    gloss=["No test. No catching up. He just tells it again",
           "to the person sitting in front of him."],
    devanagari=["स एवायं मया तेऽद्य योगः प्रोक्तः पुरातनः ।",
                "भक्तोऽसि मे सखा चेति रहस्यं ह्येतदुत्तमम् ॥"],
    translit="Sa evayam maya te 'dya yogah proktah puratanah",
    translation="That same ancient teaching I am telling you today, because you are my devotee and my friend.",
)

TURN = ["&ldquo;You are not a bad Hindu.",
        "You are an interrupted one.&rdquo;"]

REEL_SUB = "nobody taught you. that's it."
REEL_CLOSE = [("THE CHAIN BROKE", False),
              ("BEFORE YOU GOT HERE.", False),
              ("IT RESTARTS WITH YOU.", True)]
