# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — Kali Chaudas, 2026-11-07. SILENT.

Same night, same ordering point, in the LOCK format's plainer register. See
pipeline/kalichaudas_content.py for the full fact check: Kali Chaudas is the
night of 7 November 2026 and the same Chaturdashi is Diwali Hanuman Puja;
Hanuman is worshipped tonight as protection against fear and evil spirits;
Hanuman Chalisa verse 24 is the couplet recited for it.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="DIWALI STARTS TOMORROW.",
    correction=["Tonight has its own name.",
                "Kali Chaudas."],
    reframe=["The dark fourteenth.",
             "The night you call the guard."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["The Chalisa says nothing comes near",
         "when his name is spoken."],
        ["So tonight the puja is to Hanuman.",
         "Lakshmi is tomorrow."],
    ],
    closing=["Nobody calls the guard",
             "on an easy night."],
    badge="HANUMAN CHALISA 24",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "kc_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "kc_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_kalichaudas_LOCK_SILENT.mp4")
        print("recorded")
