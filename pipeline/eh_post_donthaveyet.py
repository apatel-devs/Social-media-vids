# -*- coding: utf-8 -*-
"""
@expandHinduism, countdown series — "5 Hindu Apps You Don't Have Yet".
Built 2026-11-09, off the analytics rather than the calendar.

    python3 pipeline/eh_apps.py --post eh_post_donthaveyet \\
        --out ./frames --work .

WHY THIS POST EXISTS
Avi asked for content that makes people watch longer and share. The 30-day
numbers say the ranked list is the only thing on any of these accounts that
has earned real shares - post one took 4, more than every Dharma Lock and
Omni post combined - and it ran a 5.5% like rate. Lists get sent to people.
So the answer to "what drives shares" was a format we already had.

The title is the one variable doing work here. "Actually live on my phone"
(post one) was a credibility hook. "You don't have yet" is a curiosity hook
pointed at the viewer, which is what gets a swipe to frame two.

CAST AND ORDER
Cast is fixed - see the note beside APPS in pipeline/eh_apps.py. Same five
apps, same cover, same screenshots, same blurbs, verbatim.

Order, with Dharma Lock pinned at 3 as always:
  post 1: 5 Gita | 4 Vignanam | 3 DL | 2 Hindu Calendar | 1 mySatsang
  post 2: 5 Hindu Calendar | 4 Vignanam | 3 DL | 2 mySatsang | 1 Gita
  here:   5 Hindu Calendar | 4 Gita | 3 DL | 2 mySatsang | 1 Vignanam

Every one of the four movable slots differs from post one, which is the post
most likely to be the last one the audience actually saw, since post two has
not published yet. mySatsang stays at 2: the content rules bar ranking it
low, because the Gujarati audience is the segment most likely to share and
that is the whole point of this post.

Vignanam takes the top slot on its own merits - 4.92, the highest rating in
the cast, and a stotra library is the least app-like thing in the list,
which makes it a better payoff frame than another calendar or lock screen.
"""

COVER_TITLE = "5 Hindu Apps You Don't Have Yet"
COVER_SUB = "all five of them live on my phone"

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (5, 1321271821, "Hindu Calendar",
     ["Tithi, muhurat, every festival date.", "I check it before I call my mom."], 4, False, 0.20),
    (4, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit right there. Costs nothing."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 6444313821, "mySatsang",
     ["If you're Swaminarayan you already have", "this one. It is not close."], 3, False, 0.0),
    (1, 1557728556, "Vignanam",
     ["Every stotra and sahasranamam you grew up", "hearing. Nine languages."], 0, False, 0.0),
]

# Caption draft. Keeps post one's hashtag set, which is the set that ran the
# 5.5% like rate and took the 4 shares.
CAPTION = (
    "Five Hindu apps you probably don't have yet. All five live on my phone. "
    "No. 1 isn't mine \U0001f64f\n\n"
    "#hindu #hindutok #desi #desitiktok #hinduism #bhakti #swaminarayan #gita "
    "#mandir #indianamerican"
)
