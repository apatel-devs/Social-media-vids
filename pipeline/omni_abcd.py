# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — "You're a bad Hindu." 2026-11-23.

SILENT, as always here. Avi adds the trending sound in the app.

See pipeline/abcd_content.py for the fact check AND for the voice change
Avi asked for on 2026-11-23 - young adult, short, clear, name the real
thing. That applies to this account too.

Struck line is 19 characters, inside the 26 the column fits; omni_kit
measures it and refuses to render an overlong one.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="YOU'RE A BAD HINDU.",
    correction=["You're an interrupted one.",
                "The chain broke before you."],
    reframe=["Krishna says it broke.",
             "Then he says it again anyway."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Handed down teacher to student for",
         "generations. Then over time, lost."],
        ["No test to get back in. He just tells",
         "it again to whoever is sitting there."],
    ],
    closing=["Nobody taught you.",
             "That is the whole problem."],
    badge="BHAGAVAD GITA 4.2",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "ab2_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "ab2_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_abcd_SILENT.mp4")
        print("recorded")
