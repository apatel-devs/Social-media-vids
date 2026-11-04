# -*- coding: utf-8 -*-
"""
@dharmalockapp — "You cleaned the whole house for Lakshmi", 2026-11-03.
Diwali run-up (Diwali Sun Nov 8).

FACT CHECK
  Bhagavata Purana 10.80-81 (vedabase.net): Sudama, a poor brahmana, came to
  Dwarka in a torn cloth with a small bundle of flat rice which he HID, being
  ashamed to offer it. Krishna took it and ate a handful with pleasure. His
  hovel was replaced by palaces on his return. He never asked for anything.
  Gita 9.26 (holy-bhagavad-gita.org): patram pushpam phalam toyam - a leaf,
  a flower, a fruit, water, offered with devotion, and I accept it.
  Gita 9.29: samo 'ham sarva-bhuteshu - I am equally disposed to all beings;
  none is hateful or dear to me.
"""
CHIP = "GITA WISDOM"
HEAD = [("YOU CLEANED THE WHOLE", False),
        ("HOUSE FOR LAKSHMI.", False),
        ("SHE NEVER ASKED.", True)]
BODY = ["Sudama walked to Dwarka in a torn cloth with a little",
        "flattened rice, too ashamed to hand it over. Krishna",
        "took it from him and ate it."]
PILL = "BHAGAVATA PURANA"

V1 = dict(
    source="BHAGAVAD GITA",
    title="A leaf, a flower, a fruit, water",
    reference="CHAPTER 9, VERSE 26",
    gloss=["He never set a minimum. The list is deliberately the cheapest",
           "things a poor person already has."],
    devanagari=["पत्रं पुष्पं फलं तोयं यो मे भक्त्या प्रयच्छति ।",
                "तदहं भक्त्युपहृतमश्नामि प्रयतात्मन: ॥"],
    translit="Patram pushpam phalam toyam yo me bhaktya prayacchati",
    translation="A leaf, a flower, a fruit, water. Whoever gives it to me with love, I take it, because of the heart it came from.",
)

V2 = dict(
    source="BHAGAVAD GITA",
    title="I am the same to every single person",
    reference="CHAPTER 9, VERSE 29",
    gloss=["Nobody gets a better seat for having a bigger house.",
           "The door opens the same for everyone."],
    devanagari=["समोऽहं सर्वभूतेषु न मे द्वेष्योऽस्ति न प्रिय: ।",
                "ये भजन्ति तु मां भक्त्या मयि ते तेषु चाप्यहम् ॥"],
    translit="Samo 'ham sarva-bhuteshu na me dveshyo 'sti na priyah",
    translation="I am the same to everyone. Nobody is further away from me, and nobody is closer. Come to me and I am right there.",
)

TURN = ["&ldquo;You scrubbed every room she was",
        "never going to inspect.&rdquo;"]

REEL_SUB = "she was never coming for the floors."
REEL_CLOSE = [("WHAT DID YOU CLEAN", False),
              ("SO HARD YOU FORGOT", False),
              ("TO SIT DOWN?", True)]
