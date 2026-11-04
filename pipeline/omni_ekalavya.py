"""
Ekalavya in the @dharmalock_omnipeace LOCK format — 2026-11-02.

Built on omni_kit, which was measured off a real posted video rather than
described from notes. Ships SILENT.

FACT CHECK — Mahabharata, Adi Parva, Sambhava Parva, Section CXXXIV
(Ganguli, ibiblio.org/sripedia m01/m01135):
  * Drona "accepted not the prince as his pupil in archery, seeing that he
    was a Nishada who might (in time) excel all his high-born pupils."
  * Ekalavya "made a clay-image of Drona, and began to worship it."
  * Drona asked for "the thumb of thy right hand"; Ekalavya "cut off without
    ado his thumb, and gave it unto Drona."
  The text says "fees," not "guru-dakshina" — the copy doesn't put a word in
  the text's mouth. "Nishada" is rendered as "the wrong family" to keep the
  plain-language bar without turning the slide into a caste lecture.

NOT Abhimanyu — that is the exact post Avi's friend made (@gita.talk), and
Avi said on 10/29 "I don't want my friend saying I copied him."
"""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import omni_kit as K
from _guard import preflight
preflight()

POST = dict(
    struck="THE THUMB WAS DEVOTION.",
    correction=["It was the price of a lesson",
                "nobody agreed to teach him."],
    reframe=["Drona shut the door on him.",
             "He learned anyway, alone."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Drona turned him away. Wrong family, he said,",
         "and too likely to beat the princes."],
        ["So he made a clay statue of Drona",
         "and taught himself in front of it."],
    ],
    closing=["They came for the thumb",
             "only after he got better than them."],
    badge="ADI PARVA 134",
)

if __name__ == "__main__":
    html = K.page(**POST)
    mode = sys.argv[1] if len(sys.argv) > 1 else "png"
    if mode == "png":
        K.shot(html, K.OUT / "omni2_locked.png", 4.9)
        K.shot(html, K.OUT / "omni2_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_ekalavya_LOCK_SILENT.mp4")
        print("recorded")
