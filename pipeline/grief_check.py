"""Re-render the real gita_grief post and compare to the committed originals."""
import sys; sys.path.insert(0,"/home/claude/dl")
import dl_cards as D

D.shot(D.hook_card(
    chip="GITA WISDOM",
    head_lines=[("YOU STILL GO TO TEXT THEM", False),
                ("BEFORE YOU REMEMBER.", True)],
    body_lines=["Arjuna froze in front of people he'd have to bury.",
                "Krishna didn't tell him the grief was wrong &mdash; he told",
                "him what death can't reach."],
    pill="BHAGAVAD GITA"), D.OUT/"chk_hook.png")

D.shot(D.reflection_card("YOUR TURN",
    ["&ldquo;The part of them you keep reaching",
     "for was never the part that died.&rdquo;"]), D.OUT/"chk_refl.png")

D.shot(D.verse_card(
    source="BHAGAVAD GITA",
    title="The soul is never born, and it never dies",
    reference="CHAPTER 2, VERSE 20",
    gloss=["Krishna said this to a man standing in front of everyone he was about to",
           "lose. Not as comfort &mdash; as fact."],
    devanagari=["न जायते म्रियते वा कदाचिन्नायं भूत्वा भविता वा न भूयः।",
                "अजो नित्यः शाश्वतोऽयं पुराणो न हन्यते हन्यमाने शरीरे॥"],
    translit="Na jayate mriyate va kadachin nayam bhutva bhavita va na bhuyah",
    translation="The soul is never born, nor does it ever die. It is unborn, eternal, everlasting and ancient. It is not slain when the body is slain.",
), D.OUT/"chk_verse.png")
print("rendered")
