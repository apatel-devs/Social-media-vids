# -*- coding: utf-8 -*-
"""
@expandHinduism, post 2 of the countdown series — "5 Ways To Be A Better Hindu".
Planned 2026-11-08 02:20 ET, from Avi's queued topic list.

    python3 pipeline/eh_apps.py --post eh_post_betterhindu \\
        --out ./frames --work .

HOW THIS POST DIFFERS FROM POST ONE — and it is only two things.
Avi, 2026-11-08, on what a new post in this series changes: the ranking order
and the title. Not the apps, not the cover, not the screenshots, and not the
blurbs. So every blurb below is post one's copy, verbatim. If you find yourself
rewriting one, you have left the brief.

THE TITLE SAYS FIVE, NOT SIX
Avi's queued line reads "6 ways to be a better Hindu". The cast is five apps
and the cast is now fixed, so six would mean adding an app, which is the one
thing the cast rule forbids. Five it is. Flagged to him on 11/08; change it
back only if he wants a sixth app, which reopens the cast.

THE REORDER, AND WHY THIS ORDER
Post one ran 5 Gita · 4 Vignanam · 3 Dharma Lock · 2 Hindu Calendar · 1
mySatsang. Every slot but Dharma Lock moves here, so it reads as a different
post rather than a near-repeat.

  * Dharma Lock stays at 3. Standing rule, never 1.
  * The Gita takes 1. Under this title the countdown builds to a "way", and
    "read the Gita" is the one nobody argues with - it is also the least
    sect-specific thing in the list, which matters on a title this broad.
  * mySatsang moves to 2, not lower. The content rule warns that ranking it
    low burns the Gujarati audience, which is the segment most likely to
    share. Second is a move, not a demotion.
  * Hindu Calendar takes 5 and Vignanam 4, so the list opens on the most
    everyday habit and works inward.

rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
         fraction to crop off the top of the screenshot)
Screenshot indices and crops are post one's, unchanged, with the reasons in
pipeline/eh_apps.py beside the cast.
"""

COVER_TITLE = "5 Ways To Be A Better Hindu"
COVER_SUB = "five apps, five habits, one phone"

APPS = [
    (5, 1321271821, "Hindu Calendar",
     ["Tithi, muhurat, every festival date.", "I check it before I call my mom."], 4, False, 0.20),
    (4, 1557728556, "Vignanam",
     ["Every stotra and sahasranamam you grew up", "hearing. Nine languages."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 6444313821, "mySatsang",
     ["If you're Swaminarayan you already have", "this one. It is not close."], 3, False, 0.0),
    (1, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit right there. Costs nothing."], 0, False, 0.0),
]

# Caption draft for Avi to approve. Keeps post one's hashtag set, since the
# account is three posts old and the tags have not been tested against
# anything yet.
CAPTION = (
    "Five ways to be a better Hindu, and five apps that do the work for you. "
    "No. 1 isn't mine \U0001f64f\n\n"
    "#hindu #hindutok #desi #desitiktok #hinduism #bhakti #swaminarayan #gita "
    "#mandir #indianamerican"
)
