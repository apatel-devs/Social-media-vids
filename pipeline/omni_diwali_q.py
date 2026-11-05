# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — "Why celebrate Lakshmi", 2026-11-05. SILENT.

Avi's brief: same story as today's @dharmalockapp post, but plainer. His own
framing for the hook: "why celebrate Lakshmi". So the struck claim is the
half-answer most people give - that Diwali is only about Ram - and the post
answers the question a nine year old actually asked.

Kept deliberately simple: short sentences, no abstractions, nothing a ten
year old would have to re-read.

FACT CHECK — see pipeline/diwali_q_content.py for the full working. In short,
verified against the text rather than the viral post it came from:
  * SB 8.7: the halahala poison comes up first; Shiva drinks it. SB 8.8.1
    opens "pite gare vrsankena" — when the poison had been drunk by Siva.
  * SB 8.8.8: Lakshmi herself appears, after the Apsaras.
  * SB 8.8.31-34: Dhanvantari comes last, with the amrita.
  So "poison came up before she did" is the text, not a flourish.

  NOT claimed as text: that the churning happened on Kartik Amavasya. The
  Puranas do not date it, so the night link stays in the question, never in
  the WHAT THE TEXT SAYS band.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="DIWALI IS JUST ABOUT RAM.",
    correction=["Then why do we celebrate",
                "Lakshmi on the same night?"],
    reframe=["Because of what the ocean",
             "gave up first."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Devas and asuras churned the ocean",
         "for a very long time."],
        ["Poison came up before she did.",
         "Shiva drank it. Then she rose."],
    ],
    closing=["She did not show up for the asking.",
             "She showed up after the worst of it."],
    badge="BHAGAVATA PURANA 8.8.8",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "dq_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "dq_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_diwaliq_LOCK_SILENT.mp4")
        print("recorded")
