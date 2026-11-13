# -*- coding: utf-8 -*-
"""
@dharmalock_omnipeace — "That prayer doesn't count." 2026-11-12.

SILENT, as normal for this account. Avi adds the trending sound in the TikTok
app and posts it himself; this account does not go through Post Bridge unless
he says so for a given post. The two times it did (Abhimanyu, Saal Mubarak)
were explicit one-offs - see omni_abhimanyu.py.

See pipeline/wantsomething_content.py for the full fact check and for why the
hook puts the reader in line one instead of opening on scripture.

WHY THE STRUCK LINE IS THE READER'S OWN VERDICT
This account's format strikes a wrong belief and corrects it, and the belief
that earns the strike here is not a fact about the Gita - it is the thing the
reader already says about themselves. "That prayer doesn't count" is what a
person thinks walking away from a mandir after asking for a job. Krishna
disagrees, in writing, in chapter 7. The correction is his, not ours.

Avi sent a @gita.talk post in the same register on 2026-11-12 (Bhima struck,
then the reader's own experience). Same mechanic, different story and
different claim, per the standing rule about not giving his friend grounds to
say he was copied.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight

POST = dict(
    struck="THAT PRAYER DOESN'T COUNT.",
    correction=["You wanted something.",
                "He counted it anyway."],
    reframe=["Krishna names four kinds",
             "of people who come to him."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["The hurting one. The curious one.",
         "The one who wants something. The wise one."],
        ["He calls all four of them good,",
         "and sends none of them away."],
    ],
    closing=["You are not at the top of that list.",
             "You are still on it."],
    badge="BHAGAVAD GITA 7.16",
)

if __name__ == "__main__":
    preflight()
    html = K.page(**POST)
    if sys.argv[1:2] == ["png"]:
        K.shot(html, K.OUT / "ws_omni_locked.png", 4.9)
        K.shot(html, K.OUT / "ws_omni_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_wantsomething_SILENT.mp4")
        print("recorded")
