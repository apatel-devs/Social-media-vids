# -*- coding: utf-8 -*-
"""
@expandHinduism, "Apps For Every ABCD Kid". 2026-11-23.

Carries the day's angle onto the countdown cover - see abcd_content.py for
the voice change Avi asked for and for the verses behind the Dharma Lock
and Omni posts.

    Build:  python3 pipeline/eh_apps.py --post eh_post_abcdkids \\
                --out ./frames --work .

ORDER
First post under the rule Avi set on 2026-11-20: "Switch the order any of
the apps except dharmalock, cover and cta." Dharma Lock stays at 3; the
other four are now free, which takes the legal orders from 12 to 24.

Spent so far (7 before this one):

    donthaveyet    5 Hindu Calendar  4 Gita  3 DL  2 mySatsang  1 Vignanam
    newyear        5 Vignanam  4 Hindu Calendar  3 DL  2 Gita  1 mySatsang
    whichofthese   5 Hindu Calendar  4 Gita  3 DL  2 Vignanam  1 mySatsang
    ranking        5 Vignanam  4 Gita  3 DL  2 mySatsang  1 Hindu Calendar
    worththetime   5 Hindu Calendar  4 Vignanam  3 DL  2 mySatsang  1 Gita
    stoppedpraying 5 Gita  4 Hindu Calendar  3 DL  2 Vignanam  1 mySatsang
    stillwaiting   5 Gita  4 Vignanam  3 DL  2 mySatsang  1 Hindu Calendar

This one puts mySatsang at 4, which the old rule forbade. It is a
deliberate middle step rather than jumping straight to mySatsang at 5: the
reason the old rule existed was that a low placement could cost the
Gujarati audience, who are the segment most likely to share, and shares are
what this format is for. Worth watching this post's share count before
putting mySatsang last.
"""

COVER_TITLE = "Apps For Every ABCD Kid"
COVER_SUB = "top 5, all on my phone"

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (5, 1557728556, "Vignanam",
     ["Stotras and slokas in your own script.", "Nothing to sign up for."], 0, False, 0.0),
    (4, 6444313821, "mySatsang",
     ["Satsang you can actually get to, with", "people near you."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit next to it."], 0, False, 0.0),
    (1, 1321271821, "Hindu Calendar",
     ["Every vrat, tithi and festival, without", "asking your mum which day it is."], 0, False, 0.0),
]

CAPTION = ("For everyone who got called ABCD 🕉️📲 Five apps, all on my phone. "
           "No. 1 isn't mine 🙏")
