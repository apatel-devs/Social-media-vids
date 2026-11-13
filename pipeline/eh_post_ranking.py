# -*- coding: utf-8 -*-
"""
@expandHinduism, "Ranking Hindu Apps". Avi's wording, 2026-11-13: cover title
"Ranking Hindu Apps" and "in smaller text top 7".

WHY IT SAYS TOP 5 AND NOT TOP 7
Asked on 2026-11-13, because "top 7" contradicts his own standing rule from
2026-11-07 ("keep the same exact apps and the pics from our first post, we
don't need any new ones everytime") - the series cast is five. A cover
reading "top 7" over five apps is the exact kind of thing the comments pick
apart. He chose: keep the five, cover says top 5. The seven is the FRAME
count (cover + five apps + CTA), not the app count, and that is probably
where the number came from.

    Build:  python3 pipeline/eh_apps.py --post eh_post_ranking \\
                --out ./frames --work .

ABOUT THE EMOJI
Avi asked for "top 7 🕉️📲" on the cover. The cover is drawn with PIL using
ArchivoBlack and Inter, and neither font carries emoji glyphs, so emoji in
COVER_SUB render as empty boxes. They live in the post caption instead, where
TikTok renders them properly. If a future session wants emoji ON the image it
needs an actual emoji font composited in - do not just paste them into
COVER_SUB and assume it worked.

ORDER, AND WHY THIS ONE
Fifth use of the reorder mechanic. Constraints: Dharma Lock is pinned at 3
(Avi's standing call) and mySatsang is never ranked low (slot 1 or 2 only),
which leaves twelve legal orders. Already spent:

    donthaveyet   5 Hindu Calendar  4 Gita  3 DL  2 mySatsang  1 Vignanam
    newyear       5 Vignanam  4 Hindu Calendar  3 DL  2 Gita  1 mySatsang
    whichofthese  5 Hindu Calendar  4 Gita  3 DL  2 Vignanam  1 mySatsang

This one is new, and it is the first time Hindu Calendar takes the top slot.
Eight orders left after this. The mechanic is close to exhausted and the real
fix is a new cast member or a new format, not a ninth shuffle - flagged to
Avi on 2026-11-12.

The cover photo and the per-app screenshots are pinned by the builder and are
the same as post one, on purpose: reusing one cover across the series is what
makes it read as one body of work.
"""

COVER_TITLE = "Ranking Hindu Apps"
COVER_SUB = "top 5"

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (5, 1557728556, "Vignanam",
     ["Stotras and slokas in your own script.", "Nothing to sign up for."], 0, False, 0.0),
    (4, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit next to it."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 6444313821, "mySatsang",
     ["Satsang you can actually get to, with", "people near you."], 0, False, 0.0),
    (1, 1321271821, "Hindu Calendar",
     ["Every vrat, tithi and festival, without", "asking your mum which day it is."], 0, False, 0.0),
]

CAPTION = ("Ranking Hindu apps 🕉️📲 All five of these live on my phone. "
           "No. 1 isn't mine 🙏")
