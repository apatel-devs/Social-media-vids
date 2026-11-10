# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — Abhimanyu and the half-lesson. 2026-11-09.

NOT SILENT, FOR ONCE. Avi, 2026-11-09: "Post to the accounts this time for me.
Use hype audio." This account normally ships silent so he can add a trending
sound in the TikTok app, and normally does not go through Post Bridge at all.
Both of those are suspended for this post at his explicit request - note the
"this time". Do not treat this file as the new default.

See pipeline/abhimanyu_content.py for the full fact check, and for why the
angle is the half-lesson rather than the betrayal reading @gita.talk ran.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="ABHIMANYU WAS OUTNUMBERED.",
    correction=["He was under-taught.",
                "Not the same thing."],
    reframe=["He knew the way in.",
             "Nobody gave him the way out."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Krishna does not say try harder.",
         "He says repeat it until it holds."],
        ["And nothing you start on this",
         "road is ever wasted."],
    ],
    closing=["The way in is the easy half.",
             "Nobody teaches the rest."],
    badge="BHAGAVAD GITA 12.9",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "ab_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "ab_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_abhimanyu_SILENT.mp4")
        print("recorded")
