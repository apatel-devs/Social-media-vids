# -*- coding: utf-8 -*-
"""
@dharmalockapp — "You only pray when you want something." 2026-11-12.

WHY THIS HOOK, AND WHY IT IS BUILT THIS WAY
Avi, 2026-11-12: "What I'm still seeing is that main hooks you send are always
so bland or they don't catch the user and are confusing."

He was right, and the 30-day numbers say exactly where it goes wrong. Ranked
by views on @dharmalockapp:

    410  "Tonight you pray to the devotee before you pray to God"
    346  "Darkness has never put out a single flame"
    158  "Abhimanyu knew how to get into the chakravyuha"
    131  "Saal Mubarak - Vikram Samvat 2083"

The two that worked put THE READER in the first sentence, or gave one plain
picture. The two that died opened with a proper noun most of the audience
cannot place, or with a greeting - information about the day rather than
about the person holding the phone. Abhimanyu is the "confusing" case in its
purest form: if you do not already know the story, line one is homework.

THE RULE THIS FILE EXISTS TO ENFORCE
Line one is about the reader. Scripture is the PAYOFF, never the opener. If
the first card could be printed on a calendar, it is the wrong first card.

Avi picked this hook from four on 2026-11-12. He also sent a @gita.talk post
the same minute - Bhima, struck line, then "for everyone who's heard: you're
strong, you'll be fine" - as the register he wants. Same move: accusation,
then the reader's own life. Different story and different claim, per the
standing rule that nothing can let his friend say he copied him.

WHY THIS HOOK AND NOT A SCOLD
Every account in this niche runs the scold. The turn here is that Krishna
got there first and was KINDER about it than the internet is: he names the
man who shows up because he wants something, and calls him virtuous anyway.
That is the surprise, and surprise is what gets shared.

FACT CHECK
  * Gita 7.16 verified at shlokam.org/gita/gita-7-16.htm. Devanagari,
    transliteration and the four types taken from there. The four are arta
    (distressed), jijnasu (seeker of knowledge), artharthi (seeker of
    wealth/wanting something) and jnani (the wise). Krishna calls all four
    SUKRTINAH - virtuous, doers of good. That word is the whole post.
  * Gita 7.18 verified at vivekavani.com/b7v18/. "Udarah sarva evaite" -
    "noble indeed are they all" - and then the jnani is deemed Krishna's
    very self.

  NOT CLAIMED: that the four are equal, or that wanting something is as good
  as wisdom. 7.17 and 7.18 both say plainly that the jnani is dearest, and a
  post that flattened that would be corrected in the comments by anyone who
  has read the chapter. The copy says you are ON the list, not at the top of
  it, and that is both the honest reading and the better line.

  NOT CLAIMED: that Krishna promises to give you the thing you asked for.
  9.22 ("yoga-kshemam vahamy aham") is the verse people reach for here and it
  does NOT apply - it is addressed to the undivided devotee, not to the one
  who came with a list. Deliberately left out.
"""
CHIP = "BHAGAVAD GITA"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("YOU ONLY PRAY", False),
        ("WHEN YOU WANT", False),
        ("SOMETHING.", True)]
BODY = ["Krishna knew. He counted four kinds of people who come",
        "to him, and one of them is the one who came because he",
        "wanted something. He called all four of them good."]
PILL = "CHAPTER 7"

V1 = dict(
    source="BHAGAVAD GITA",
    title="He names the one who came for a reason",
    reference="CHAPTER 7, VERSE 16",
    gloss=["Four kinds of people come to me, he says. The hurting,",
           "the curious, the one who wants something, and the wise."],
    devanagari=["चतुर्विधा भजन्ते मां जनाः सुकृतिनोऽर्जुन ।",
                "आर्तो जिज्ञासुरर्थार्थी ज्ञानी च भरतर्षभ ॥"],
    translit="Chaturvidha bhajante mam janah sukritino'rjuna",
    translation="Four kinds of good people worship me: the one in pain, the one who wants to know, the one who wants something, and the wise one.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="Noble, all of them",
    reference="CHAPTER 7, VERSE 18",
    gloss=["He does not say the four are the same. He says not one",
           "of them is turned away. You are on the list."],
    devanagari=["उदाराः सर्व एवैते ज्ञानी त्वात्मैव मे मतम् ।",
                "आस्थितः स हि युक्तात्मा मामेवानुत्तमां गतिम् ॥"],
    translit="Udarah sarva evaite jnani tvatmaiva me matam",
    translation="Noble are they all. The wise one I hold as my own self.",
)

TURN = ["&ldquo;You are not at the top of that list.",
        "You are still on it.&rdquo;"]

REEL_SUB = "so did almost everyone in the Gita."
REEL_CLOSE = [("KEEP COMING", False),
              ("FOR THE WRONG REASON", False),
              ("UNTIL IT IS THE RIGHT ONE.", True)]
