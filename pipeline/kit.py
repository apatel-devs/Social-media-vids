"""
Dharma Lock card + video kit — rebuilt 2026-11-02 against the recorded spec.

Spec this follows (from the project's own standing rules, not invented):
  NATIVE_FPS = 25 everywhere. Playwright records true CFR 25; forcing 30
  duplicates frames and causes the stutter that got the 10/09 post deleted.
  HOOK 1.8s / VERSE 4.0s / CTA 2.8s. Cover frame ~1150ms.
  stitch uses slideleft, never fade (near-identical cards ghost on a dissolve).
  Entrance animations are the point — record the page, don't screenshot it.
  Music mixes at volume 0.6 with a 1.0s fade-out, AAC 192k, IG only.
"""
import pathlib, base64, subprocess, time, shutil, json

W, H = 1080, 1920
NATIVE_FPS = 25
HOOK_DURATION = 1.8
VERSE_DURATION = 4.0
DIALOGUE_DURATION = 4.0
CTA_DURATION = 2.8
COVER_MS = 1150

A = pathlib.Path("/home/claude/dl/assets")
OUT = pathlib.Path("/home/claude/dl/out")
OUT.mkdir(parents=True, exist_ok=True)

CREAM = "#FBF4E9"
INK = "#1A1208"
ORANGE = "#E2691C"
ORANGE_D = "#B8500F"
MUTED = "#6B5B45"


def _b64(p):
    return base64.b64encode((A / p).read_bytes()).decode()


def _face(name, file, weight="400", style="normal"):
    return (f"@font-face{{font-family:'{name}';font-weight:{weight};"
            f"font-style:{style};src:url(data:font/ttf;base64,{_b64(file)}) "
            f"format('truetype');}}")


FONTS = "".join([
    _face("Pop", "Poppins-Medium.ttf", "500"),
    _face("Pop", "Poppins-SemiBold.ttf", "600"),
    _face("Pop", "Poppins-Bold.ttf", "700"),
    _face("Pop", "Poppins-Black.ttf", "900"),
    _face("PopI", "Poppins-MediumItalic.ttf", "500", "italic"),
    _face("Anton", "Anton-Regular.ttf", "400"),
    _face("Deva", "NotoSansDevanagari-Bold.ttf", "700"),
])

LOGO = "data:image/png;base64," + _b64("logo.png")
PHONE = "data:image/png;base64," + _b64("phone_verse_base_full2.png")
CTA_IMG = "data:image/jpeg;base64," + _b64("cta_full_poster.jpg")

BASE = """
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:%dpx;height:%dpx;}
body{background:%s;color:%s;font-family:'Pop',sans-serif;
     position:relative;overflow:hidden;}
.blob{position:absolute;border-radius:50%%;background:%s;opacity:.10;}
.b1{width:760px;height:760px;left:-300px;top:-240px;}
.b2{width:620px;height:620px;right:-280px;bottom:-240px;}
.pad{position:absolute;inset:0;padding:96px 88px;z-index:2;
     display:flex;flex-direction:column;}
.badge{align-self:flex-start;background:%s;color:#fff;font-weight:700;
       font-size:27px;letter-spacing:.14em;text-transform:uppercase;
       padding:15px 28px;border-radius:999px;}
.foot{position:absolute;left:88px;right:88px;bottom:72px;z-index:4;
      display:flex;align-items:center;gap:18px;}
.foot img{width:62px;height:62px;border-radius:16px;}
.foot .nm{font-weight:700;font-size:29px;}
.foot .hd{margin-left:auto;font-size:26px;color:%s;font-weight:500;}
.count{position:absolute;top:104px;right:88px;z-index:4;font-weight:700;
       font-size:28px;color:%s;letter-spacing:.08em;}
/* Nothing moves until the recorder adds .go to <body>, so the clip never
   starts mid-paint. !important is load-bearing: the `animation` shorthand
   used below resets animation-play-state to `running`. */
body:not(.go) *{animation-play-state:paused !important;}
@keyframes rise{from{opacity:0;transform:translateY(34px);}
                to{opacity:1;transform:translateY(0);}}
@keyframes fadein{from{opacity:0;}to{opacity:1;}}
.an{opacity:0;animation:rise .52s cubic-bezier(.22,.9,.3,1) forwards;}
.af{opacity:0;animation:fadein .55s ease forwards;}
""" % (W, H, CREAM, INK, ORANGE, ORANGE, MUTED, MUTED)


def _doc(body, extra=""):
    return ("<html><head><meta charset='utf-8'><style>"
            f"{FONTS}{BASE}{extra}</style></head><body>"
            "<div class='blob b1'></div><div class='blob b2'></div>"
            f"{body}</body></html>")


def _foot():
    return (f"<div class='foot af' style='animation-delay:.55s'>"
            f"<img src='{LOGO}'><span class='nm'>Dharma Lock</span>"
            f"<span class='hd'>@dharmalockapp</span></div>")


# ---------------------------------------------------------------- hook card
def build_hook_anim(badge, big_lines, small):
    big = "".join(
        f"<div class='an' style='animation-delay:{.12+i*.09:.2f}s'>{l}</div>"
        for i, l in enumerate(big_lines))
    extra = """
    .mid{margin:auto 0;}
    .big{font-family:'Anton';font-size:112px;line-height:1.04;
         letter-spacing:-.012em;text-transform:uppercase;}
    .big div:last-child{color:%s;}
    .small{font-family:'PopI';font-style:italic;font-size:41px;line-height:1.42;
           color:%s;margin-top:42px;max-width:850px;}
    """ % (ORANGE_D, MUTED)
    body = (f"<div class='pad'>"
            f"<span class='badge an'>{badge}</span>"
            f"<div class='mid'><div class='big'>{big}</div>"
            f"<div class='small an' style='animation-delay:.46s'>{small}</div>"
            f"</div></div>{_foot()}")
    return _doc(body, extra)


# --------------------------------------------------------------- verse card
def build_verse_anim(label, gloss, devanagari, translit, translation, n, total):
    dev = "<br>".join(devanagari)
    # phone png is 1080x1350; scaled 1.42x and bottom-anchored so the screen
    # interior is a ~600px column the verse can actually be read in.
    extra = """
    /* phone png is 1080x1350 natural, scaled 1.45 and pinned bottom:-230.
       Everything below is derived from that: image left -243, top 192.5,
       so the screen's usable column is x 245..770 and the text must start
       BELOW the png's own "today's scripture" label at y~1109. */
    .top{position:absolute;left:88px;right:88px;top:400px;}
    .lbl{font-weight:700;font-size:27px;letter-spacing:.16em;color:%s;
         text-transform:uppercase;}
    .gloss{font-family:'Anton';font-size:70px;line-height:1.08;
           text-transform:uppercase;margin-top:16px;letter-spacing:-.01em;}
    /* the png ships on an opaque white field that would otherwise cover the
       whole page; multiply drops the white and keeps the dark phone body.
       It has to sit on the wrapper with NO z-index — a z-index would make
       the wrapper its own stacking context and the blend would have nothing
       but transparency behind it. */
    .phonewrap{position:absolute;left:50%%;bottom:-230px;width:1566px;
               height:1958px;margin-left:-783px;mix-blend-mode:multiply;}
    .phonewrap img{width:100%%;height:100%%;object-fit:contain;}
    .screen{position:absolute;left:245px;width:525px;top:1150px;z-index:3;}
    .san{font-family:'Deva';font-weight:700;font-size:30px;line-height:1.64;
         color:%s;}
    .tl{font-family:'PopI';font-style:italic;font-size:23px;line-height:1.46;
        color:%s;margin-top:18px;}
    .tr{font-size:27px;line-height:1.46;margin-top:20px;font-weight:500;}
    """ % (ORANGE_D, INK, MUTED)
    body = (
        f"<div class='count'>{n} / {total}</div>"
        f"<div class='phonewrap af' style='animation-delay:.28s'>"
        f"<img src='{PHONE}'></div>"
        f"<div class='screen an' style='animation-delay:.5s'>"
        f"<div class='san'>{dev}</div>"
        f"<div class='tl'>{translit}</div>"
        f"<div class='tr'>{translation}</div></div>"
        f"<div class='pad'><div class='top'>"
        f"<div class='lbl an'>{label}</div>"
        f"<div class='gloss an' style='animation-delay:.14s'>{gloss}</div>"
        f"</div></div>")
    return _doc(body, extra)


# ------------------------------------------------------------ YOUR TURN card
def build_dialogue_anim(tag, quote, sub=""):
    extra = """
    .mid{margin:auto 0;}
    .tag{align-self:flex-start;border:3px solid %s;color:%s;font-weight:700;
         font-size:25px;letter-spacing:.18em;text-transform:uppercase;
         padding:13px 26px;border-radius:999px;}
    .q{font-family:'Anton';font-size:86px;line-height:1.1;margin-top:0;
       text-transform:uppercase;letter-spacing:-.012em;}
    .q em{color:%s;font-style:normal;}
    .sub{font-family:'PopI';font-style:italic;font-size:38px;line-height:1.42;
         color:%s;margin-top:36px;max-width:840px;}
    """ % (ORANGE, ORANGE_D, ORANGE_D, MUTED)
    subhtml = (f"<div class='sub an' style='animation-delay:.42s'>{sub}</div>"
               if sub else "")
    body = (f"<div class='pad'><span class='tag an'>{tag}</span>"
            f"<div class='mid'><div class='q an' "
            f"style='animation-delay:.18s'>{quote}</div>{subhtml}</div>"
            f"</div>{_foot()}")
    return _doc(body, extra)


# ----------------------------------------------------------------- CTA card
def build_cta_anim():
    extra = """
    .cta{position:absolute;inset:0;z-index:1;}
    .cta img{width:100%;height:100%;object-fit:cover;}
    """
    body = (f"<div class='cta af'><img src='{CTA_IMG}'></div>")
    return _doc(body, extra)


# ------------------------------------------------------------------ capture
def capture_png(html, out_path, settle_s=1.5):
    from playwright.sync_api import sync_playwright
    tmp = OUT / "_c.html"
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H},
                        device_scale_factor=1)
        pg.goto(f"file://{tmp}")
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(int(settle_s * 1000)); pg.evaluate("document.body.classList.add('go')"); pg.wait_for_timeout(int(settle_s * 1000))
        pg.screenshot(path=str(out_path))
        b.close()
    return out_path


def record_slide(html, duration_s, out_path):
    """Record the page so the CSS entrance animation is in the clip.

    Warm the compositor on a blank page first, measure how much warm-up video
    landed before the real content was set, and trim exactly that — never a
    flat skip, which is what ate the entrance animations in the 10/08 build.
    """
    from playwright.sync_api import sync_playwright
    tmp = OUT / "_r.html"
    tmp.write_text(html, encoding="utf-8")
    raw_dir = OUT / "_raw"
    if raw_dir.exists():
        shutil.rmtree(raw_dir)
    raw_dir.mkdir(parents=True)

    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": W, "height": H},
                            record_video_dir=str(raw_dir),
                            record_video_size={"width": W, "height": H})
        pg = ctx.new_page()
        t0 = time.time()
        pg.goto("about:blank")
        pg.wait_for_timeout(260)          # warm compositor
        pg.goto(f"file://{tmp}")
        # wait for fonts AND two composited frames, so the clip's frame 0 is
        # the settled page rather than a half-painted one
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(250)
        pg.evaluate("new Promise(r=>requestAnimationFrame("
                    "()=>requestAnimationFrame(r)))")
        nav = time.time() - t0
        pg.evaluate("document.body.classList.add('go')")
        pg.wait_for_timeout(int(duration_s * 1000) + 900)
        ctx.close()
        b.close()

    raw = next(raw_dir.glob("*.webm"))
    # trim to the measured navigation point, never a flat guess — a skip long
    # enough to be "safe" is long enough to eat the entrance animation.
    skip = min(max(nav, 0.05), 1.5)
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(raw),
        "-ss", f"{skip:.3f}", "-t", f"{duration_s:.3f}",
        "-r", str(NATIVE_FPS), "-vsync", "cfr",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-pix_fmt", "yuv420p", str(out_path)
    ], check=True)
    shutil.rmtree(raw_dir)
    return out_path


def stitch_clips(clips, out_path, xfade=0.4):
    """slideleft only — a plain fade ghosts between near-identical cards."""
    durs = []
    for c in clips:
        d = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                            "format=duration", "-of", "csv=p=0", str(c)],
                           capture_output=True, text=True, check=True)
        durs.append(float(d.stdout.strip()))
    parts, offset = [], durs[0] - xfade
    fc = "".join(f"[{i}:v]fps={NATIVE_FPS},format=yuv420p,setsar=1[v{i}];"
                 for i in range(len(clips)))
    cur = "[v0]"
    for i in range(1, len(clips)):
        lab = f"[x{i}]"
        fc += (f"{cur}[v{i}]xfade=transition=slideleft:duration={xfade}"
               f":offset={offset:.3f}{lab};")
        cur = lab
        offset += durs[i] - xfade
    fc = fc.rstrip(";")
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for c in clips:
        cmd += ["-i", str(c)]
    cmd += ["-filter_complex", fc, "-map", cur,
            "-r", str(NATIVE_FPS), "-c:v", "libx264", "-preset", "medium",
            "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            str(out_path)]
    subprocess.run(cmd, check=True)
    return out_path


def add_background_music(video, track, out_path, volume=0.6, fade_dur=1.0):
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of", "csv=p=0", str(video)],
                             capture_output=True, text=True,
                             check=True).stdout.strip())
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(video),
        "-stream_loop", "-1", "-i", str(track),
        "-filter_complex",
        f"[1:a]atrim=0:{d:.3f},asetpts=N/SR/TB,volume={volume},"
        f"afade=t=out:st={max(d-fade_dur,0):.3f}:d={fade_dur}[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-shortest",
        "-movflags", "+faststart", str(out_path)
    ], check=True)
    return out_path
