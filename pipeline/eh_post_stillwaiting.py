# -*- coding: utf-8 -*-
"""
@expandHinduism, "Still Waiting For A Sign?". 2026-11-20.

Carries the day's hook onto the countdown cover - see sign_content.py - the
same way "Stopped Praying To Bhagwan?" did yesterday. Second cover in a row
that asks the reader a question instead of describing the list, which is now
the default for this series rather than an experiment.

    Build:  python3 pipeline/eh_apps.py --post eh_post_stillwaiting \\
                --out ./frames --work .

ORDER
Seventh of twelve legal orders. Dharma Lock pinned at 3, mySatsang never
below slot 2. Spent so far:

    donthaveyet    5 Hindu Calendar  4 Gita  3 DL  2 mySatsang  1 Vignanam
    newyear        5 Vignanam  4 Hindu Calendar  3 DL  2 Gita  1 mySatsang
    whichofthese   5 Hindu Calendar  4 Gita  3 DL  2 Vignanam  1 mySatsang
    ranking        5 Vignanam  4 Gita  3 DL  2 mySatsang  1 Hindu Calendar
    worththetime   5 Hindu Calendar  4 Vignanam  3 DL  2 mySatsang  1 Gita
    stoppedpraying 5 Gita  4 Hindu Calendar  3 DL  2 Vignanam  1 mySatsang

Five orders left. At roughly one a day that is a week, so the new cast
member or the new mechanic is now the thing to decide, not a thing to
mention again later.
"""

COVER_TITLE = "Still Waiting For A Sign?"
COVER_SUB = "top 5 apps, this is your sign"

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (5, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit next to it."], 0, False, 0.0),
    (4, 1557728556, "Vignanam",
     ["Stotras and slokas in your own script.", "Nothing to sign up for."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 6444313821, "mySatsang",
     ["Satsang you can actually get to, with", "people near you."], 0, False, 0.0),
    (1, 1321271821, "Hindu Calendar",
     ["Every vrat, tithi and festival, without", "asking your mum which day it is."], 0, False, 0.0),
]

CAPTION = ("This is your sign 🕉️📲 Five apps, all on my phone. "
           "No. 1 isn't mine 🙏")
