# -*- coding: utf-8 -*-
"""
@expandHinduism, cover A/B test — VARIANT B. 2026-11-24.

Avi, 2026-11-23: "From now on for expand Hindu we need 'top 5 Hindu apps'
to be bigger and then under that 'if you were called an ABCD growing up.
I want to test it both ways."

THE TEST
Variant A is eh_post_abcdkids.py, posted 11/23 17:50 ET:
    title    "Apps For Every ABCD Kid"
    subtitle "top 5, all on my phone"
Variant B is this file, posted 11/24 at the same time:
    title    "Top 5 Hindu Apps"
    subtitle "if you were called an ABCD growing up"

The difference is which line gets the size. A puts the READER in the big
type and the count underneath. B puts the generic category in the big type
and the reader underneath, which also makes the title much larger - the
cover title auto-shrinks to fit 960px on one line, so a 16-character title
renders at the full 104px where a 23-character one does not. That size
jump is most of what Avi is asking for.

EVERYTHING ELSE IS HELD CONSTANT ON PURPOSE. Same five apps, same order,
same photo, same screenshots, same caption shape. The cover is the only
variable, so whatever the numbers say is about the cover and nothing else.

WHAT THIS COSTS, SO IT IS NOT A SURPRISE
  * The two posts go out a day apart, so day-of-week and whatever else
    moves on this account are confounded with the variant. That is
    unavoidable on one account without running them weeks apart.
  * Followers who saw A will see the same five apps in the same order
    again. The covers differ, but the body is a repeat. If that matters
    more than test cleanliness, vary the order on B and accept that the
    test gets noisier - the cover is what drives the swipe, not the order.

WHAT TO COMPARE, AND WHEN
Views first, because the cover's whole job is to stop the scroll. Then
shares, which is why this format earns its slot at all. Give it 48 hours
before reading anything into it; this account's posts have taken that long
to settle. Record the result in claude/expandhinduism-countdown-format.md
and make the winner the default, per "from now on".

See pipeline/abcd_content.py for the ABCD angle and the Gita verses behind
the Dharma Lock and Omni posts on the same hook.
"""

COVER_TITLE = "Top 5 Hindu Apps"
COVER_SUB = "if you were called an ABCD growing up"
# The series default is 54px, sized for short subtitles like "top 5, all on
# my phone". This one is 37 characters, so at 54px it auto-shrinks further to
# fit 960px and ends up thin and small under a title that is now rendering at
# the full 104px. 64px gives the second line enough weight to still be read on
# a phone, which is the whole point of putting the reader's line there.
COVER_SUB_PX = 64

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
# IDENTICAL to eh_post_abcdkids.py. Do not "improve" this list - the whole
# point of the test is that it is the same.
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
