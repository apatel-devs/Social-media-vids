# Dharma Lock — social pipeline storage

Storage backend for the Dharma Lock daily content automation.

## /assets
Brand assets (fonts, logo, template images) needed to render posts via the
`dharma-lock-social-posts` skill. The daily scheduled task clones this repo
at the start of each run to restore these instead of asking Avi to re-attach
a zip.

## /videos
Finished rendered videos, named `YYYY-MM-DD_<concept-slug>.mp4`. Pushed here
after Avi approves a build, so Post Bridge can fetch the raw GitHub URL
directly (Post Bridge has no GitHub login, so these files are public by
necessity — same content that's about to be posted publicly to
@dharmalockapp on Instagram/TikTok anyway).

Public repo — nothing sensitive is stored here.
