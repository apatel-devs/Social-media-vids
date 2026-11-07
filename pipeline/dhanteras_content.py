# -*- coding: utf-8 -*-
"""
@dharmalockapp — Dhanteras, 2026-11-06. Part two of the Samudra Manthan run.

THE ANGLE, AND WHY IT IS NOT THE OBVIOUS ONE
Avi sent two reference posts: a @gita.talk card on Gita 17.20 (giving), and a
@soumya_aggarwal__ carousel at 36K likes reading "Dhanteras isn't about buying
gold - 'Dhan' was never money. It was the one thing money can't buy."

Both were taken as look references only. The gold-versus-health turn is
exactly where this post would naturally land, which is the problem: at 36K
likes that line has been widely seen, and Avi does not want these accounts
reading as derivative. So the hook leads instead with the thing only this
account can say - we posted Lakshmi rising from the churning yesterday, and
Dhanvantari rose from the SAME churning, last. The viral post asserts; this
one shows the verse and continues a series already in progress.

FACT CHECK
  * Dhanteras 2026 is Friday 6 November, and the same day is Dhanvantari
    Trayodashi - verified at drikpanchang.com/diwali/dhanvantari-trayodashi.
    The day is named for the physician, not only for wealth.
  * SB 8.8.33 describes the figure carrying the nectar pot:
    "amritapurna-kalasam bibhrad valaya-bhushitah" - bearing a pot filled
    with amrita, adorned with bracelets. Devanagari verified at
    vedapath.app/bhagavatam/ashtama-skandha/8/33. The Sanskrit of that verse
    does not name him; the surrounding passage and the tradition do, so the
    copy says "the physician" rather than putting a name in the verse's mouth.
  * He comes LAST in the churning sequence (8.8.31-34), after Lakshmi at
    8.8.8. That ordering is the spine of the post.
  * Gita 6.17 Devanagari and sense verified at shlokam.org/bhagavad-gita/6-17.

  NOT claimed: any scriptural statement that the churning happened on
  Dhanteras. The Puranas do not date it. Same restraint as yesterday.
"""
CHIP = "DHANTERAS"
# Line 3 stays short: the temple crop sits bottom-right of the hook card.
HEAD = [("THEY TORE UP AN OCEAN", False),
        ("TO FIND ONE THING.", False),
        ("IT WASN'T GOLD.", True)]
BODY = ["Gold came up. Jewels, a horse, a wish-granting tree.",
        "All of it got divided up. Then Dhanvantari, the god of",
        "medicine, came up holding amrita, and the war started."]
PILL = "BHAGAVATA PURANA"

V1 = dict(
    source="BHAGAVATA PURANA",
    title="The god of medicine, holding a pot of amrita",
    reference="CANTO 8, CHAPTER 8, VERSE 33",
    gloss=["This is Dhanvantari, and the day is named after him.",
           "The demons snatched the pot and ran the moment he rose."],
    devanagari=["स्‍निग्धकुञ्चितकेशान्तसुभग: सिंहविक्रम: ।",
                "अमृतापूर्णकलसं बिभ्रद् वलयभूषित: ॥"],
    translit="Amritapurna-kalasam bibhrad valaya-bhushitah",
    translation="Bearing a pot filled with nectar, his arms circled with bracelets.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="It works for the one who is not at war with himself",
    reference="CHAPTER 6, VERSE 17",
    gloss=["Gold you can buy again tomorrow. This is the other",
           "kind of wealth, and it runs on ordinary habits."],
    devanagari=["युक्ताहारविहारस्य युक्तचेष्टस्य कर्मसु ।",
                "युक्तस्वप्नावबोधस्य योगो भवति दु:खहा ॥"],
    translit="Yuktahara-viharasya yukta-cestasya karmasu",
    translation="For the one whose eating and resting, whose work, whose sleeping and waking are all in measure, this practice is what ends the suffering.",
)

TURN = ["&ldquo;The war was never",
        "about the gold.&rdquo;"]

REEL_SUB = "and that is when the war started."
REEL_CLOSE = [("YOU BOUGHT THE GOLD.", False),
              ("NOW GO TO BED", False),
              ("ON TIME.", True)]
