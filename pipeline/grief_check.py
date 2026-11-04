"""The real `images/gita_grief` post, as data, so verify.py can re-render it.

This is the carousel template's reference post. Do not edit the copy — it is
transcribed from the published cards in reference/originals/.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dl_cards as D

HOOK = D.hook_card(
    chip="GITA WISDOM",
    head_lines=[("YOU STILL GO TO TEXT THEM", False),
                ("BEFORE YOU REMEMBER.", True)],
    body_lines=["Arjuna froze in front of people he'd have to bury.",
                "Krishna didn't tell him the grief was wrong &mdash; he told",
                "him what death can't reach."],
    pill="BHAGAVAD GITA")

REFL = D.reflection_card("YOUR TURN",
    ["&ldquo;The part of them you keep reaching",
     "for was never the part that died.&rdquo;"])

VERSE = D.verse_card(
    source="BHAGAVAD GITA",
    title="The soul is never born, and it never dies",
    reference="CHAPTER 2, VERSE 20",
    gloss=["Krishna said this to a man standing in front of everyone he was about to",
           "lose. Not as comfort &mdash; as fact."],
    devanagari=["न जायते म्रियते वा कदाचिन्नायं भूत्वा भविता वा न भूयः।",
                "अजो नित्यः शाश्वतोऽयं पुराणो न हन्यते हन्यमाने शरीरे॥"],
    translit="Na jayate mriyate va kadachin nayam bhutva bhavita va na bhuyah",
    translation="The soul is never born, nor does it ever die. It is unborn, eternal, everlasting and ancient. It is not slain when the body is slain.")

if __name__ == "__main__":
    D.shot(HOOK, D.OUT / "chk_hook.png")
    D.shot(VERSE, D.OUT / "chk_verse.png")
    D.shot(REFL, D.OUT / "chk_refl.png")
    print("rendered")
