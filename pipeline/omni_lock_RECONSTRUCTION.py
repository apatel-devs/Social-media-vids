"""
@dharmalock_omnipeace — Ekalavya, 2026-11-02. SILENT (Avi adds a trending
sound in-app and posts it himself; this account does not go through Post
Bridge).

Format is the account's standing one, per the recorded spec:
  * the myth line crossed out with TWO hand-scored crossing strokes — not a
    strikethrough, not an exact X
  * the correction under it
  * the rest of the page withheld behind a blur and a lock
  * the lock wording is "TAP TO UNLOCK", never "pray to unlock"
  * every cover is the locked frame, so frame 0 is the locked state
  * white page, the app's own orange on top, Dharma Lock mark present —
    "simple" means the COPY, not the branding
  * no deity/fairy motion
Copy written to the plain-language bar: short lines, spoken words.
"""
import sys, pathlib, base64, subprocess, time, shutil
sys.path.insert(0, "/home/claude/dl")
import kit as K

W, H = 1080, 1920
ORANGE = "#E2691C"
ORANGE_D = "#B8500F"
INK = "#15100A"
MUTED = "#6E6257"

STRUCK = "Ekalavya gave his thumb out of respect."
CORRECT = "He gave it up because the teacher who refused to teach him still came to collect."

LINES = [
    "They would not let him in the room.",
    "So he built a statue of the teacher who said no, stood in front of it, and taught himself.",
    "He got better than everyone who was allowed inside.",
    "That is when they came for the thumb.",
]

VERSE_LABEL = "BHAGAVAD GITA 6.5"
VERSE = ("Pull yourself up. Don't let yourself sink. "
         "You are your own best friend, and your own worst enemy.")

CLOSING = "Nobody is coming to teach you. Start in front of the statue."

LOCK_WORDING = "TAP TO UNLOCK"

# timeline (seconds). The locked state has to actually EXIST long enough to
# be a cover — strokes land ~1.1s, correction ~1.9s, and the lock does not
# open until 3.4s, leaving ~1.5s of the true locked frame.
T_STRIKE = 0.45     # strokes start drawing
T_OPEN = 3.40       # lock opens, blur lifts
T_BODY = 3.85       # body lines begin arriving
DUR = 13.0


def html():
    lines = "".join(f"<p class='ln'>{t}</p>" for t in LINES)
    return f"""<html><head><meta charset='utf-8'><style>
{K.FONTS}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
body{{background:#fff;color:{INK};font-family:'Pop',sans-serif;
      position:relative;overflow:hidden;}}

.bar{{position:absolute;left:0;right:0;top:0;height:170px;background:{ORANGE};
      display:flex;align-items:center;padding:0 72px;gap:22px;z-index:6;}}
.bar img{{width:78px;height:78px;border-radius:19px;}}
.bar .nm{{color:#fff;font-weight:700;font-size:38px;letter-spacing:.01em;}}
.bar .hd{{margin-left:auto;color:#FFE4CE;font-size:28px;font-weight:600;}}

.page{{position:absolute;left:0;right:0;top:170px;bottom:0;padding:92px 78px 0;}}

.struckwrap{{position:relative;display:inline-block;}}
.struck{{font-size:46px;line-height:1.3;font-weight:600;color:{MUTED};
         white-space:nowrap;}}
svg.score{{position:absolute;left:-20px;top:-10px;width:calc(100% + 40px);
           height:calc(100% + 20px);overflow:visible;pointer-events:none;}}
svg.score path{{fill:none;stroke:{ORANGE};stroke-width:9;stroke-linecap:round;
                stroke-dasharray:1400;stroke-dashoffset:1400;
                animation:score .6s ease forwards;}}
svg.score path.s2{{animation-delay:{T_STRIKE+0.34:.2f}s;stroke-width:7;}}
svg.score path.s1{{animation-delay:{T_STRIKE:.2f}s;}}
@keyframes score{{to{{stroke-dashoffset:0;}}}}

.correct{{font-family:'Anton';font-size:76px;line-height:1.1;margin-top:46px;
          text-transform:uppercase;letter-spacing:-.01em;opacity:0;
          animation:rise .6s cubic-bezier(.22,.9,.3,1) forwards;
          animation-delay:{T_STRIKE+0.85:.2f}s;}}
.correct em{{color:{ORANGE_D};font-style:normal;}}

/* everything below the fold is withheld until the lock opens. The blur has
   to still READ as text behind glass — too much blur or too little opacity
   and the lower half just looks like an empty page. */
.vault{{margin-top:58px;filter:blur(13px);opacity:.9;
        animation:unblur .8s ease forwards;animation-delay:{T_OPEN:.2f}s;}}
@keyframes unblur{{to{{filter:blur(0);opacity:1;}}}}

/* The vault's contents are PRESENT from frame 0 — only blurred. They must be
   there for the locked cover to show "answer blurred" rather than a blank
   lower half, so nothing in here fades in on its own timer. */
@keyframes rise{{from{{opacity:0;transform:translateY(26px);}}
                 to{{opacity:1;transform:translateY(0);}}}}
.ln{{font-size:44px;line-height:1.46;margin-bottom:30px;}}
.vlabel{{font-weight:700;font-size:26px;letter-spacing:.16em;color:{ORANGE_D};
         text-transform:uppercase;margin-top:54px;}}
.verse{{font-family:'PopI';font-style:italic;font-size:46px;line-height:1.4;
        margin-top:16px;color:{INK};}}
.close{{font-family:'Anton';font-size:62px;line-height:1.14;margin-top:58px;
        text-transform:uppercase;color:{ORANGE_D};}}

/* the lock overlay — this is what the cover frame shows */
.lockwrap{{position:absolute;left:0;right:0;top:700px;bottom:0;z-index:5;
           display:flex;flex-direction:column;align-items:center;
           justify-content:flex-start;padding-top:230px;
           background:linear-gradient(180deg,rgba(255,255,255,0) 0%,
                      rgba(255,255,255,.42) 16%,rgba(255,255,255,.62) 100%);
           animation:vanish .5s ease forwards;animation-delay:{T_OPEN:.2f}s;}}
@keyframes vanish{{to{{opacity:0;visibility:hidden;}}}}
.lock{{width:150px;height:170px;position:relative;}}
.shackle{{position:absolute;left:33px;top:0;width:84px;height:84px;
          border:15px solid {ORANGE};border-bottom:none;
          border-radius:44px 44px 0 0;transform-origin:88% 100%;
          animation:pop .45s cubic-bezier(.3,1.5,.5,1) forwards;
          animation-delay:{T_OPEN-0.1:.2f}s;}}
@keyframes pop{{to{{transform:rotate(-26deg) translateY(-8px);}}}}
.body{{position:absolute;left:0;top:72px;width:150px;height:98px;
       background:{ORANGE};border-radius:22px;}}
.lw{{margin-top:34px;font-weight:700;font-size:34px;letter-spacing:.2em;
     color:{ORANGE_D};}}
</style></head><body>

<div class='bar'><img src='{K.LOGO}'>
  <span class='nm'>Dharma Lock</span>
  <span class='hd'>@dharmalock_omnipeace</span></div>

<div class='page'>
  <div class='struckwrap'>
    <div class='struck'>{STRUCK}</div>
    <svg class='score' viewBox='0 0 960 120' preserveAspectRatio='none'>
      <path class='s1' d='M10,74 C250,58 560,52 950,42'/>
      <path class='s2' d='M16,50 C290,66 600,74 946,80'/>
    </svg>
  </div>
  <div class='correct'>He gave it up because the teacher who refused him
    <em>still came to collect.</em></div>

  <div class='vault'>
    {lines}
    <div class='vlabel'>{VERSE_LABEL}</div>
    <div class='verse'>{VERSE}</div>
    <div class='close'>{CLOSING}</div>
  </div>
</div>

<div class='lockwrap'>
  <div class='lock'><div class='shackle'></div><div class='body'></div></div>
  <div class='lw'>{LOCK_WORDING}</div>
</div>

</body></html>"""


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "png"
    if mode == "png":
        K.capture_png(html(), K.OUT / "omni_locked.png", settle_s=2.6)
        K.capture_png(html(), K.OUT / "omni_open.png", settle_s=11.0)
        print("stills")
    else:
        out = K.OUT / "omnipeace_ekalavya_SILENT.mp4"
        K.record_slide(html(), DUR, out)
        print("recorded", out)
