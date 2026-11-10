# -*- coding: utf-8 -*-
"""
@expandHinduism countdown — "5 Apps To Start Your Year With", 2026-11-10.
Saal Mubarak / Vikram Samvat 2083.

    python3 pipeline/eh_apps.py --post eh_post_newyear --out ./frames --work .

Cast fixed (see the note beside APPS in pipeline/eh_apps.py). Only the title
and the ranking order move.

  post 1: 5 Gita | 4 Vignanam | 3 DL | 2 Calendar | 1 mySatsang
  post 3: 5 Calendar | 4 Gita | 3 DL | 2 mySatsang | 1 Vignanam
  here:   5 Vignanam | 4 Calendar | 3 DL | 2 Gita | 1 mySatsang

mySatsang takes the top slot for a new-year post on purpose: the Gujarati
audience is the one actually marking Bestu Varas today, and it is the segment
the content rules protect because it is the most likely to share.

No date is printed - Bestu Varas splits across the date line this year. See
pipeline/saal_mubarak_content.py for that fact check.
"""

COVER_TITLE = "5 Apps To Start Your Year With"
COVER_SUB = "saal mubarak, all five are on my phone"

APPS = [
    (5, 1557728556, "Vignanam",
     ["Every stotra and sahasranamam you grew up", "hearing. Nine languages."], 0, False, 0.0),
    (4, 1321271821, "Hindu Calendar",
     ["Tithi, muhurat, every festival date.", "I check it before I call my mom."], 4, False, 0.20),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit right there. Costs nothing."], 0, False, 0.0),
    (1, 6444313821, "mySatsang",
     ["If you're Swaminarayan you already have", "this one. It is not close."], 3, False, 0.0),
]

CAPTION = (
    "Saal Mubarak \U0001f64f Five apps to start the new year with. "
    "All five live on my phone. No. 1 isn't mine\n\n"
    "#saalmubarak #bestuvaras #gujarati #hindu #hindutok #desi #desitiktok "
    "#hinduism #swaminarayan #indianamerican"
)
