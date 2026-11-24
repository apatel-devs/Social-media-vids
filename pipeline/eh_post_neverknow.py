# -*- coding: utf-8 -*-
"""
@expandHinduism, "Top 5 Hindu Apps / if you never know what to pray".
2026-11-24. FIRST POST IN THE NEW COVER LAYOUT.

Avi, 2026-11-23: "we need 'top 5 Hindu apps' to be bigger and then under
that 'if you were called an ABCD growing up'", and on 11/24: "New test
layout for expand." So the layout proven out in eh_post_abcdkids_b.py is
now the standing shape:

    TITLE     the generic category line, short, so it renders at the full
              104px. The cover title never wraps and shrinks to fit 960px,
              so LENGTH IS SIZE - "Top 5 Hindu Apps" at 16 characters is
              the biggest type this cover can carry.
    SUBTITLE  the reader's line, which may now wrap to two lines (added to
              eh_apps.py on 11/23 for exactly this).

Covers through 11/18 described the list. From 11/19 they addressed the
reader as the title. From here the title is fixed-ish and the READER LINE
IS THE VARIABLE - that is the thing to write well each day.

TODAY'S READER LINE
"if you never know what to pray" - the quiet version of the problem this
whole category solves, and it pairs with the Amy post running the same
day about the app matching a mantra to your mood.

ORDER
Ninth of twenty-four. Dharma Lock pinned at 3; the other four free since
11/20. Spent so far:

    donthaveyet    5 Calendar  4 Gita  3 DL  2 mySatsang  1 Vignanam
    newyear        5 Vignanam  4 Calendar  3 DL  2 Gita  1 mySatsang
    whichofthese   5 Calendar  4 Gita  3 DL  2 Vignanam  1 mySatsang
    ranking        5 Vignanam  4 Gita  3 DL  2 mySatsang  1 Calendar
    worththetime   5 Calendar  4 Vignanam  3 DL  2 mySatsang  1 Gita
    stoppedpraying 5 Gita  4 Calendar  3 DL  2 Vignanam  1 mySatsang
    stillwaiting   5 Gita  4 Vignanam  3 DL  2 mySatsang  1 Calendar
    abcdkids       5 Vignanam  4 mySatsang  3 DL  2 Gita  1 Calendar

This one is new and puts the Gita app at 1 with mySatsang at 4 again.
"""

COVER_TITLE = "Top 5 Hindu Apps"
COVER_SUB = "if you never know what to pray"
COVER_SUB_PX = 64

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (5, 1321271821, "Hindu Calendar",
     ["Every vrat, tithi and festival, without", "asking your mum which day it is."], 0, False, 0.0),
    (4, 6444313821, "mySatsang",
     ["Satsang you can actually get to, with", "people near you."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray, and picks", "your mantra from how you feel."], 0, True, 0.0),
    (2, 1557728556, "Vignanam",
     ["Stotras and slokas in your own script.", "Nothing to sign up for."], 0, False, 0.0),
    (1, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit next to it."], 0, False, 0.0),
]

CAPTION = ("If you never know what to pray 🕉️📲 Five apps, all on my phone. "
           "No. 1 isn't mine 🙏")
