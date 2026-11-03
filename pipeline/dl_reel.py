"""
@dharmalockapp Instagram reel template — measured 2026-11-03 off the real
posted reel (Karwa Chauth, 1080x1920, 25fps, 19.92s) plus the committed
reels in videos/.

The reel is NOT the carousel scaled up. Measured differences:
  page        pure white (the 4:5 carousel page is cream #FFFDF9)
  margin      56 for the header, the card itself sits x32-1050
  card        y300-1478, radius 34, temple cropped into its bottom-right
  header      y76-123, icon 52px, DHARMA LOCK 33px, handle 29px
  hook        Anton 94px / 94px, last line rust; italic subline 40px;
              outlined pill bottom-LEFT and "check it out ->" bottom-RIGHT,
              both inside the card. There is no body paragraph on the reel.
  verse       source 23px .25em, Anton title 48px rust, ref, gold rule,
              gloss 26px italic, phone mockup below the card
  closing     Anton 78px question with a short rust rule, no CTA poster —
              the reel ENDS on the question card
  joins       HARD CUTS between slides, never a crossfade. Each slide plays
              its own entrance animation; that is what carries the motion.
  durations   hook 2.84s, content slides ~4.2s (measured cut points
              2.84 / 6.88 / 11.28 / 15.68 / 19.92)
"""
import pathlib, base64, subprocess, time, shutil

A = pathlib.Path("/home/claude/smv/assets")
OUT = pathlib.Path("/home/claude/out")
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1920
FPS = 25
D_HOOK, D_SLIDE = 2.84, 4.20

INK = "#18120D"
RUST = "#C1440E"
MUTED = "#8A8178"
GOLD = "#E8C98A"
SUBGREY = "#5C564E"


def _b64(p):
    return base64.b64encode((A / p).read_bytes()).decode()


def _face(n, f, w="400", s="normal"):
    return (f"@font-face{{font-family:'{n}';font-weight:{w};font-style:{s};"
            f"src:url(data:font/ttf;base64,{_b64(f)}) format('truetype');}}")


FONTS = "".join([
    _face("Pop", "Poppins-Medium.ttf", "500"),
    _face("Pop", "Poppins-Bold.ttf", "700"),
    _face("PopI", "Poppins-MediumItalic.ttf", "500", "italic"),
    _face("Anton", "Anton-Regular.ttf", "400"),
    _face("Deva", "NotoSansDevanagari-Bold.ttf", "700"),
])
ICON = "data:image/png;base64," + _b64("logo.png")
TEMPLE = "data:image/png;base64," + _b64("temple_real.png")
PHONE = "data:image/png;base64," + _b64("phone_verse_base_full2.png")

CSS = f"""
{FONTS}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{H}px;}}
body{{background:#fff;color:{INK};font-family:'Pop',sans-serif;
      position:relative;overflow:hidden;}}
body:not(.go) *{{animation-play-state:paused !important;}}
@keyframes rise{{from{{opacity:0;transform:translateY(30px);}}
                 to{{opacity:1;transform:translateY(0);}}}}
@keyframes fin{{from{{opacity:0;}}to{{opacity:1;}}}}
@keyframes up{{from{{opacity:0;transform:translateY(70px);}}
               to{{opacity:1;transform:translateY(0);}}}}
.an{{opacity:0;animation:rise .55s cubic-bezier(.22,.9,.3,1) forwards;}}
.af{{opacity:0;animation:fin .5s ease forwards;}}
.ap{{opacity:0;animation:up .7s cubic-bezier(.22,.9,.3,1) forwards;}}

.hdr{{position:absolute;left:56px;right:50px;top:70px;display:flex;
      align-items:center;gap:18px;}}
.hdr img{{width:52px;height:52px;}}
.hdr .nm{{font-weight:700;font-size:33px;letter-spacing:.10em;}}
.hdr .hd{{margin-left:auto;font-weight:500;font-size:29px;color:{MUTED};}}

.card{{position:absolute;left:32px;right:30px;top:300px;height:1178px;
       background:#fff;border-radius:34px;overflow:hidden;
       box-shadow:0 22px 60px rgba(70,46,18,.10);}}
.tcrop{{position:absolute;right:0;bottom:0;width:330px;height:430px;
        overflow:hidden;}}
.tcrop img{{width:100%;height:100%;object-fit:cover;object-position:62% 50%;
            opacity:.5;mix-blend-mode:multiply;}}
.pad{{position:relative;z-index:2;padding:92px 56px 0;}}

.head{{font-family:'Anton';font-size:94px;line-height:94px;
       text-transform:uppercase;}}
.head .o{{color:{RUST};}}
.sub{{font-family:'PopI';font-style:italic;font-size:40px;line-height:52px;
      color:{SUBGREY};margin-top:50px;}}

.btm{{position:absolute;left:56px;right:56px;bottom:56px;z-index:3;
      display:flex;align-items:center;}}
.pill{{border:3px solid {RUST};color:{RUST};font-weight:700;font-size:28px;
       letter-spacing:.06em;text-transform:uppercase;padding:14px 24px;
       border-radius:8px;}}
.cta{{margin-left:auto;color:{RUST};font-weight:700;font-size:32px;}}

.vsrc{{text-align:center;font-weight:700;font-size:23px;letter-spacing:.25em;
       text-transform:uppercase;}}
.vtitle{{text-align:center;font-family:'Anton';font-size:48px;line-height:58px;
         color:{RUST};text-transform:uppercase;margin-top:22px;
         transform:skewX(-8deg);}}
.vref{{text-align:center;font-weight:700;font-size:22px;letter-spacing:.10em;
       color:{MUTED};margin-top:20px;}}
.vrule{{width:64px;height:4px;background:{GOLD};margin:20px auto 0;}}
.vgloss{{text-align:center;font-family:'PopI';font-style:italic;font-size:26px;
         line-height:36px;margin-top:22px;}}

.phone{{position:absolute;left:-200px;top:166px;width:1480px;}}
.screen{{position:absolute;left:262px;width:504px;top:1054px;background:#fff;
         border-radius:22px;padding:22px 24px;text-align:center;}}
.screen .dev{{font-family:'Deva';font-weight:700;font-size:33px;
              line-height:1.62;}}
.screen .srule{{width:46px;height:3px;background:{GOLD};margin:13px auto;}}
.screen .tl{{font-family:'PopI';font-style:italic;font-size:26px;
             line-height:1.45;color:#4A423A;}}
.screen .tr{{font-size:25px;line-height:1.45;color:#6B6258;margin-top:15px;}}

.q{{font-family:'Anton';font-size:78px;line-height:85px;
    text-transform:uppercase;}}
.q .o{{color:{RUST};}}
.qrule{{width:72px;height:5px;background:{RUST};margin-top:30px;}}
"""


def _hdr():
    return (f"<div class='hdr'><img src='{ICON}'>"
            f"<span class='nm'>DHARMA LOCK</span>"
            f"<span class='hd'>@dharmalockapp</span></div>")


def _doc(body):
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head>"
            f"<body>{_hdr()}{body}</body></html>")


def hook(head_lines, sub, pill, cta="check it out &rarr;"):
    head = "".join(f"<div class='{'o' if o else ''}'>{t}</div>"
                   for t, o in head_lines)
    return _doc(
        f"<div class='card af'><div class='tcrop'><img src='{TEMPLE}'></div>"
        f"<div class='pad'><div class='head an' style='animation-delay:.14s'>{head}</div>"
        f"<div class='sub an' style='animation-delay:.46s'>{sub}</div></div>"
        f"<div class='btm an' style='animation-delay:.66s'>"
        f"<span class='pill'>{pill}</span><span class='cta'>{cta}</span></div>"
        f"</div>")


def verse(source, title, reference, gloss, devanagari, translit, translation):
    g = "".join(f"<div>{l}</div>" for l in gloss)
    dev = "<br>".join(devanagari)
    return _doc(
        f"<img class='phone ap' style='animation-delay:.52s' src='{PHONE}'>"
        f"<div class='card af' style='height:640px'>"
        f"<div class='pad' style='padding-top:72px'>"
        f"<div class='vsrc an'>{source}</div>"
        f"<div class='vtitle an' style='animation-delay:.16s'>&ldquo;{title}&rdquo;</div>"
        f"<div class='vref an' style='animation-delay:.28s'>{reference}</div>"
        f"<div class='vrule'></div>"
        f"<div class='vgloss an' style='animation-delay:.36s'>{g}</div>"
        f"</div></div>"
        f"<div class='screen ap' style='animation-delay:.62s'>"
        f"<div class='dev'>{dev}</div><div class='srule'></div>"
        f"<div class='tl'>{translit}</div>"
        f"<div class='tr'>{translation}</div></div>")


def closing(q_lines):
    q = "".join(f"<div class='{'o' if o else ''}'>{t}</div>" for t, o in q_lines)
    return _doc(
        f"<div class='card af'><div class='tcrop'><img src='{TEMPLE}'></div>"
        f"<div class='pad' style='padding-top:490px'>"
        f"<div class='q an' style='animation-delay:.16s'>{q}</div>"
        f"<div class='qrule af' style='animation-delay:.6s'></div></div></div>")


def _settle(pg):
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(260)
    pg.evaluate("new Promise(r=>requestAnimationFrame("
                "()=>requestAnimationFrame(r)))")


def shot(html, path, at_s=2.4):
    from playwright.sync_api import sync_playwright
    tmp = OUT / "_r.html"
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto(f"file://{tmp}")
        _settle(pg)
        pg.evaluate("document.body.classList.add('go')")
        pg.wait_for_timeout(int(at_s * 1000))
        pg.screenshot(path=str(path))
        b.close()
    return path


def clip(html, path, dur):
    from playwright.sync_api import sync_playwright
    tmp = OUT / "_r.html"
    tmp.write_text(html, encoding="utf-8")
    raw = OUT / "_raw"
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
        pg.wait_for_timeout(240)
        pg.goto(f"file://{tmp}")
        _settle(pg)
        nav = time.time() - t0
        pg.evaluate("document.body.classList.add('go')")
        pg.wait_for_timeout(int(dur * 1000) + 900)
        ctx.close()
        b.close()
    src = next(raw.glob("*.webm"))
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
        "-ss", f"{min(max(nav,0.05),1.6):.3f}", "-t", f"{dur:.3f}",
        "-r", str(FPS), "-vsync", "cfr", "-c:v", "libx264", "-preset", "medium",
        "-crf", "18", "-pix_fmt", "yuv420p", str(path)
    ], check=True)
    shutil.rmtree(raw)
    return path


def join(clips, out):
    """Hard cuts — the reference reel has no crossfades between slides."""
    lst = OUT / "_list.txt"
    lst.write_text("".join(f"file '{c}'\n" for c in clips))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat",
                    "-safe", "0", "-i", str(lst), "-c", "copy",
                    "-movflags", "+faststart", str(out)], check=True)
    return out


def music(video, track, out, volume=0.6, fade=1.0):
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                              "format=duration", "-of", "csv=p=0", str(video)],
                             capture_output=True, text=True,
                             check=True).stdout.strip())
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(video),
        "-stream_loop", "-1", "-i", str(track), "-filter_complex",
        f"[1:a]atrim=0:{d:.3f},asetpts=N/SR/TB,volume={volume},"
        f"afade=t=out:st={max(d-fade,0):.3f}:d={fade}[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac",
        "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)
    ], check=True)
    return out
