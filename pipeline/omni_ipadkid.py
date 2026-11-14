# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — "It's the kids who are addicted." 2026-11-14.

SILENT, as normal for this account. Avi adds the trending sound in the
TikTok app and posts it himself. He said on 2026-11-14 that he is posting
everything manually today except @expandHinduism, so nothing here goes
through Post Bridge.

See pipeline/ipadkid_content.py for the full fact check and for why the
hook names "the kids" rather than "your kid".

THE STRUCK LINE
It is the sentence the reader would say out loud about somebody else's
children, and the correction turns it around without letting them off. Same
mechanic Avi pointed at in the @gita.talk Bhima post on 2026-11-12: strike
the easy belief, then put the reader in the second line. Different subject
and different claim, per the standing rule about his friend's posts.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="IT'S THE KIDS WHO ARE ADDICTED.",
    correction=["You handed them the iPad.",
                "You were already on yours."],
    reframe=["Nobody is born knowing",
             "how to sit still."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Krishna says people copy whoever",
         "they look up to. Not what they are told."],
        ["And when the mind runs off,",
         "you catch it and bring it back. Again."],
    ],
    closing=["You cannot hand them a habit",
             "you do not have yourself."],
    badge="BHAGAVAD GITA 3.21",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "ik_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "ik_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_ipadkid_SILENT.mp4")
        print("recorded")
