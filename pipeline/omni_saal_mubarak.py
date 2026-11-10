# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — Saal Mubarak, Vikram Samvat 2083. 2026-11-10.

Carries Avi's own sketch for this post: a struck-through "new year, new me"
corrected by the fact that the note is still saved from last time. See
pipeline/saal_mubarak_content.py for the fact check, including why no date
is printed.

Audio: Avi asked for hype audio on 2026-11-09 and for all of today's posts to
go out, so this ships with a bed track and through Post Bridge rather than
silent. The account's standing default is still silent - see
pipeline/omni_abhimanyu.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="NEW YEAR, NEW ME.",
    correction=["You wrote that last year.",
                "The note is still saved."],
    reframe=["Saal Mubarak.",
             "Try a smaller promise."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Krishna's pace for change is",
         "shanaih shanaih. Little by little."],
        ["And your own work done badly",
         "beats somebody else's done well."],
    ],
    closing=["The list was never the problem.",
             "Day forty was."],
    badge="BHAGAVAD GITA 6.25",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "sm_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "sm_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_saalmubarak_SILENT.mp4")
        print("recorded")
