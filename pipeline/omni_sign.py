# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — "I never got a sign." 2026-11-20.

SILENT, as normal for this account.

See pipeline/sign_content.py for the fact check, and for why this does not
touch the @gita.talk post Avi sent this morning: the struck-line mechanic is
the account's own, the Duryodhana claim is his friend's.

Struck line is 19 characters, inside the 26 the column fits. omni_kit
measures this now and refuses to render an overlong one.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="I NEVER GOT A SIGN.",
    correction=["You got three.",
                "You were busy."],
    reframe=["He does not send fireworks.",
             "He sends small things."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Whatever stops you in your tracks,",
         "he says that is a piece of him."],
        ["And the bar for starting is a leaf",
         "and some water. That is all."],
    ],
    closing=["You are not waiting for a sign.",
             "You are waiting to feel ready."],
    badge="BHAGAVAD GITA 10.41",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "sg_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "sg_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_sign_SILENT.mp4")
        print("recorded")
