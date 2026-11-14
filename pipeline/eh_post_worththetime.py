# -*- coding: utf-8 -*-
"""
@expandHinduism, "Apps Worth Your Screen Time". 2026-11-14.

The cover ties the series to the day's angle across the other accounts -
Avi's screen-time / iPad-kid idea, see ipadkid_content.py - without turning
the countdown into a lecture. The list stays a list.

    Build:  python3 pipeline/eh_apps.py --post eh_post_worththetime \\
                --out ./frames --work .

ORDER
Fifth legal order used of twelve. Constraints: Dharma Lock pinned at 3,
mySatsang never below 2. Spent so far:

    donthaveyet    5 Hindu Calendar  4 Gita  3 DL  2 mySatsang  1 Vignanam
    newyear        5 Vignanam  4 Hindu Calendar  3 DL  2 Gita  1 mySatsang
    whichofthese   5 Hindu Calendar  4 Gita  3 DL  2 Vignanam  1 mySatsang
    ranking        5 Vignanam  4 Gita  3 DL  2 mySatsang  1 Hindu Calendar

This one is new and puts the Gita app at the top for the first time. Seven
orders left after it - corrected from the "three left" told to Avi on
2026-11-13, which was wrong: there are twelve legal orders, not nine.

Cover photo and screenshots stay pinned by the builder, same as every post
in the series.
"""

COVER_TITLE = "Apps Worth Your Screen Time"
COVER_SUB = "all five live on my phone"

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (5, 1321271821, "Hindu Calendar",
     ["Every vrat, tithi and festival, without", "asking your mum which day it is."], 0, False, 0.0),
    (4, 1557728556, "Vignanam",
     ["Stotras and slokas in your own script.", "Nothing to sign up for."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 6444313821, "mySatsang",
     ["Satsang you can actually get to, with", "people near you."], 0, False, 0.0),
    (1, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit next to it."], 0, False, 0.0),
]

CAPTION = ("Five apps actually worth your screen time 🕉️📲 All five live on "
           "my phone. No. 1 isn't mine 🙏")
