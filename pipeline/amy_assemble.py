# -*- coding: utf-8 -*-
"""
@amysharma_dharma — assemble one post: reaction clip + CTA, music baked in.

WHY THIS FILE EXISTS
--------------------
On 2026-11-05 the build container was rebuilt and the Amy working files went
with it. amy_caption.py (the overlay) was committed, but the assembly - where
the source clips live, how a long clip is split, which CTA gets appended, how
the audio is laid out - was not, so it had to be worked out again from
scratch. This file is that knowledge, committed. Re-run it.

WHERE THE SOURCES LIVE (Google Drive, link-accessible)
------------------------------------------------------
The Claude container cannot reach Drive's file hosts, but the Higgsfield
sandbox can, and these files are reachable by link:

    https://drive.google.com/uc?export=download&id=<FILE_ID>

THE PACK HAS SEVEN CREATORS, NOT ONE. "100 UGC Reactions Pack",
Drive folder 1igdcapsIM3DrAaYfGI0zzK0ur6NAVvJi, holds subfolders
1, 1a, 2, 2a, 3, 4 and 5 - a different person in each.

    3  "black hair"  1xIZ4QYAQwHQRBP1MxWeGmqrOdQhHPHqS   (3a - 3j)
    4  "brunette"    1dTt6b76pvJkOGat2JfJRKpYfJRR32urW   (1a - 1w, 23 clips)

Avi, 2026-10-27, said "Start with 3 in order. Don't slip around", and that
was read as "only ever use 3". By 2026-11-12 three posts running were the
same woman in the same outfit in the same salon, and Avi caught it: "I see
that you have been using the same reaction for the last 3 posts."

So: in order WITHIN a creator, but rotate the creator between posts. Never
ship two consecutive posts from the same folder, and never the same shoot
three times. Only folders 3 and 4 have been catalogued; 1, 1a, 2, 2a and 5
are unexplored.

CTA clips live in a different folder, 1tm90thYotmpm_XWS9Ath-NNkERAxUM4v,
as cta 1-5.mp4. Avi picked **cta 1.mp4** on 2026-11-05. Do not swap it
without asking - a different tail would break the series.

THE RULES THIS ENCODES (from the account's standing notes)
----------------------------------------------------------
* Reaction clip FIRST, CTA appended after.
* A reaction clip of roughly 7 seconds or more is SPLIT IN TWO and becomes
  two posts. 3c is 7.48s, so part 1 is 0 -> 3.7417 and part 2 is 3.7417 ->
  end. Split at the midpoint so the two halves are reproducible without
  having to remember where the last one stopped.
* The CTA is never cut down. Avi: it may be sped up or left exactly as is.
  It ships here exactly as is, INCLUDING ITS OWN AUDIO, which is why the
  music is a bed underneath rather than a replacement.
* Nothing on this account ships silent - music is baked into both the
  Instagram and the TikTok cut. Trending audio was traded away on this
  account in exchange for hands-off scheduling.
* Overlay: never over the face or chest, centred at the neck/collar line,
  whole block appears at once, first word capitalised. See amy_caption.py,
  whose numbers were measured off the account's own live grid.

GOTCHAS THAT COST TIME
----------------------
* iPhone .MOV carry rotation metadata that ffmpeg applies automatically.
  NEVER add a transpose filter - it double-rotates.
* The source is 3840x2160 at 60fps with rotation 90, so it presents as
  2160x3840, exactly 9:16. Scale straight to 1080x1920.
* Reaction clips have NO audio track. Concat needs a uniform audio layout,
  so silence is added to the reaction before joining or the join drops the
  CTA's audio.
* Playwright is installed in the sandbox but its browser is not, and pip is
  broken there because PYTHONPATH contains an unreadable /root. Install and
  run with the env prefix in SANDBOX_ENV below.
* Cloudflare returns a 502 on long sandbox_exec chains fairly often. The
  work usually completed - re-probe which outputs exist and resume rather
  than re-running the whole chain.

USAGE (in the Higgsfield sandbox)
---------------------------------
    python3 amy_assemble.py --clip-id <drive id> --start 3.7417 \\
        --cta-id 19Zo7NSFkAyjuwdYernyHmbviX_JrjMwN \\
        --line "Okay so it really won't" --line "open until you PRAY" \\
        --line "to Bhagwan first" --out amy_3c_part2.mp4
"""
import argparse
import pathlib
import subprocess

REPO = pathlib.Path(__file__).resolve().parent.parent

DRIVE = "https://drive.google.com/uc?export=download&id={}"

# Drive ids worth keeping at hand.
CTA_IDS = {
    "cta 1.mp4": "19Zo7NSFkAyjuwdYernyHmbviX_JrjMwN",   # Avi's pick, 2026-11-05
    "cta 2.mp4": "1jkdKwhWtP3nE6B43Ah4ztPZqE9jF954N",
    "cta 3.mp4": "19StGEpHYKMOiflRaNS1aCO2HSx0SKwgH",
    "cta 4.mp4": "1vY0YUTELXuUNo9m_Xx2agnZYN0Q_TU79",
    "cta 5.mp4": "1WqTZPSFQJW1pDknazWq6eAPye2g1FHuL",
}
CLIP_IDS = {
    "black hair 3a.mov": "1svsvsuKyQM-LUvxE_rgDseC3wB3ndB2-",
    "black hair 3b.MOV": "1FYkZDJqGDE7jATcutyNZOnG7Xrp4YqXz",
    "black hair 3c.MOV": "1cAXzit6VxX6YruIX15XFyXOL3klADfsV",
    "black hair 3d.MOV": "1lXfTAYto5mHr5OkQfsKsa4n4Fi5UJLLm",
    "black hair 3e.MOV": "1g8xx7OPdldJLZ5yq7LE-CW1rKfhFdE0m",
    "black hair 3f.MOV": "1OpSF23LJtdi6l3awVK6rw1hbSn6rGuKu",
    "black hair 3g.MOV": "1QDG1OipIu3zOAk6aFNkM9z8CFbplRgeD",
    "black hair 3h.MOV": "1mKykYgxz4RsWeD4NF8SzbpC_mG4QPMSo",
    "black hair 3j.MOV": "1Zy_hShwasSR_Mmn5ScYVkLcPVJPVzrAn",
}

# The bed track. It was hardcoded to week-5 and so went out on three Amy
# reels in a row before Avi caught it on 2026-11-08: "don't use the same
# music you have been for the past 3 reels. Use something upbeat." Pass
# --music on every build and check what the last post used first; the
# no-repeat rule in the concept log applies to this account too.
MUSIC_DEFAULT = "sketchbook-2024-08-01.ogg"   # playful/energetic, 128bpm
MUSIC_VOL = 0.55          # sits under the CTA's own voiceover without burying it
SPLIT_THRESHOLD = 7.0     # seconds; at or above this the clip becomes two posts

# Playwright needs this in the Higgsfield sandbox; see GOTCHAS.
SANDBOX_ENV = ("env -u PYTHONPATH HOME=/home/user TMPDIR=/home/user/tmp "
               "PLAYWRIGHT_BROWSERS_PATH=/home/user/pw-browsers")

W, H, FPS = 1080, 1920, 30
FIT = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1"


def run(cmd):
    subprocess.run(cmd, shell=isinstance(cmd, str), check=True)


def probe(path, stream="v:0", entries="format=duration"):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", stream,
         "-show_entries", entries, "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True)
    return out.stdout.strip()


def fetch(file_id, dest):
    dest = pathlib.Path(dest)
    if not dest.exists():
        run(["curl", "-sL", "-o", str(dest), DRIVE.format(file_id)])
    return dest


def build(clip, cta, cap_png, out, start=0.0, end=None, work=pathlib.Path("."),
          music=None):
    music = music or (REPO / "assets" / "audio" / MUSIC_DEFAULT)
    react = work / "_react.mp4"
    # No transpose: the rotation metadata is applied for us.
    cut = ["-ss", str(start)] + (["-to", str(end)] if end else [])
    run(["ffmpeg", "-v", "error", *cut, "-i", str(clip), "-i", str(cap_png),
         "-filter_complex", f"[0:v]{FIT}[v0];[v0][1:v]overlay=0:0[v]",
         "-map", "[v]", "-an", "-c:v", "libx264", "-preset", "medium",
         "-crf", "18", "-pix_fmt", "yuv420p", "-y", str(react)])

    # ALWAYS re-encode the CTA, with the same encoder settings as the reaction
    # clip above. Do not "optimise" this into a stream copy.
    #
    # On 2026-11-09 it was switched to -c copy, on the correct observation that
    # the CTA source is already 1080x1920 at 30fps. That broke the next build:
    # a stream copy keeps the SOURCE's timebase, the reaction clip carries the
    # encoder's, and concatenating two files with mismatched timebases under
    # -c copy produces garbage timestamps. The output had the right 813 frames
    # and claimed to be 29 minutes long. Nothing errors - it just silently
    # produces an unpostable file, which is the worst kind of bug to leave in
    # a pipeline that runs unattended.
    #
    # preset veryfast is the real fix for the original complaint: it takes
    # about 19s where medium took over a minute, which is what kept the
    # Cloudflare 502s killing this step and leaving a truncated _cta.mp4.
    cta_n = work / "_cta.mp4"
    run(["ffmpeg", "-v", "error", "-i", str(cta), "-vf", FIT,
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-ar", "44100", "-ac", "2", "-y", str(cta_n)])
    # Fail here, loudly, rather than three steps downstream. A killed encode
    # leaves a file with no moov atom; ffprobe then exits non-zero or returns
    # nothing, and the old code only found out at the concat.
    try:
        float(probe(cta_n, entries="format=duration"))
    except (subprocess.CalledProcessError, ValueError):
        raise RuntimeError(
            f"{cta_n} is truncated or unreadable - the encode was killed. "
            "Delete it and re-run; nothing upstream needs redoing.")

    # Reaction clips carry no audio; concat needs a matching layout.
    react_a = work / "_react_a.mp4"
    run(["ffmpeg", "-v", "error", "-f", "lavfi", "-t", probe(react),
         "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
         "-i", str(react), "-map", "1:v", "-map", "0:a", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-shortest", "-y", str(react_a)])

    lst = work / "_list.txt"
    lst.write_text(f"file '{react_a.name}'\nfile '{cta_n.name}'\n")
    joined = work / "_joined.mp4"
    run(["ffmpeg", "-v", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", "-y", str(joined)])

    # Sanity-check the join before the music goes on. A timebase mismatch
    # between the two inputs yields the right frames with nonsense timestamps,
    # and nothing upstream errors - see the CTA note above. Catch it here,
    # where the cause is still obvious.
    dur = float(probe(joined))
    expected = float(probe(react_a)) + float(probe(cta_n))
    if abs(dur - expected) > 1.0:
        raise RuntimeError(
            f"{joined} is {dur:.1f}s but its parts are {expected:.1f}s. The "
            "concat produced broken timestamps - the two inputs almost "
            "certainly have mismatched timebases. Re-encode both with the "
            "same settings rather than stream-copying either one.")

    run(["ffmpeg", "-v", "error", "-i", str(joined),
         "-stream_loop", "-1", "-i", str(music),
         "-filter_complex",
         f"[1:a]volume={MUSIC_VOL},atrim=0:{dur:.3f},afade=t=in:st=0:d=0.4,"
         f"afade=t=out:st={max(dur - 0.5, 0):.3f}:d=0.5[m];"
         f"[0:a][m]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac",
         "-b:a", "192k", "-ar", "44100", "-ac", "2", "-y", str(out)])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clip-id", required=True, help="Drive id of the reaction clip")
    ap.add_argument("--cta-id", default=CTA_IDS["cta 1.mp4"])
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--end", type=float, default=None)
    ap.add_argument("--line", action="append", required=True,
                    help="one overlay line; repeat the flag per line")
    ap.add_argument("--out", required=True)
    ap.add_argument("--work", default=".")
    ap.add_argument("--music", default=None,
                    help="bed track filename in assets/audio, or a full path. "
                         f"Defaults to {MUSIC_DEFAULT}. Pick one the last few "
                         "posts did not use.")
    a = ap.parse_args()

    music = None
    if a.music:
        music = pathlib.Path(a.music)
        if not music.exists():
            music = REPO / "assets" / "audio" / a.music
        if not music.exists():
            raise SystemExit(f"no such track: {a.music}")

    work = pathlib.Path(a.work)
    work.mkdir(parents=True, exist_ok=True)
    clip = fetch(a.clip_id, work / "_clip.mov")
    cta = fetch(a.cta_id, work / "_cta_src.mp4")

    dur = float(probe(clip))
    if a.end is None and a.start == 0.0 and dur >= SPLIT_THRESHOLD:
        print(f"NOTE: this clip is {dur:.2f}s, at or over the {SPLIT_THRESHOLD}s "
              f"threshold - it should become two posts split at {dur / 2:.4f}s.")

    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import amy_caption as AC
    cap = AC.caption_png(a.line, work / "_cap.png", w=W, h=H)

    out = build(clip, cta, cap, work / a.out, a.start, a.end, work, music)
    print(out, probe(out), "s")


if __name__ == "__main__":
    main()
