"""
@dharmalockapp card template — rebuilt 2026-11-02 by measuring the real
finished cards committed in this repo under images/<slug>/, after a rebuild
from prose notes was rejected.

Ground truth used: images/gita_grief/{01_hook,02_verse,03_reflection}.png
and videos/*.mp4. Measured, not invented:

  carousel page   1080x1350 (4:5)  — NOT 9:16. The reel is 1080x1920 @25fps.
  page bg         #FFFDF9 cream (hook/reflection); the verse page is white
  margin          72px
  header          y 63-103 — lock icon + DHARMA LOCK left, @dharmalockapp right
  white card      x 72-1008, y 212-997, radius 28, soft shadow
                  (verse card sits high: y 57-613, phone mockup below it)
  brand rust      #C1440E   ink #18120D   muted #8A8178   rule #E8C98A
  headline        Anton 79px / 78px, black lines then rust lines
  hook chip       filled rust, white Poppins Bold 26px, .14em, radius 6
  body copy       Poppins 40px / 47px — OUTSIDE the card, on the cream
  source pill     outlined rust, radius 8, Poppins Bold 26px
  reflection      YOUR TURN chip, centred quote, short rust rule under it
  temple          temple_real.png faded into the bottom-right of the card

Run dl_grief_check.py after any change: it re-renders the real gita_grief
post and diffs the band positions against the originals.
"""
import pathlib, base64, subprocess, time, shutil

_REPO = pathlib.Path(__file__).resolve().parent.parent
A = _REPO / "assets"
OUT = _REPO / "out"
OUT.mkdir(parents=True, exist_ok=True)

W = 1080
H_CARD = 1350          # carousel, 4:5
H_REEL = 1920          # reel, 9:16
FPS = 25               # reference reel is CFR 25

CREAM = "#FFFDF9"
INK = "#18120D"
RUST = "#C1440E"
MUTED = "#8A8178"
GOLD = "#E8C98A"
MARGIN = 72


def _b64(p):
    return base64.b64encode((A / p).read_bytes()).decode()


def _face(n, f, w="400", s="normal"):
    return (f"@font-face{{font-family:'{n}';font-weight:{w};font-style:{s};"
            f"src:url(data:font/ttf;base64,{_b64(f)}) format('truetype');}}")


FONTS = "".join([
    _face("Pop", "Poppins-Medium.ttf", "500"),
    _face("Pop", "Poppins-SemiBold.ttf", "600"),
    _face("Pop", "Poppins-Bold.ttf", "700"),
    _face("PopI", "Poppins-MediumItalic.ttf", "500", "italic"),
    _face("Anton", "Anton-Regular.ttf", "400"),
    _face("Deva", "NotoSansDevanagari-Bold.ttf", "700"),
])
ICON = "data:image/png;base64," + _b64("logo.png")
TEMPLE = "data:image/png;base64," + _b64("temple_real.png")
PHONE = "data:image/png;base64," + _b64("phone_verse_base_full2.png")


def _css(h, bg):
    return f"""
{FONTS}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{W}px;height:{h}px;}}
body{{background:{bg};color:{INK};font-family:'Pop',sans-serif;
      position:relative;overflow:hidden;}}
body:not(.go) *{{animation-play-state:paused !important;}}
@keyframes rise{{from{{opacity:0;transform:translateY(26px);}}
                 to{{opacity:1;transform:translateY(0);}}}}
@keyframes fin{{from{{opacity:0;}}to{{opacity:1;}}}}
.an{{opacity:0;animation:rise .5s cubic-bezier(.22,.9,.3,1) forwards;}}
.af{{opacity:0;animation:fin .5s ease forwards;}}

.hdr{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:58px;
      display:flex;align-items:center;gap:15px;}}
.hdr img{{width:42px;height:42px;}}
.hdr .nm{{font-weight:700;font-size:29px;letter-spacing:.12em;color:{INK};}}
.hdr .hd{{margin-left:auto;font-weight:500;font-size:26px;color:{MUTED};}}

.card{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;background:#fff;
       border-radius:28px;box-shadow:0 18px 46px rgba(70,46,18,.07);
       overflow:hidden;}}
.tcrop{{position:absolute;right:0;bottom:0;width:352px;height:530px;
        overflow:hidden;pointer-events:none;}}
.tcrop img{{width:100%;height:100%;object-fit:cover;object-position:62% 50%;
            opacity:.5;mix-blend-mode:multiply;}}
.inner{{position:relative;z-index:2;padding:38px;}}

.chip{{display:inline-block;background:{RUST};color:#fff;font-weight:700;
       font-size:26px;letter-spacing:.14em;text-transform:uppercase;
       padding:11px 20px;border-radius:6px;}}
.head{{font-family:'Anton';font-size:78px;line-height:78px;
       text-transform:uppercase;letter-spacing:.004em;margin-top:27px;}}
.head .o{{color:{RUST};}}
.sub{{font-family:'PopI';font-style:italic;font-size:36px;line-height:46px;
      color:#4A423A;margin-top:26px;}}

.body{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;
       font-size:31px;line-height:47px;font-weight:500;}}
.pill{{display:inline-block;border:3px solid {RUST};color:{RUST};
       font-weight:700;font-size:26px;letter-spacing:.06em;
       text-transform:uppercase;padding:13px 22px;border-radius:8px;}}

.q{{text-align:center;font-weight:700;font-size:43px;line-height:52px;}}
.qrule{{width:64px;height:4px;background:{RUST};border-radius:2px;
        margin:26px auto 0;}}

.count{{position:absolute;right:{MARGIN}px;top:22px;font-weight:700;
        font-size:28px;color:{MUTED};letter-spacing:.06em;}}
.vsrc{{text-align:center;font-weight:700;font-size:23px;letter-spacing:.25em;
       text-transform:uppercase;color:{INK};}}
.vtitle{{text-align:center;font-family:'Anton';font-size:38px;line-height:46px;
         color:{RUST};text-transform:uppercase;margin-top:20px;
         transform:skewX(-8deg);}}
.vref{{text-align:center;font-weight:700;font-size:21px;letter-spacing:.10em;
       text-transform:uppercase;color:{MUTED};margin-top:20px;}}
.vrule{{width:62px;height:4px;background:{GOLD};border-radius:2px;
        margin:18px auto 0;}}
.vgloss{{text-align:center;font-family:'PopI';font-style:italic;font-size:22px;
         line-height:29px;margin-top:22px;}}

.phone{{position:absolute;left:0;width:{W}px;}}
.screen{{position:absolute;left:337px;width:368px;background:#fff;
         border-radius:18px;padding:18px 20px;text-align:center;
         box-shadow:0 6px 18px rgba(70,46,18,.06);}}
.screen .dev{{font-family:'Deva';font-weight:700;font-size:27px;
              line-height:1.62;color:{INK};}}
.screen .srule{{width:46px;height:3px;background:{GOLD};margin:14px auto;}}
.screen .tl{{font-family:'PopI';font-style:italic;font-size:21px;
             line-height:1.45;color:#4A423A;}}
.screen .tr{{font-size:20px;line-height:1.46;color:#6B6258;margin-top:13px;}}
.screen .ss{{font-weight:700;font-size:22px;color:{RUST};margin-top:16px;}}
.screen .sr{{font-size:18px;color:{MUTED};margin-top:4px;}}
.foot{{position:absolute;left:{MARGIN}px;font-weight:500;font-size:34px;
       color:{MUTED};}}
"""


def _hdr():
    return (f"<div class='hdr'><img src='{ICON}'>"
            f"<span class='nm'>DHARMA LOCK</span>"
            f"<span class='hd'>@dharmalockapp</span></div>")


def _shell(h, bg, body, extra=""):
    return (f"<html><head><meta charset='utf-8'><style>{_css(h,bg)}{extra}"
            f"</style></head><body>{body}</body></html>")


def hook_card(chip, head_lines, body_lines, pill, sub=None, h=H_CARD):
    """head_lines: list of (text, is_rust)."""
    head = "".join(
        f"<div class='{'o' if o else ''}'>{t}</div>" for t, o in head_lines)
    subhtml = f"<div class='sub an' style='animation-delay:.34s'>{sub}</div>" if sub else ""
    body = "".join(f"<div>{l}</div>" for l in body_lines)
    card_bottom = 997 if h == H_CARD else 1180
    extra = f"""
    .card{{top:212px;height:{card_bottom-212}px;}}
    .body{{top:{card_bottom+52}px;}}
    .pillwrap{{position:absolute;left:{MARGIN}px;
               top:{card_bottom+52+len(body_lines)*47+31}px;}}
    """
    inner = (f"<div class='inner'><span class='chip an'>{chip}</span>"
             f"<div class='head an' style='animation-delay:.18s'>{head}</div>"
             f"{subhtml}</div>")
    return _shell(h, CREAM,
                  f"{_hdr()}<div class='card af'>"
                  f"<div class='tcrop'><img src='{TEMPLE}'></div>{inner}</div>"
                  f"<div class='body an' style='animation-delay:.42s'>{body}</div>"
                  f"<div class='pillwrap an' style='animation-delay:.52s'>"
                  f"<span class='pill'>{pill}</span></div>", extra)


def reflection_card(chip, quote_lines, h=H_CARD):
    q = "".join(f"<div>{l}</div>" for l in quote_lines)
    card_bottom = 997 if h == H_CARD else 1180
    mid = (212 + card_bottom) // 2
    extra = f"""
    .card{{top:212px;height:{card_bottom-212}px;}}
    .qwrap{{position:absolute;left:60px;right:60px;top:50%;
            transform:translateY(-50%);z-index:2;}}
    """
    return _shell(h, CREAM,
                  f"{_hdr()}<div class='card af'>"
                  f"<div class='tcrop'><img src='{TEMPLE}'></div>"
                  f"<div class='inner'><span class='chip an'>{chip}</span></div>"
                  f"<div class='qwrap'><div class='an' style='animation-delay:.22s'>"
                  f"<div class='q'>{q}</div><div class='qrule'></div></div></div>"
                  f"</div>", extra)


def verse_card(source, title, reference, gloss, devanagari, translit,
               translation, n=1, total=1, h=H_CARD):
    dev = "<br>".join(devanagari)
    glosshtml = "".join(f"<div>{l}</div>" for l in gloss)
    phone_top = 0 if h == H_CARD else 320
    extra = f"""
    .card{{top:57px;height:556px;}}
    .inner{{padding:170px 56px 0;}}
    .phone{{top:{phone_top}px;}}
    .screen{{top:{phone_top + 638}px;}}
    .foot{{top:{h - 68}px;}}
    """
    return _shell(h, "#FFFFFF",
                  f"<div class='count'>{n} / {total}</div>"
                  f"<img class='phone af' style='animation-delay:.3s' src='{PHONE}'>"
                  f"<div class='card af'><div class='inner'>"
                  f"<div class='vsrc an'>{source}</div>"
                  f"<div class='vtitle an' style='animation-delay:.14s'>"
                  f"&ldquo;{title}&rdquo;</div>"
                  f"<div class='vref an' style='animation-delay:.24s'>{reference}</div>"
                  f"<div class='vrule'></div>"
                  f"<div class='vgloss an' style='animation-delay:.32s'>{glosshtml}</div>"
                  f"</div></div>"
                  f"<div class='screen an' style='animation-delay:.46s'>"
                  f"<div class='dev'>{dev}</div><div class='srule'></div>"
                  f"<div class='tl'>{translit}</div>"
                  f"<div class='tr'>{translation}</div>"
                  f"<div class='ss'>{source.title()}</div>"
                  f"<div class='sr'>{reference.title()}</div></div>"
                  f"<div class='foot'>@dharmalockapp</div>", extra)


def _settle(pg):
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(260)
    pg.evaluate("new Promise(r=>requestAnimationFrame("
                "()=>requestAnimationFrame(r)))")


def shot(html, path, h=H_CARD, at_s=2.2):
    from playwright.sync_api import sync_playwright
    tmp = OUT / "_d.html"
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": W, "height": h},
                        device_scale_factor=1)
        pg.goto(f"file://{tmp}")
        _settle(pg)
        pg.evaluate("document.body.classList.add('go')")
        pg.wait_for_timeout(int(at_s * 1000))
        pg.screenshot(path=str(path))
        b.close()
    return path
