# -*- coding: utf-8 -*-
"""
@expandHinduism, "Stopped Praying To Bhagwan?". 2026-11-19.

Avi's hook, his words: "Top 5 apps if you stopped praying to Bhagwan".

WHY THE COVER SPLITS HIS LINE
The cover title is drawn as ONE line that shrinks to fit 960px and never
wraps. His full sentence is 43 characters, which shrinks to roughly 49px -
thin and small next to every other cover in the series, and close enough to
the 40px floor that a longer one would overflow and lose its tail, which is
exactly the bug that bit the Omni struck line on 2026-11-14. So the question
goes in the title and the "top 5 apps" goes in the subtitle, which is where
this series has always put the count anyway.

WHY THIS IS THE BEST COVER THE SERIES HAS HAD
Every earlier cover described the LIST ("Ranking Hindu Apps", "Apps Worth
Your Screen Time"). This one describes the READER, and asks a question they
have to answer before they can scroll. That is the rule the Dharma Lock
hooks were rewritten around on 2026-11-12 after the 30-day numbers showed
reader-first hooks beating list-first ones, and this is the first time it
has reached the countdown cover.

ORDER
Sixth of twelve legal orders. Dharma Lock pinned at 3, mySatsang never below
slot 2. Spent so far:

    donthaveyet    5 Hindu Calendar  4 Gita  3 DL  2 mySatsang  1 Vignanam
    newyear        5 Vignanam  4 Hindu Calendar  3 DL  2 Gita  1 mySatsang
    whichofthese   5 Hindu Calendar  4 Gita  3 DL  2 Vignanam  1 mySatsang
    ranking        5 Vignanam  4 Gita  3 DL  2 mySatsang  1 Hindu Calendar
    worththetime   5 Hindu Calendar  4 Vignanam  3 DL  2 mySatsang  1 Gita

This one is new, and it moves mySatsang back to the top slot, which has not
been used since the new year post. Six orders left.

    Build:  python3 pipeline/eh_apps.py --post eh_post_stoppedpraying \\
                --out ./frames --work .
"""

COVER_TITLE = "Stopped Praying To Bhagwan?"
COVER_SUB = "top 5 apps to start again"

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (5, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit next to it."], 0, False, 0.0),
    (4, 1321271821, "Hindu Calendar",
     ["Every vrat, tithi and festival, without", "asking your mum which day it is."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 1557728556, "Vignanam",
     ["Stotras and slokas in your own script.", "Nothing to sign up for."], 0, False, 0.0),
    (1, 6444313821, "mySatsang",
     ["Satsang you can actually get to, with", "people near you."], 0, False, 0.0),
]

CAPTION = ("If you stopped praying to Bhagwan, start here 🕉️📲 Five apps, all "
           "on my phone. No. 1 isn't mine 🙏")
