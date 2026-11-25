# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — "I don't know how to pray." 2026-11-24.

SILENT, as always here.

See pipeline/whattosay_content.py for the fact check, including the one
honest stretch in this angle and the line not to cross with it.

Struck line is 25 characters, inside the 26 the column fits.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="I DON'T KNOW HOW TO PRAY.",
    correction=["Neither did Arjuna.",
                "He said so out loud."],
    reframe=["The Gita is the answer",
             "to someone admitting that."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["My mind is confused, he says.",
         "Tell me plainly what is best."],
        ["Seven hundred verses come after",
         "that one sentence."],
    ],
    closing=["You are not bad at praying.",
             "You were never given the words."],
    badge="BHAGAVAD GITA 2.7",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "wts_omni_locked.png", 4.9)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_whattosay_SILENT.mp4")
        print("recorded")
