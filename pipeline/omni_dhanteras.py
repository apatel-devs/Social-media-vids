# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — Dhanteras, 2026-11-06. SILENT.

Same angle as the @dharmalockapp post, in the LOCK format's plainer register.
See pipeline/dhanteras_content.py for the full fact check and for why the
hook deliberately avoids the "Dhanteras isn't about gold" framing of the
viral post Avi sent - it leads on the churning sequence instead, which is
this account's own continuing thread.

Verified: Dhanteras 2026 is 6 November and is also Dhanvantari Trayodashi;
SB 8.8.33 has the figure bearing a pot of amrita; he comes last in the
churning, after Lakshmi at 8.8.8.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="DHANTERAS IS GOLD DAY.",
    correction=["It is also the day of",
                "a physician."],
    reframe=["He came out of the same",
             "ocean as Lakshmi. Last."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Lakshmi rose from that churning.",
         "He rose from it after her."],
        ["He was holding a pot of amrita.",
         "Medicine. Not coins, not a chain."],
    ],
    closing=["Buy the gold if you want it.",
             "You cannot re-buy your health."],
    badge="BHAGAVATA PURANA 8.8.33",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "dh_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "dh_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_dhanteras_LOCK_SILENT.mp4")
        print("recorded")
