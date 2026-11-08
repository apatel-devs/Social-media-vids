# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — Diwali, 2026-11-08. SILENT.

Same night, same ritual, in the LOCK format's plainer register. See
pipeline/diwali_content.py for the full fact check: Chopda Pujan / Sharda
Pujan falls on Diwali itself, new account books are worshipped, and Lakshmi,
Saraswati and Ganesha are worshipped together - Lakshmi for the wealth,
Saraswati and Ganesha for the wisdom to keep it.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="TONIGHT IS LAKSHMI'S NIGHT.",
    correction=["She is not in the room alone.",
                "Saraswati is right there."],
    reframe=["One of them brings it.",
             "The other decides if you keep it."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["The book they bless tonight has",
         "nothing written in it yet."],
        ["Krishna names wealth and sense",
         "in one line. Both, or neither."],
    ],
    closing=["Lakshmi fills the book.",
             "She does not write in it."],
    badge="BHAGAVAD GITA 10.34",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "dw_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "dw_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_diwali_LOCK_SILENT.mp4")
        print("recorded")
