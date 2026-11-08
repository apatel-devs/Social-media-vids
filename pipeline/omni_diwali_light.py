# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — Diwali, 2026-11-08, second post. SILENT.

Light over darkness, in the LOCK format. See
pipeline/diwali_light_content.py for the full fact check and for why the
angle is the asymmetry rather than the inner-lamp reading - @gita.talk ran
that one today and Avi's standing rule is that nothing can look copied from
his friend's account.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="THE DARK IS WINNING.",
    correction=["It has never won once.",
                "Not one single time."],
    reframe=["Light a match in a dark room.",
             "Now try it the other way."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Krishna does not fight the dark.",
         "He lights a lamp. That is all."],
        ["The oldest prayer asks the same.",
         "Lead me from dark to light."],
    ],
    closing=["It was never a fair fight.",
             "That is the good news."],
    badge="BHAGAVAD GITA 10.11",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "lt_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "lt_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_diwali_light_LOCK_SILENT.mp4")
        print("recorded")
