# -*- coding: utf-8 -*-
"""
@dharmalockapp — Abhimanyu and the half-lesson. 2026-11-09.

THE HOOK
He knew how to get into the chakravyuha. Nobody had taught him how to get
out. That is what killed him, and it is the cleanest statement of the app's
own argument anywhere in the Mahabharata: starting is the half everybody
learns, finishing is the half nobody teaches.

WHY NOT THE BETRAYAL ANGLE
Avi sent @gita.talk's Abhimanyu post as the hook he wanted. That post reads
the story as betrayal - "it's the story of everyone who thought they'd never
do that to me", the ones who turned on him, and the wheel he picked up when
they broke his weapons. The story is public Mahabharata, but that reading is
his, and Avi's standing rule is that nothing can let his friend say he copied
him. So this takes the same character and makes a different claim: his post
says you don't control who turns on you; this one says you were never taught
the second half. No overlap in angle, scripture or wording.

FACT CHECK
  * The incomplete knowledge is canonical: Abhimanyu could penetrate the
    chakravyuha and did not know how to exit it, and that is what let him be
    surrounded and killed. Wikipedia's Abhimanyu article states it directly -
    "he was unable to hear how to exit the chakravyuha, and this incomplete
    knowledge later contributed to his demise."
  * He was sixteen. Standard across retellings.
  * Gita 12.9 verified at shlokam.org/gita/gita-12-9.htm.
  * Gita 2.40 verified at asitis.com/2/40.html - Devanagari, transliteration
    and translation taken from there.

  NOT CLAIMED: that he learned it in his mother's womb. That is the detail
  everyone knows and it is LATER FOLKLORE, not in the Mahabharata - Wikipedia
  labels it so explicitly. The copy stays off it rather than printing a folk
  addition as scripture and getting corrected in the comments. If a future
  post wants it, write it as "the story people tell", never as the text.

  NOT CLAIMED: who broke the rules, who surrounded him, or that it was unfair.
  That is the other post's territory and it is also the part where retellings
  disagree.
"""
CHIP = "MAHABHARATA"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("ABHIMANYU KNEW", False),
        ("HOW TO GET IN.", False),
        ("NOT HOW TO GET OUT.", True)]
BODY = ["He could break into the chakravyuha. He was never",
        "taught the way back out. Sixteen years old, alone",
        "inside it, and the exit was the half he never got."]
PILL = "BHAGAVAD GITA"

V1 = dict(
    source="BHAGAVAD GITA",
    title="If you cannot get there, practise your way there",
    reference="CHAPTER 12, VERSE 9",
    gloss=["Krishna does not say try harder. He says if you",
           "cannot hold it yet, repeat it until you can."],
    devanagari=["अथ चित्तं समाधातुं न शक्नोषि मयि स्थिरम् ।",
                "अभ्यासयोगेन ततो मामिच्छाप्तुं धनञ्जय ॥"],
    translit="Abhyasa-yogena tato mam icchaptum dhananjaya",
    translation="If you cannot hold your mind on me, then come to me by practice, done again and again.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="Nothing you start on this road is ever wasted",
    reference="CHAPTER 2, VERSE 40",
    gloss=["Nobody gets the whole lesson in one sitting.",
           "He says the part you did get is never lost."],
    devanagari=["नेहाभिक्रमनाशोऽस्ति प्रत्यवायो न विद्यते ।",
                "स्वल्पमप्यस्य धर्मस्य त्रायते महतो भयात् ॥"],
    translit="Svalpam apy asya dharmasya trayate mahato bhayat",
    translation="On this road nothing you begin is lost, and even a little of it guards you from the great fear.",
)

TURN = ["&ldquo;Everybody learns the way in.",
        "Almost nobody learns the way out.&rdquo;"]

REEL_SUB = "the exit was the half he missed."
REEL_CLOSE = [("WHAT DID YOU START", False),
              ("AND NEVER LEARN", False),
              ("HOW TO FINISH?", True)]
