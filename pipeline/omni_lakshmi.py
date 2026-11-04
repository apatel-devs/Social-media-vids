# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — "She comes to clean houses", 2026-11-03. SILENT.

Avi's brief: keep "Lakshmi comes to the cleanest house" as the struck claim,
then say something about poor people who don't live in a nice house - she
still visits them. Then the quote, as usual.

FACT CHECK — Bhagavata Purana, Canto 10, ch. 80-81 (vedabase.net summary):
  * Sudama came to Dwarka a poor brahmana in a torn cloth.
  * He brought a small bundle of flat rice and HID it, ashamed to offer
    something so meagre.
  * Krishna took the bundle himself and ate a handful with great pleasure;
    he was reaching for a second when Rukmini stopped him.
  * Sudama's home had been a broken-down hovel; he returned to find palaces.
  * He never asked for anything.
Nothing here is embroidered - the shame, the hiding and the eating are all
in the text.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="SHE COMES TO CLEAN HOUSES.",
    correction=["She walked into a hut",
                "with a broken roof."],
    reframe=["Sudama had nothing to bring.",
             "He brought it anyway."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["He came in a torn cloth with a little",
         "flattened rice, and hid it behind his back."],
        ["Krishna took it from him and ate it.",
         "He went home to a palace. He never asked."],
    ],
    closing=["She was never checking the floors.",
             "She was watching who showed up."],
    badge="BHAGAVATA PURANA 10.81",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "lak_locked.png", 4.9)
        K.shot(html, K.OUT / "lak_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_lakshmi_LOCK_SILENT.mp4")
        print("recorded")
