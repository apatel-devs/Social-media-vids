# -*- coding: utf-8 -*-
"""
@dharmalockapp — Saal Mubarak / Bestu Varas, Vikram Samvat 2083. 2026-11-10.

THE HOOK
Avi's brief: a new year post about accomplishing goals, with a hook that is
relatable but pulls the viewer in. His own sketch was a struck-through "I
will accomplish nothing" corrected into resolutions. That shape lives on the
Omni cut (pipeline/omni_saal_mubarak.py). Here it is pointed at the one
object every single viewer actually has: the resolution list still sitting in
their notes app from last year.

Relatable, slightly uncomfortable, and true - which is what makes someone
stop. The turn is that the list was never the hard part.

FACT CHECK
  * Saal Mubarak / Nutan Varshabhinandan is the Gujarati New Year greeting,
    and the year beginning is Vikram Samvat 2083 - confirmed on hindutone's
    Bestu Varas 2026 page.
  * Gita 6.25 verified at shlokam.org/gita/gita-6-25.htm.
  * Gita 3.35 verified at shlokam.org/gita/gita-3-35.htm.

  NO DATE IS PRINTED, deliberately. Bestu Varas splits across the date line
  this year: hindutone's USA page puts it Monday 9 November, Drik Panchang
  for New Delhi puts it Tuesday 10 November, because the deciding Kartik
  Shukla Pratipada morning falls on different civil days. Saying "today"
  would be wrong for half the audience, so the copy greets the year without
  dating it.
"""
CHIP = "SAAL MUBARAK"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
# HOOK REPLACED 2026-11-10. Avi: "Why can you also use the same caption for
# dharma lock? New year new me?" He was right and the first version had it
# backwards. "New year, new me" is the phrase every viewer already knows, and
# it went onto Omni only because the struck-line mechanic is native to that
# format - which put the strongest hook on the weakest account. Omni runs
# 0-1% like rates; this account runs about 4%. The carousel carries the line
# without needing a strikethrough, and the notes-app detail moves down into
# the body where it still does its work.
HEAD = [("NEW YEAR, NEW ME.", False),
        ("YOU SAID THAT", False),
        ("LAST YEAR TOO.", True)]
BODY = ["Saal Mubarak. The list is still in your notes app.",
        "Two thousand and eighty three new years, and not",
        "one was ever won by the list written on day one."]
PILL = "BHAGAVAD GITA"

V1 = dict(
    source="BHAGAVAD GITA",
    title="Little by little. Not all of it today",
    reference="CHAPTER 6, VERSE 25",
    gloss=["Shanaih shanaih. Krishna's pace for changing",
           "anything is slowly, held by a mind that stays."],
    devanagari=["शनैः शनैरुपरमेद् बुद्ध्या धृतिगृहीतया ।",
                "आत्मसंस्थं मनः कृत्वा न किञ्चिदपि चिन्तयेत् ॥"],
    translit="Shanaih shanair uparamed buddhya dhriti-grihitaya",
    translation="Little by little come to quiet, with the understanding held firm. Settle the mind in the self and think of nothing else.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="Your own work done badly beats someone else's",
    reference="CHAPTER 3, VERSE 35",
    gloss=["Half of that list was never yours. You copied it",
           "off somebody whose life is not your life."],
    devanagari=["श्रेयान्स्वधर्मो विगुणः परधर्मात्स्वनुष्ठितात् ।",
                "स्वधर्मे निधनं श्रेयः परधर्मो भयावहः ॥"],
    translit="Shreyan sva-dharmo vigunah para-dharmat svanushthitat",
    translation="Your own work done imperfectly is better than another's done well. Another person's road is a dangerous place to live.",
)

TURN = ["&ldquo;The list was never the problem.",
        "Day forty was.&rdquo;"]

REEL_SUB = "the list was never the problem."
REEL_CLOSE = [("WHAT ARE YOU", False),
              ("ACTUALLY DOING", False),
              ("TOMORROW?", True)]
