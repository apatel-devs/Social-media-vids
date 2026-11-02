"""
@dharmalock_omnipeace — the LOCK format, rebuilt 2026-11-02 by measuring a
real posted video frame by frame (Ambe Ma / Devi Mahatmyam 2, 12.0s, 30fps).

This replaces an earlier reconstruction that was built from a four-line prose
description and was wrong in every visual respect. Everything below is
measured off the reference, not invented:

  page            1080x1920, white
  top rule        y 0-9, #FFBD69
  header          band y 126-171 — app icon + DHARMA LOCK, rules either side
  struck line     EB Garamond 62px, band y 268-312, crossed by a wide X
  X strokes       #E0531F, 9px round caps, x 242-837 across y 254-321
  correction      EB Garamond 62px / 74px, bands y 382-445, 456-519
  reframe         EB Garamond Italic 47px / 61px, #B07223, y 564-676
  label           Poppins Bold 26px, .22em, #835628, band y 758-777
  body            EB Garamond 46px / 65px, paragraph gap 65px, y 828-1133
  closing         EB Garamond Italic 44px / 59px, y 1189-1295
  badge           pill 393x72 r36, fill #FFBC70, Poppins Bold, y 1346-1417
  footer          Poppins Bold 28px, #918C8B, y 1462-1487 — NEVER blurred
  bottom 430px    deliberately empty (platform UI sits there)

Timeline, measured at 10Hz off the reference:
  0.00-0.60  struck line fades in
  0.90-1.60  the two X strokes draw
  1.70-2.50  correction fades in
  2.50-3.30  reframe fades in
  3.70-4.40  the vault (label/body/closing/badge) fades in ALREADY BLURRED,
             with the lock and TAP TO UNLOCK over it
  5.50-6.20  unlock: blur lifts, lock vanishes
  6.20-12.0  hold

Ships SILENT — Avi adds a trending sound and posts natively.
"""
import pathlib, base64, subprocess, time, shutil

W, H = 1080, 1920
FPS = 30
DUR = 12.0

A = pathlib.Path("/home/claude/dl/assets")
SF = pathlib.Path("/home/claude/ref/fonts")
OUT = pathlib.Path("/home/claude/dl/out")
OUT.mkdir(parents=True, exist_ok=True)

INK = "#111111"
RULE = "#FFBD69"
STROKE = "#E0531F"
REFRAME = "#B07223"
LABEL_C = "#835628"
BADGE_BG = "#FFBC70"
BADGE_FG = "#4A2A08"
FOOT_C = "#918C8B"
LOCK_C = "#C2621A"

# timeline
T_STRUCK, D_STRUCK = 0.00, 0.60
T_X, D_X = 0.90, 0.70
T_CORR, D_CORR = 1.70, 0.80
T_REFR, D_REFR = 2.50, 0.80
T_VAULT, D_VAULT = 3.70, 0.70
T_OPEN, D_OPEN = 5.50, 0.70


def _b64(p, d=A):
    return base64.b64encode((d / p).read_bytes()).decode()


def _face(name, file, d, weight="400", style="normal"):
    return (f"@font-face{{font-family:'{name}';font-weight:{weight};"
            f"font-style:{style};src:url(data:font/ttf;base64,{_b64(file, d)}) "
            f"format('truetype');}}")


FONTS = "".join([
    _face("Pop", "Poppins-SemiBold.ttf", A, "600"),
    _face("Pop", "Poppins-Bold.ttf", A, "700"),
    _face("Ser", "EBGaramond.ttf", SF, "400"),
    _face("Ser", "EBGaramond-Italic.ttf", SF, "400", "italic"),
])
ICON = "data:image/png;base64," + _b64("logo.png")


def page(struck, correction, reframe, label, paragraphs, closing, badge,
         handle="@dharmalock_omnipeace", lock_wording="TAP TO UNLOCK"):
    corr = "".join(f"<div>{l}</div>" for l in correction)
    refr = "".join(f"<div>{l}</div>" for l in reframe)
    # NOT <p> — a <div> inside a <p> makes the parser close the <p> early and
    # the lines escape the paragraph's styling entirely.
    body = "".join(
        "<div class='para'>" + "".join(f"<div>{l}</div>" for l in para)
        + "</div>" for para in paragraphs)
    clos = "".join(f"<div>{l}</div>" for l in closing)
    return f"""<html><head><meta charset='utf-8'><style>
{FONTS}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
body{{background:#fff;color:{INK};position:relative;overflow:hidden;
      font-family:'Ser',serif;text-align:center;}}
/* Nothing animates until the recorder adds .go to <body>. Without this the
   capture starts before the webfonts have painted and the DHARMA LOCK
   wordmark pops in a frame or two late — the banner has to be constant and
   outside every transition. */
/* !important is load-bearing: every animated rule here uses the `animation`
   shorthand, which resets animation-play-state to `running` and would
   otherwise win the cascade over a plain paused declaration. */
body:not(.go) *{{animation-play-state:paused !important;}}
@keyframes fin{{from{{opacity:0;}}to{{opacity:1;}}}}
@keyframes vfin{{from{{opacity:0;}}to{{opacity:.6;}}}}
@keyframes fout{{to{{opacity:0;visibility:hidden;}}}}
@keyframes draw{{to{{stroke-dashoffset:0;}}}}
@keyframes unlock{{to{{filter:blur(0);opacity:1;}}}}

.rule{{position:absolute;left:0;right:0;top:0;height:10px;background:{RULE};}}

.hd{{position:absolute;left:0;right:0;top:118px;display:flex;
     align-items:center;justify-content:center;gap:22px;}}
.hd .dash{{width:48px;height:3px;background:{RULE};}}
.hd img{{width:52px;height:52px;}}
.hd span{{font-family:'Pop';font-weight:700;font-size:31px;letter-spacing:.19em;
          color:#1b1b1b;}}

.col{{position:absolute;left:80px;right:80px;top:256px;}}

.struckwrap{{position:relative;display:inline-block;
             opacity:0;animation:fin {D_STRUCK}s ease forwards;
             animation-delay:{T_STRUCK}s;}}
.struck{{font-size:62px;line-height:1.0;white-space:nowrap;}}
svg.x{{position:absolute;left:-26px;top:-7px;width:calc(100% + 52px);
       height:calc(100% + 14px);overflow:visible;}}
svg.x line{{stroke:{STROKE};stroke-width:9;stroke-linecap:round;
            stroke-dasharray:1200;stroke-dashoffset:1200;
            animation:draw {D_X}s ease forwards;}}
svg.x line.b{{animation-delay:{T_X + 0.18:.2f}s;}}
svg.x line.a{{animation-delay:{T_X:.2f}s;}}

.corr{{font-size:62px;line-height:74px;margin-top:49px;
       opacity:0;animation:fin {D_CORR}s ease forwards;
       animation-delay:{T_CORR}s;}}
.refr{{font-style:italic;font-size:47px;line-height:61px;color:{REFRAME};
       margin-top:36px;opacity:0;animation:fin {D_REFR}s ease forwards;
       animation-delay:{T_REFR}s;}}

/* the vault arrives already blurred, then unlocks */
.vault{{margin-top:76px;opacity:0;filter:blur(15px);
        animation:vfin {D_VAULT}s ease forwards,
                  unlock {D_OPEN}s ease forwards;
        animation-delay:{T_VAULT}s,{T_OPEN}s;}}
.lbl{{font-family:'Pop';font-weight:700;font-size:26px;letter-spacing:.22em;
      color:{LABEL_C};}}
.bd .para{{font-size:46px;line-height:65px;margin-top:25px;}}
.bd .para + .para{{margin-top:65px;}}
.clos{{font-style:italic;font-size:44px;line-height:59px;margin-top:37px;}}
.badge{{display:inline-block;margin-top:53px;background:{BADGE_BG};
        color:{BADGE_FG};font-family:'Pop';font-weight:700;font-size:27px;
        letter-spacing:.10em;padding:16px 44px;border-radius:40px;}}

.foot{{position:absolute;left:0;right:0;top:1455px;font-family:'Pop';
       font-weight:700;font-size:28px;letter-spacing:.08em;color:{FOOT_C};}}

.lock{{position:absolute;left:0;right:0;top:862px;z-index:5;
       opacity:0;animation:fin {D_VAULT}s ease forwards,
                           fout {D_OPEN * 0.6:.2f}s ease forwards;
       animation-delay:{T_VAULT}s,{T_OPEN}s;}}
.lock img{{width:86px;height:86px;}}
.lock .w{{margin-top:22px;font-family:'Pop';font-weight:700;font-size:34px;
          letter-spacing:.18em;color:{LOCK_C};}}
</style></head><body>

<div class='rule'></div>
<div class='hd'><i class='dash'></i><img src='{ICON}'>
  <span>DHARMA LOCK</span><i class='dash'></i></div>

<div class='col'>
  <div class='struckwrap'>
    <div class='struck'>{struck}</div>
    <svg class='x' viewBox='0 0 600 100' preserveAspectRatio='none'>
      <line class='a' x1='4' y1='8' x2='596' y2='92'/>
      <line class='b' x1='4' y1='92' x2='596' y2='8'/>
    </svg>
  </div>
  <div class='corr'>{corr}</div>
  <div class='refr'>{refr}</div>
  <div class='vault lit'>
    <div class='lbl'>{label}</div>
    <div class='bd'>{body}</div>
    <div class='clos'>{clos}</div>
    <div><span class='badge'>{badge}</span></div>
  </div>
</div>

<div class='lock'><img src='{ICON}'><div class='w'>{lock_wording}</div></div>
<div class='foot'>{handle}</div>

</body></html>"""


def _settle(pg):
    """Block until the fonts are loaded AND two frames have actually been
    composited, so the static chrome is fully painted before anything moves."""
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(250)
    pg.evaluate("new Promise(r=>requestAnimationFrame("
                "()=>requestAnimationFrame(r)))")


def shot(html, path, at_s):
    """Screenshot the page at a given point on its own timeline."""
    from playwright.sync_api import sync_playwright
    tmp = OUT / "_o.html"
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H},
                        device_scale_factor=1)
        pg.goto(f"file://{tmp}")
        _settle(pg)
        pg.evaluate("document.body.classList.add('go')")
        pg.wait_for_timeout(int(at_s * 1000) + 120)
        pg.screenshot(path=str(path))
        b.close()
    return path


def record(html, path, dur=DUR):
    from playwright.sync_api import sync_playwright
    tmp = OUT / "_o.html"
    tmp.write_text(html, encoding="utf-8")
    raw = OUT / "_oraw"
    if raw.exists():
        shutil.rmtree(raw)
    raw.mkdir(parents=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": W, "height": H},
                            record_video_dir=str(raw),
                            record_video_size={"width": W, "height": H})
        pg = ctx.new_page()
        t0 = time.time()
        pg.goto("about:blank")
        pg.wait_for_timeout(260)
        pg.goto(f"file://{tmp}")
        _settle(pg)
        # everything above this line is the settled, static page; the clip
        # starts here, so frame 0 already has the banner on it
        nav = time.time() - t0
        pg.evaluate("document.body.classList.add('go')")
        pg.wait_for_timeout(int(dur * 1000) + 900)
        ctx.close()
        b.close()
    src = next(raw.glob("*.webm"))
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
        "-ss", f"{min(max(nav,0.05),1.5):.3f}", "-t", f"{dur:.3f}",
        "-r", str(FPS), "-vsync", "cfr",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(path)
    ], check=True)
    shutil.rmtree(raw)
    return path
