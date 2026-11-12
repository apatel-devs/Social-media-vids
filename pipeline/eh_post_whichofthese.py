# -*- coding: utf-8 -*-
"""
@expandHinduism countdown — "Which Of These 5 Do You Have?", 2026-11-12.

    python3 pipeline/eh_apps.py --post eh_post_whichofthese --out ./frames --work .

Cast fixed (see the note beside APPS in pipeline/eh_apps.py). The title asks
a question this time rather than making a claim: the three posts so far have
all been declarative ("actually live on my phone", "you don't have yet",
"start your year with"), and a question is the one hook that asks for a
comment instead of a scroll.

ORDER, with Dharma Lock pinned at 3 and mySatsang never below 2:
  post 1: Gita | Vignanam | DL | Calendar | mySatsang
  post 3: Calendar | Gita | DL | mySatsang | Vignanam
  post 4: Vignanam | Calendar | DL | Gita | mySatsang
  here:   Calendar | Gita | DL | Vignanam | mySatsang

HEADS UP FOR THE NEXT SESSION: the reordering trick is nearly used up. With
Dharma Lock pinned to slot 3 and mySatsang restricted to slot 1 or 2, there
are only twelve possible orders, and this is the fourth. After a couple more
the series needs something other than a reshuffle - a sixth app, a different
cover photo, or a format change - and that is a conversation to have with
Avi rather than a decision to make quietly.
"""

COVER_TITLE = "Which Of These 5 Do You Have?"
COVER_SUB = "all five of them live on my phone"

APPS = [
    (5, 1321271821, "Hindu Calendar",
     ["Tithi, muhurat, every festival date.", "I check it before I call my mom."], 4, False, 0.20),
    (4, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit right there. Costs nothing."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 1557728556, "Vignanam",
     ["Every stotra and sahasranamam you grew up", "hearing. Nine languages."], 0, False, 0.0),
    (1, 6444313821, "mySatsang",
     ["If you're Swaminarayan you already have", "this one. It is not close."], 3, False, 0.0),
]

CAPTION = (
    "Which of these five do you actually have? All five live on my phone. "
    "No. 1 isn't mine \U0001f64f\n\n"
    "#hindu #hindutok #desi #desitiktok #hinduism #bhakti #swaminarayan #gita "
    "#mandir #indianamerican"
)
