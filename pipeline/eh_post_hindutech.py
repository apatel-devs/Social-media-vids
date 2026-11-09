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
COVER_SUB = "five jobs, five apps, all on my phone"

# CUT FROM SIX TO FIVE APPS, 2026-11-07, for a posting reason rather than an
# editorial one. The eight-frame version failed to publish four times, always
# with TikTok's "took too long to process the upload". Ruled out on the night:
# payload size (a 1.1MB re-encode failed exactly like the 3.0MB original),
# malformed frames (all validate 1080x1920 RGB), TikTok being unable to fetch
# the images (they pull in ~0.15s, HTTP 200, from outside), the account and
# its connection (post one published fine on the same credentials), and Post
# Bridge itself (a dharmalockapp carousel published minutes earlier).
#
# The one variable left: every carousel that has ever published on any of
# these accounts was 5 or 7 frames, and the only one that would not go was
# the 8-frame one. So this drops to 7 frames - the exact shape of post one.
# Bhajan was the slot to lose: 4.6, the weakest rating of the six.
#
# This is inference from a handful of posts, not a documented TikTok limit.
# If a 7-frame post also fails, the cause is elsewhere and this note is wrong.
#
# ============================================================================
# 2026-11-09: EVERYTHING BELOW THIS LINE WAS WRONG. THE POSTS PUBLISHED.
#
# Avi: "it kept failing in post bridge but then posted 5 times so I deleted
# them." TikTok was accepting and publishing every one of these uploads.
# Post Bridge's "TikTok took too long to process the upload" is a
# CONFIRMATION TIMEOUT, not a failure - it gives up waiting for TikTok to
# report back, marks the post failed, and the post goes live anyway.
#
# So the frames were never the problem, the frame count was never the
# problem, and the account was never held. We spent two days diagnosing a
# reporting bug, and the only real damage was five duplicate posts on
# @expandHinduism that Avi had to delete by hand.
#
# THE RULE THAT MATTERS NOW: on this account, a reported failure is not a
# failure. Do NOT re-post, do NOT rebuild, do NOT "try 7 frames instead."
# Wait, then check the live profile. The error message says this itself -
# "It may still complete on TikTok's end" - and it was taken as boilerplate.
#
# The reasoning below is kept rather than deleted so the next session can see
# how a confident, well-evidenced diagnosis went wrong: every ruled-out
# suspect was ruled out correctly, and the conclusion was still false,
# because the one thing never questioned was whether "failed" meant failed.
# ============================================================================
#
# TESTED 2026-11-08 00:31 UTC. THE 7-FRAME VERSION FAILED THE SAME WAY.
# Post 64e953b0-a06b-4a64-bc77-9d1a82b5fedc, 7 frames, 1,179,678 bytes, all
# seven PUT returning 200: status went to "failed" after ~28 minutes with the
# same "TikTok took too long to process the upload". So frame count is NOT the
# cause and the five apps here are now just an editorial choice, not a fix.
#
# What that leaves, since Post Bridge, the credentials and the frames are all
# accounted for: TikTok's own side is accepting the upload and then never
# reporting it finished. Five attempts on this account have now timed out this
# way (post ids 6c6b4e8f, c2934d11, 51e72dd0, 6fcdabca, 64e953b0), while post
# one (be05af5b, 2026-11-05) published through the same path in the normal
# time. The leading guess is that this account is being held - new account,
# app-promotion content, and every attempt reusing a cover image that is
# byte-identical to the one already published, which is what duplicate
# detection looks for. Untested. Do not retry a sixth time on the same cover
# without checking the TikTok inbox first: the error says the upload may still
# complete on TikTok's end, so there may be queued copies sitting there.
#
# Next things to try, cheapest first:
#   1. Avi checks the @expandhinduism TikTok inbox and drafts for held copies.
#   2. A fresh cover photo rather than the pinned series cover.
#   3. platform_configurations.tiktok.draft = true, so TikTok only has to
#      accept the upload and not publish it, and Avi posts from the app.
#   4. Posting it by hand from the phone.
#
# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
APPS = [
    (5, 1434423184, "Japa 108",
     ["A mala counter that does not lose count", "when your thumb slips."], 0, False, 0.0),
    (4, 562758691, "Live Kirtan",
     ["Live darshan and kirtan from temples,", "on at hours that suit this timezone."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 930904592, "bliss by Gurudev",
     ["Art of Living's app. Breathwork and", "guided sits for when your head is loud."], 0, False, 0.0),
    # Neutral on the man himself. This account does not need the argument in
    # the comments, and the review count makes the case on its own.
    (1, 537568757, "Sadhguru",
     ["Twenty one thousand ratings. The", "biggest thing in this whole category."], 0, False, 0.0),
]
