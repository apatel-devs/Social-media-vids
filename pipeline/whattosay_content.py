# -*- coding: utf-8 -*-
"""
@dharmalockapp — "You don't know what to say when you pray." 2026-11-24.

Voice per abcd_content.py (Avi, 11/23): young adult, short lines, name the
real thing, scripture is the payoff and never the hook, forgiving at the
turn.

WHY THIS ANGLE
Every Dharma Lock post so far has described the app as the thing that locks
your phone. The App Store listing's SECOND feature is that it checks how
you are feeling and gives you a Sanskrit mantra matched to that mood, and
we had never once used it. A competitor doing roughly that one thing
(@gitaforall_app, Gita verse by mood) has a post at 163K likes and 16.6K
shares, which is more than this whole account has ever done. So: the lock
is the hook everyone has heard from us, and the mantra is the one they
have not.

The reader-side of that feature is not "mood matching", it is not knowing
what to say. That is the hook.

THE PAYOFF IS THE BEST ONE THIS ACCOUNT HAS HAD
The Bhagavad Gita exists because somebody admitted he did not know what to
do. 2.7 is Arjuna saying it out loud - my mind is confused, tell me plainly
what is best, I am your student. Seven hundred verses follow from that one
sentence. A reader who feels stupid for not knowing how to pray is in
exactly Arjuna's position at the start of the book, and nobody tells them
that.

FACT CHECK
  * Gita 2.7 verified at asitis.com/2/7.html. Devanagari and transliteration
    from there. Arjuna, confused about his duty, asks Krishna to tell him
    plainly what is best and calls himself his student.
  * Gita 10.10 verified at vivekavani.com/b10v10. Devanagari and IAST from
    there. To those devoted and worshipping with love, he gives the
    buddhi-yoga by which they come to him.

  NOT CLAIMED: that Krishna hands you words to say. 10.10 gives
  buddhi-yoga - understanding - not a script. The copy says he gives you
  the understanding, deliberately, and does not promise the app's mantra is
  the thing Krishna meant.

  NOT CLAIMED: that Arjuna did not know how to pray. He did not know what
  was RIGHT TO DO; the copy says "he did not know what to say either",
  which is the honest stretch - he says pricchami tvam, I am asking you,
  having just said his mind is confused. Keep it at that. Do not escalate
  it into "Arjuna forgot how to pray", which the text does not support.
"""
CHIP = "BHAGAVAD GITA"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("YOU DON'T KNOW", False),
        ("WHAT TO SAY", False),
        ("WHEN YOU PRAY.", True)]
BODY = ["Neither did Arjuna. He said it out loud, to God,",
        "with an army in front of him. Seven hundred verses",
        "come after that one sentence."]
PILL = "CHAPTER 2"

V1 = dict(
    source="BHAGAVAD GITA",
    title="The whole Gita starts with I don't know",
    reference="CHAPTER 2, VERSE 7",
    gloss=["My head is a mess, he says. Tell me plainly.",
           "That is the sentence the book answers."],
    devanagari=["कार्पण्यदोषोपहतस्वभावः पृच्छामि त्वां धर्मसम्मूढचेताः ।",
                "यच्छ्रेयः स्यान्निश्चितं ब्रूहि तन्मे शिष्यस्तेऽहं शाधि मां त्वां प्रपन्नम् ॥"],
    translit="Pricchami tvam dharma-sammudha-cetah",
    translation="My mind is confused about what is right. Tell me plainly what is best. I am your student, teach me.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="He gives you the understanding, not a script",
    reference="CHAPTER 10, VERSE 10",
    gloss=["You are not supposed to arrive knowing.",
           "Showing up is the part that is yours."],
    devanagari=["तेषां सततयुक्तानां भजतां प्रीतिपूर्वकम् ।",
                "ददामि बुद्धियोगं तं येन मामुपयान्ति ते ॥"],
    translit="Dadami buddhi-yogam tam yena mam upayanti te",
    translation="To those who keep coming back to me with love, I give the understanding that brings them to me.",
)

TURN = ["&ldquo;You are not bad at praying.",
        "You were never given the words.&rdquo;"]

REEL_SUB = "neither did Arjuna."
REEL_CLOSE = [("YOU DON'T NEED", False),
              ("THE RIGHT WORDS.", False),
              ("YOU NEED TO ASK.", True)]
