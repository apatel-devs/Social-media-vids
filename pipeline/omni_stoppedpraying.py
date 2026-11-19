# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — "You have to start over." 2026-11-19.

SILENT, as normal for this account. Avi adds the trending sound in the
TikTok app and posts it himself; he said today he is posting Amy, Dharma
Lock and Omni by hand, so nothing here goes near Post Bridge.

See pipeline/stoppedpraying_content.py for the fact check, including the
care needed around 6.43 and rebirth.

THE STRUCK LINE
It is what the lapsed person believes about themselves, and Krishna
contradicts it directly in answer to the exact question Arjuna asked about
them. 23 characters, inside the 26 that fit - see omni_kit, which now
measures this and refuses to render an overlong one after the "ADDICTED"
line ran off the frame on 2026-11-14.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="YOU HAVE TO START OVER.",
    correction=["You start from where",
                "you stopped."],
    reframe=["Arjuna asked Krishna",
             "about exactly this."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["What happens to the one who had faith",
         "and could not hold on to it?"],
        ["Nothing he did is destroyed. What he",
         "understood comes back to him."],
    ],
    closing=["You are not starting from zero.",
             "You are starting from where you stopped."],
    badge="BHAGAVAD GITA 6.40",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "sp_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "sp_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_stoppedpraying_SILENT.mp4")
        print("recorded")
