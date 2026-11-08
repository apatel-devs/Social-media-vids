# -*- coding: utf-8 -*-
"""
@dharmalockapp — Diwali, 2026-11-08.

THE ANGLE
Not the lamps, not Rama's return, not "wealth isn't money." Tonight in
Gujarati homes a brand new account book is opened in front of Lakshmi with
every page still blank - Chopda Pujan, also called Sharda Pujan - and
Saraswati and Ganesha are worshipped alongside her for it. The hook is that
emptiness: the most auspicious object in the room is the one with nothing
written in it yet. It also lands with the Gujarati audience, which the
concept log flags as the segment most likely to share.

FACT CHECK
  * Diwali 2026 is Sunday 8 November, and Chopda Pujan / Sharda Pujan falls
    on the same day - confirmed on drikpanchang.com's Sharda Puja page and
    hindutone's Bestu Varas page, which both list Diwali, Lakshmi Puja,
    Chopda Puja and Sharda Puja together on 2026-11-08.
  * Drik Panchang, verbatim: "New account books are worshipped on Sharda
    Puja," called Chopda in Gujarat, with prayers to Lakshmi, Saraswati and
    Ganesha. It also states Sharda is a name of Saraswati, goddess of
    knowledge, and that Lakshmi brings the wealth while Saraswati and Ganesha
    bring the wisdom to sustain it. That is the post's whole spine, and it is
    the source's own framing, not ours.
  * Gita 10.34 second line and Gita 4.38 both verified on shlokam.org -
    Devanagari, transliteration and translation taken from there.

  ONLY THE SECOND LINE OF 10.34 IS SHOWN, deliberately. The first line is
  "I am all-devouring Death", which is a true part of the verse and the wrong
  note for Diwali. The second line is a self-contained list, and the card
  labels it so, but anyone editing this should know the half that is missing
  rather than discover it in a comment reply.

  NOT claimed: that Bestu Varas is the next day. Drik Panchang puts Gujarati
  New Year on Tuesday 10 November 2026, not the 9th, and the gap depends on
  the panchang and the city - so the copy stays off it rather than printing a
  date that is wrong for half the audience.

  NOT reused: @gita.talk's giving angle or @soumya_aggarwal's "Dhan was never
  money" reframe. Both are wealth-isn't-money posts. This one is a ritual
  that actually happens tonight, with a verse that names Lakshmi and
  Saraswati in the same breath.
"""
CHIP = "DIWALI"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("THE BOOK THEY BLESS", False),
        ("TONIGHT HAS NOTHING", False),
        ("WRITTEN IN IT.", True)]
BODY = ["In Gujarati homes tonight a brand new account book",
        "is opened in front of Lakshmi, every page still blank.",
        "Saraswati and Ganesha are right there beside her."]
PILL = "BHAGAVAD GITA"

V1 = dict(
    source="BHAGAVAD GITA",
    title="Money and brains are named in the same breath",
    reference="CHAPTER 10, VERSE 34",
    gloss=["Krishna lists what he is. Wealth does not get a line",
           "of its own - it shares one with memory and sense."],
    devanagari=["कीर्तिः श्रीर्वाक्च नारीणां",
                "स्मृतिर्मेधा धृतिः क्षमा ॥"],
    translit="Kirtih shrir vak cha narinam smritir medha dhritih kshama",
    translation="I am fame, and wealth, and speech, and memory, and sense, and steadiness, and the will to forgive.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="Nothing washes you clean like knowing something",
    reference="CHAPTER 4, VERSE 38",
    gloss=["Lakshmi is asked for the money. Saraswati is asked",
           "for the part that decides what you do with it."],
    devanagari=["न हि ज्ञानेन सदृशं पवित्रमिह विद्यते ।",
                "तत्स्वयं योगसंसिद्धः कालेनात्मनि विन्दति ॥"],
    translit="Na hi jnanena sadrisham pavitram iha vidyate",
    translation="There is nothing in this world that makes you clean the way knowing does.",
)

TURN = ["&ldquo;Lakshmi fills the book.",
        "She does not write in it.&rdquo;"]

REEL_SUB = "the page is blank on purpose."
REEL_CLOSE = [("WHAT ARE YOU", False),
              ("PUTTING ON", False),
              ("PAGE ONE?", True)]
