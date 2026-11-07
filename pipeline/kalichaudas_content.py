# -*- coding: utf-8 -*-
"""
@dharmalockapp — Kali Chaudas, 2026-11-07. Diwali is tomorrow.

THE ANGLE
Kali Chaudas is the night before Diwali: the "dark fourteenth". Tradition
holds the bad things come closest tonight, so the puja is to Hanuman - the
protector - and Lakshmi is welcomed tomorrow. The hook is that ordering:
tonight the devotee gets the prayer, before the deity does. It also carries
across from the @amysharma_dharma post that went out this morning, which is
Hanuman-themed, so the accounts line up for the day.

FACT CHECK
  * Kali Chaudas 2026 is the night of Saturday 7 November, and the same
    Chaturdashi is Diwali Hanuman Puja - verified at
    drikpanchang.com/diwali/hanuman-puja and hindutone's Kali Chaudas page.
    Kali Chaudas is the night observance; Narak Chaturdashi is the morning
    one, with the oil bath and the Krishna/Narakasura story.
  * Hanuman is worshipped tonight as protection against fear and evil
    spirits. That is the stated reason, not a flourish.
  * Hanuman Chalisa verse 24 is the couplet people actually recite for this:
    "bhoot pisaach nikat nahin aavai, Mahabir jab naam sunavai". Confirmed on
    shlokam.org's Hanuman Chalisa page, including the "स" spelling of
    pisaach. Tulsidas, 16th century, long out of copyright; one couplet.
  * Gita 18.66 Devanagari and sense verified at shlokam.org/gita/gita-18-66.

  NOT claimed: that Hanuman was born on this Chaturdashi. Some traditions
  hold that and others place Hanuman Jayanti in Chaitra; the copy stays off
  it rather than picking a side on a disputed date.
"""
CHIP = "KALI CHAUDAS"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("TONIGHT YOU PRAY TO", False),
        ("THE DEVOTEE BEFORE", False),
        ("YOU PRAY TO GOD.", True)]
BODY = ["Kali Chaudas is the dark fourteenth, the night people",
        "say the bad things come closest. So the puja tonight",
        "is to Hanuman. Lakshmi gets welcomed tomorrow."]
PILL = "HANUMAN CHALISA"

V1 = dict(
    source="HANUMAN CHALISA",
    title="Nothing comes near when his name is said",
    reference="VERSE 24",
    gloss=["This is the couplet people recite tonight, and it is",
           "the whole reason the puja happens after dark."],
    devanagari=["भूत पिसाच निकट नहिं आवै ।",
                "महाबीर जब नाम सुनावै ॥"],
    translit="Bhoot pisaach nikat nahin aavai, Mahabir jab naam sunavai",
    translation="Ghosts and spirits do not come near, when the name of Mahavir is spoken.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="Come to me, and stop being afraid",
    reference="CHAPTER 18, VERSE 66",
    gloss=["The last thing he says to Arjuna. Not a ritual and not",
           "a rule. Come here, and put the fear down."],
    devanagari=["सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज ।",
                "अहं त्वा सर्वपापेभ्यो मोक्षयिष्यामि मा शुच: ॥"],
    translit="Sarva-dharman parityajya mam ekam sharanam vraja",
    translation="Set all of it down and come to me alone. I will free you from everything you have done wrong. Do not grieve.",
)

TURN = ["&ldquo;Nobody calls the guard",
        "on an easy night.&rdquo;"]

REEL_SUB = "the night you call the guard."
REEL_CLOSE = [("WHAT ARE YOU ASKING", False),
              ("HIM TO KEEP OUT", False),
              ("TONIGHT?", True)]
