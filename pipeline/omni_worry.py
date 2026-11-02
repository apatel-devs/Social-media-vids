"""
@dharmalock_omnipeace — "Worry is a luxury", 2026-11-02. SILENT.

Source: a viral TikTok Avi sent, captioned as Bhagavad Gita 2.70, Gita Press
Gorakhpur: "Krishna smiled on the battlefield, not because he didn't care,
but because he knew worry never changed destiny. Worry is a luxury of those
who have forgotten who is in control."

FACT CHECK — that is not Gita 2.70, and not any verse. 2.70 is the ocean
verse (verified at holy-bhagavad-gita.org/chapter/2/verse/70):

  आपूर्यमाणमचलप्रतिष्ठं समुद्रमाप: प्रविशन्ति यद्वत् |
  तद्वत्कामा यं प्रविशन्ति सर्वे स शान्तिमाप्नोति न कामकामी ||

  "Just as the ocean remains undisturbed by the incessant flow of waters
  from rivers merging into it, likewise the sage who is unmoved despite the
  flow of desirable objects all around him attains peace, and not the person
  who strives to satisfy desires."

Nothing about a battlefield, a smile, worry, destiny or control. So the post
uses the account's own format for exactly what it is for: the popular line
struck out, and what the text actually says underneath. Avi's words are the
struck claim, which is the most direct use of them available.
"""
import sys
sys.path.insert(0, "/home/claude/dl")
import omni_kit as K

POST = dict(
    struck="WORRY IS A LUXURY.",
    correction=["Gita 2.70 never says that.",
                "It says something harder."],
    reframe=["Krishna did not tell Arjuna",
             "to stop worrying."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["He pointed at the ocean.",
         "Rivers pour in all day. It never rises."],
        ["Let wanting pour into you like that",
         "and you get peace. Chase it and you don't."],
    ],
    closing=["Calm is not knowing the ending.",
             "It is not needing to."],
    badge="BHAGAVAD GITA 2.70",
)

if __name__ == "__main__":
    html = K.page(**POST)
    mode = sys.argv[1] if len(sys.argv) > 1 else "png"
    if mode == "png":
        K.shot(html, K.OUT / "worry_locked.png", 4.9)
        K.shot(html, K.OUT / "worry_final.png", 9.0)
        print("stills")
    else:
        K.record(html, K.OUT / "omnipeace_worry_LOCK_SILENT.mp4")
        print("recorded")
