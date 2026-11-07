# -*- coding: utf-8 -*-
"""
@expandHinduism, post 2 of the countdown series — "Hindu tech for everyone".
Avi picked this topic from his queued list on 2026-11-06.

Build it with the committed builder, which carries the layout and the rules:

    python3 pipeline/eh_apps.py --post eh_post_hindutech \\
        --out ./frames --work .

Same cover photo as post 1, on purpose. Reusing one cover across the series
is the mechanic that made @swingthoughtsgolf read as one body of work, and
the builder pins that photo, so nothing here needs to repeat it.

HOW THIS LIST WAS CHOSEN
  * Every app is a real App Store listing with a real rating; the builder
    re-pulls the numbers on each run. Candidates with fewer than ~40 ratings
    were not considered, so no slot is padded with something nobody uses.
  * Six different jobs rather than six rivals: bhajans, a japa counter, live
    kirtan, the lock screen, and the two big meditation apps. That is what
    makes it "tech for everyone" rather than post one with new names.
  * Dharma Lock sits at #3. Avi's standing call for this series.
  * Sadhguru is at #1 with 21k ratings. A competitor at the top is what buys
    the list its credibility, and nobody can argue with that review count.
  * DELIBERATELY LEFT OUT: "Diya - Daily Hindu Practice" (4.83, 559 ratings).
    It would have ranked, but the series rule bars anything doing lock-screen
    or daily practice, because that is Dharma Lock's own lane and putting a
    direct rival in the list works against the CTA frame.
  * No overlap with post one except Dharma Lock itself, so the two posts do
    not read as the same list twice.
"""

COVER_TITLE = "Hindu Tech For Everyone"
COVER_SUB = "six jobs, six apps, all on my phone"

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (6, 815022661, "Bhajan",
     ["Every bhajan and aarti you half know the", "words to. Free, and it downloads."], 0, False, 0.0),
    (5, 1434423184, "Japa 108",
     ["A mala counter that does not lose count", "when your thumb slips."], 0, False, 0.0),
    (4, 562758691, "Live Kirtan",
     ["Live darshan and kirtan from temples,", "on at hours that suit this timezone."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 930904592, "bliss by Gurudev",
     ["Art of Living's app. Breathwork and", "guided sits, if that is your thing."], 0, False, 0.0),
    (1, 537568757, "Sadhguru",
     ["Twenty one thousand ratings. Whatever", "you think of him, the app is good."], 0, False, 0.0),
]
