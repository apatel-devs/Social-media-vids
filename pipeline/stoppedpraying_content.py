# -*- coding: utf-8 -*-
"""
@dharmalockapp — "You stopped praying to Bhagwan. Arjuna asked about you."
2026-11-19.

Avi's hook for the day, carried across all four accounts. On the countdown
it is a cover question (eh_post_stoppedpraying.py); here it gets the verses.

WHY ARJUNA IS IN LINE ONE AND ABHIMANYU WAS A MISTAKE
A proper noun in the hook killed the Abhimanyu post (158 views, the worst
Dharma Lock post of the month) because the audience could not place him and
line one became homework. Arjuna is different: everyone in this audience
knows who he is, the reader is still the subject of the sentence, and the
claim is literally true - 6.37-39 is Arjuna asking what becomes of someone
who had faith, could not hold the practice, and fell away. That is the
reader, asked about by name, two thousand years early. Keep that test for
any future hook with a name in it: not "do I know this person" but "does
the audience, without being told".

WHY THIS IS THE RIGHT ANSWER TO GIVE THEM
The niche default is to tell the lapsed person they have fallen behind.
Krishna's actual answer to that exact question is the opposite, and it is
the whole reason this hook works: nothing is destroyed, and you resume with
what you already had rather than starting from zero.

FACT CHECK
  * Arjuna's question verified at gita-glossary.pages.dev/verses/06/06-37-47
    - 6.37-39, the person of faith whose mind wanders off the path and who
    does not reach perfection; Arjuna asks what happens to him.
  * Gita 6.40 verified at asitis.com/6/40.html. Devanagari and
    transliteration from there. "No destruction here or hereafter... one who
    does good never comes to a bad end."
  * Gita 6.43 verified at asitis.com/6/43.html. Devanagari and
    transliteration from there - he regains the understanding of his former
    life and strives again toward perfection.

  CAREFUL, AND DELIBERATELY NOT SPELLED OUT: 6.43's own frame is REBIRTH -
  "paurva-dehikam" is the previous BODY, and the verse describes the yogi
  taking a new birth. The copy says "you pick up where you stopped", which
  is what the verse states, and it does NOT say or imply this is about
  getting back to it next week. Do not let a later rewrite turn this into
  "Krishna says you can start again on Monday" - that is a different claim
  and the comments on this account would catch it.

  NOT CLAIMED: that stopping does not matter. 6.40 says the one who does
  good is not destroyed; it does not say the path completes itself.
"""
CHIP = "BHAGAVAD GITA"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("YOU STOPPED PRAYING", False),
        ("TO BHAGWAN.", False),
        ("ARJUNA ASKED ABOUT YOU.", True)]
BODY = ["He asked Krishna what happens to the one who had",
        "faith, could not hold it, and drifted off. Krishna's",
        "answer was not a warning."]
PILL = "CHAPTER 6"

V1 = dict(
    source="BHAGAVAD GITA",
    title="Nothing you did is destroyed",
    reference="CHAPTER 6, VERSE 40",
    gloss=["Arjuna asks about the one who fell away. Krishna",
           "says he is not lost, here or anywhere else."],
    devanagari=["पार्थ नैवेह नामुत्र विनाशस्तस्य विद्यते ।",
                "न हि कल्याणकृत्कश्चिद् दुर्गतिं तात गच्छति ॥"],
    translit="Na hi kalyana-krit kashchid durgatim tata gacchati",
    translation="Nothing he did is destroyed, here or hereafter. Nobody who does good ever comes to a bad end, my friend.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="You pick it up where you put it down",
    reference="CHAPTER 6, VERSE 43",
    gloss=["He does not go back to the beginning. What he",
           "already understood comes back to him."],
    devanagari=["तत्र तं बुद्धिसंयोगं लभते पौर्वदेहिकम् ।",
                "यतते च ततो भूयः संसिद्धौ कुरुनन्दन ॥"],
    translit="Tatra tam buddhi-samyogam labhate paurva-dehikam",
    translation="There he regains the understanding he already had, and from there he strives again.",
)

TURN = ["&ldquo;You are not starting from zero.",
        "You are starting from where you stopped.&rdquo;"]

REEL_SUB = "Arjuna asked about you."
REEL_CLOSE = [("YOU ARE NOT BEHIND.", False),
              ("YOU ARE JUST", False),
              ("NOT STARTED AGAIN YET.", True)]
