# -*- coding: utf-8 -*-
"""
@expandHinduism - "Top 5 Hindu apps" countdown carousel. TikTok photo slideshow.

Format locked 2026-11-01, modelled on @swingthoughtsgolf's app-ranking posts,
which Avi supplied as the reference. Avi 2026-11-04: "The one where the caption
is top 5 Hindu apps and we present 5 apps, 3rd is dharma lock, and then end in
CTA." That makes it 7 frames, not the 8 of the original six-app spec.

WHY THIS FILE EXISTS
--------------------
The 11/01 build lived only in the Higgsfield sandbox and was never committed.
Its delivery URLs expired 24h later and the render code went with the old
container, so the post had to be rebuilt from the format notes - the exact
failure that cost a week on the other accounts. This file is the committed
source. Run it, don't retype it.

This is also the ONLY account with no published artifact to verify against,
because nothing has ever gone out on it. Once the first post is live, its
frames go in reference/originals/ and a check goes in verify.py, and this
account joins the lock like the others.

STRUCTURE - 7 frames, 1080x1920
  1  cover    sharp cover photo, white rounded text box
  2  rank 5   Bhagavad-gita As It Is
  3  rank 4   Vignanam
  4  rank 3   Dharma Lock          <- Avi's call: never #1
  5  rank 2   Hindu Calendar - Drik Panchang
  6  rank 1   mySatsang            <- a competitor at #1 is what buys the
                                      list its credibility
  7  CTA      cta_full_poster.jpg, full-bleed. Deliberately does NOT match
              the rest; the hard visual break signals the list is over.

VISUAL RULES (from the locked format doc)
  * Every countdown frame shares the cover photo as its background, softened:
    Gaussian blur 16, blended 30% toward (255,250,242), plus a top scrim
    fading from alpha 64 over the first 620px. Avi 11/01: "The background on
    all the other images can match the first image."
  * Rank numeral top-left, Archivo Black ~176px, white with a dark outline.
  * App name and blurb in white rounded boxes.
  * Rating line sits ON the photo in outlined white, not in a third box.
  * Fonts: Archivo Black (headlines/numerals), Inter (body).

CONTENT RULES
  * The ranking is "apps on my phone", not a quality ranking. Nobody can argue
    with what is on your phone, and it lets a calendar, a Gita and a lock
    screen sit in one list without pretending they compete.
  * No competitors in the list - nothing that does lock-screen or daily
    practice. Single-purpose and sect-specific apps only.
  * Never stack the deck with weak apps. Ranking mySatsang low would burn the
    Gujarati audience, which is the most likely to share.

RATINGS ARE RE-PULLED ON EVERY RUN from the iTunes Lookup API. They move week
to week and a stale rating on screen is the kind of thing that gets noticed.

Run in the Higgsfield sandbox (it has open internet; the Claude container
cannot reach Apple's CDN or the Higgsfield CDN):

    python3 pipeline/eh_apps.py --out /home/user/eh/frames
"""
import argparse
import io
import json
import pathlib
import subprocess
import sys
import urllib.request

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920

# Background treatment - these five numbers ARE the format. Do not nudge them.
BG_BLUR = 16
BG_WASH = 0.30                 # fraction blended toward BG_WASH_RGB
BG_WASH_RGB = (255, 250, 242)
SCRIM_ALPHA = 64               # at the very top, fading to 0
SCRIM_DEPTH = 620

INK = (24, 18, 13)
PAPER = (255, 255, 255)
RULE = (193, 68, 14)           # Dharma Lock rust, used only as a thin accent

# The series cover. Generated 2026-11-01 with gpt_image_2_5 as "Cover F"
# (mandir courtyard, golden hour, distant figures for scale). The SAME photo is
# reused on every post in the series - that reuse is the mechanic that made the
# golf account read as one body of work, so this ID is pinned, not a parameter.
COVER_GEN_ID = "cf93f3d5-4c3f-4fd0-b98c-360698dced73"
COVER_URL = ("https://d8j0ntlcm91z4.cloudfront.net/user_3BQBszmzSoA5fU9dEex9K6Sd0q2/"
             "hf_20261101_203913_cf93f3d5-4c3f-4fd0-b98c-360698dced73.png")

FONT_URLS = {
    "ArchivoBlack.ttf":
        "https://github.com/google/fonts/raw/main/ofl/archivoblack/ArchivoBlack-Regular.ttf",
    "Inter.ttf":
        "https://github.com/google/fonts/raw/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf",
}

# Cover text. Avi 2026-11-04, sending the @swingthoughtsgolf cover as the
# reference (saved at reference/originals/expandhinduism_FORMAT_REFERENCE_*.png):
# "use text like the image I showed you, simple text on an image." So the cover
# is NOT a white card - it is heavy outlined white type sitting straight on the
# photo, exactly like the golf post. The white rounded boxes stay on the
# countdown frames, where they carry the app copy.
COVER_TITLE = "Top 5 Hindu Apps"
COVER_SUB = "the ones that actually live on my phone"
COVER_TITLE_PX = 104           # shrinks automatically if a longer title is set
COVER_SUB_PX = 54
COVER_TOP = 560                # where the text block starts, as on the golf post

# rank -> (itunes id, display name, blurb lines, screenshot index, join 1+2,
#          fraction to crop off the top of the screenshot)
#
# The screenshot index is chosen deliberately per app, not left at 0:
#   * Panchang shot EVERY screen in November 2018 and the year is legible on
#     all of them. A three-year-old date contradicts "lives on my phone", so
#     the dated header strip is cropped off index 4 (Choghadiya muhurat) and
#     the colour-coded muhurat table carries the frame. The app is already
#     named on the white card above, so losing its title bar costs nothing.
#   * mySatsang index 0 is a wide marketing panel that reads as empty pink with
#     a phone falling off the edge, and index 2 is a profile page dominated by
#     a QR code. Index 3 is the rituals grid. This is the #1 slot - the payoff
#     frame - so it gets the screen that actually looks like something.
APPS = [
    (5, 1080562426, "Bhagavad-gita As It Is",
     ["The whole Gita, verse by verse, with the", "Sanskrit right there. Costs nothing."], 0, False, 0.0),
    (4, 1557728556, "Vignanam",
     ["Every stotra and sahasranamam you grew up", "hearing. Nine languages."], 0, False, 0.0),
    (3, 6761774189, "Dharma Lock",
     ["Locks your apps until you pray. It is the", "reason I open any of the others."], 0, True, 0.0),
    (2, 1321271821, "Hindu Calendar",
     ["Tithi, muhurat, every festival date.", "I check it before I call my mom."], 4, False, 0.20),
    (1, 6444313821, "mySatsang",
     ["If you're Swaminarayan you already have", "this one. It is not close."], 3, False, 0.0),
]


# ---------------------------------------------------------------- fetching

def _get(url, tries=3):
    last = None
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "carousel-build/1.0"})
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read()
        except Exception as e:       # noqa: BLE001 - retry anything transient
            last = e
    raise RuntimeError(f"could not fetch {url}: {last}")


def fonts(work):
    d = work / "fonts"
    d.mkdir(parents=True, exist_ok=True)
    for name, url in FONT_URLS.items():
        p = d / name
        if not p.exists():
            p.write_bytes(_get(url))
    return d


def cover(work):
    p = work / "cover.png"
    if not p.exists():
        p.write_bytes(_get(COVER_URL))
    return Image.open(p).convert("RGB")


def bigger(shot_url, px=1200):
    """Apple serves a bigger render if you rewrite the trailing /NNNxNNNbb.ext."""
    import re
    return re.sub(r"/\d+x\d+bb\.(jpg|png)$", f"/{px}x{px*2}bb.\\1", shot_url)


def lookup(app_id):
    """Live App Store metadata. Re-pulled every run - ratings move weekly."""
    raw = _get(f"https://itunes.apple.com/lookup?id={app_id}&country=us&entity=software")
    r = json.loads(raw)["results"][0]
    return {
        "name": r["trackName"],
        "rating": r.get("averageUserRating") or 0.0,
        "count": r.get("userRatingCount") or 0,
        "icon": r.get("artworkUrl512") or r.get("artworkUrl100"),
        "shots": r.get("screenshotUrls") or [],
    }


# ---------------------------------------------------------------- drawing

def fit_cover(im, w=W, h=H):
    """Resize to cover the frame, then centre-crop. No distortion."""
    s = max(w / im.width, h / im.height)
    im = im.resize((max(w, int(im.width * s + 0.5)), max(h, int(im.height * s + 0.5))),
                   Image.LANCZOS)
    left, top = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((left, top, left + w, top + h))


def background(cov):
    """The shared softened background every countdown frame sits on."""
    bg = fit_cover(cov).filter(ImageFilter.GaussianBlur(BG_BLUR))
    wash = Image.new("RGB", bg.size, BG_WASH_RGB)
    bg = Image.blend(bg, wash, BG_WASH)

    scrim = Image.new("L", (1, SCRIM_DEPTH))
    for y in range(SCRIM_DEPTH):
        scrim.putpixel((0, y), int(SCRIM_ALPHA * (1 - y / SCRIM_DEPTH)))
    scrim = scrim.resize((W, SCRIM_DEPTH))
    full = Image.new("L", (W, H), 0)
    full.paste(scrim, (0, 0))
    bg.paste(Image.new("RGB", (W, H), (0, 0, 0)), (0, 0), full)
    return bg


def rounded(im, r):
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], r, fill=255)
    out = im.convert("RGBA")
    out.putalpha(m)
    return out


def shadow(base, box, r, blur=26, alpha=90, dy=10):
    x0, y0, x1, y1 = box
    lay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle([x0, y0 + dy, x1, y1 + dy], r, fill=(0, 0, 0, alpha))
    base.alpha_composite(lay.filter(ImageFilter.GaussianBlur(blur)))


def panel(base, box, r=34, fill=(255, 255, 255, 250)):
    shadow(base, box, r)
    lay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(lay).rounded_rectangle(list(box), r, fill=fill)
    base.alpha_composite(lay)


def wrapped(draw, text, font, max_w):
    out, line = [], ""
    for word in text.split():
        t = (line + " " + word).strip()
        if draw.textlength(t, font=font) <= max_w or not line:
            line = t
        else:
            out.append(line)
            line = word
    if line:
        out.append(line)
    return out


# ---------------------------------------------------------------- frames

def fit_font(draw, text, path, start_px, max_w, floor_px=40):
    """Largest size at or below start_px that still fits max_w on one line."""
    px = start_px
    while px > floor_px:
        f = ImageFont.truetype(str(path), px)
        if draw.textlength(text, font=f) <= max_w:
            return f
        px -= 2
    return ImageFont.truetype(str(path), floor_px)


def centred(d, text, font, y, stroke):
    """White type with a heavy dark outline, centred - the golf cover's look."""
    tw = d.textlength(text, font=font)
    d.text(((W - tw) / 2, y), text, font=font, fill=(255, 255, 255),
           stroke_width=stroke, stroke_fill=(17, 13, 10))


def frame_cover(cov, fdir, out):
    """Simple outlined text straight on the photo. No card - see COVER_TITLE."""
    im = fit_cover(cov).convert("RGBA")
    d = ImageDraw.Draw(im)

    title_f = fit_font(d, COVER_TITLE, fdir / "ArchivoBlack.ttf",
                       COVER_TITLE_PX, W - 120)
    sub_f = fit_font(d, COVER_SUB, fdir / "Inter.ttf", COVER_SUB_PX, W - 160)

    y = COVER_TOP
    centred(d, COVER_TITLE, title_f, y, stroke=13)
    y += int(title_f.size * 1.30)
    centred(d, COVER_SUB, sub_f, y, stroke=8)

    im.convert("RGB").save(out, quality=95)
    return out


def frame_rank(bg, rank, meta, blurb, shot_ix, join, crop_top, fdir, out):
    im = bg.copy().convert("RGBA")
    f_num = ImageFont.truetype(str(fdir / "ArchivoBlack.ttf"), 176)
    f_name = ImageFont.truetype(str(fdir / "ArchivoBlack.ttf"), 62)
    f_body = ImageFont.truetype(str(fdir / "Inter.ttf"), 37)
    f_rate = ImageFont.truetype(str(fdir / "Inter.ttf"), 40)

    d = ImageDraw.Draw(im)
    d.text((64, 56), str(rank), font=f_num, fill=(255, 255, 255),
           stroke_width=9, stroke_fill=(32, 24, 16))

    # name + blurb card, with the app icon tucked in at the right
    cx0, cy0, cx1, cy1 = 64, 282, 1016, 548
    panel(im, (cx0, cy0, cx1, cy1), r=32)
    d = ImageDraw.Draw(im)
    d.text((cx0 + 48, cy0 + 44), meta["name"], font=f_name, fill=INK)
    ty = cy0 + 134
    for ln in blurb:
        d.text((cx0 + 48, ty), ln, font=f_body, fill=(92, 86, 78))
        ty += 50

    icon = Image.open(io.BytesIO(_get(meta["icon"]))).convert("RGB").resize((132, 132), Image.LANCZOS)
    im.alpha_composite(rounded(icon, 30), (cx1 - 180, cy0 - 66))

    # screenshot panel
    band_top, band_bot, max_w = 596, 1648, 900
    shots = meta["shots"]
    if join and len(shots) >= 2:
        parts = [Image.open(io.BytesIO(_get(bigger(u)))).convert("RGB") for u in shots[:2]]
        hgt = min(p.height for p in parts)
        parts = [p.resize((int(p.width * hgt / p.height), hgt), Image.LANCZOS) for p in parts]
        sheet = Image.new("RGB", (sum(p.width for p in parts), hgt))
        x = 0
        for p in parts:                      # screenshots 1 and 2 join edge to edge
            sheet.paste(p, (x, 0))
            x += p.width
    else:
        sheet = Image.open(io.BytesIO(_get(bigger(shots[min(shot_ix, len(shots) - 1)])))).convert("RGB")

    if crop_top > 0:
        sheet = sheet.crop((0, int(sheet.height * crop_top), sheet.width, sheet.height))

    s = min(max_w / sheet.width, (band_bot - band_top) / sheet.height)
    sheet = sheet.resize((int(sheet.width * s), int(sheet.height * s)), Image.LANCZOS)
    sx = (W - sheet.width) // 2
    sy = band_top + (band_bot - band_top - sheet.height) // 2
    shadow(im, (sx, sy, sx + sheet.width, sy + sheet.height), 28, blur=34, alpha=105, dy=14)
    im.alpha_composite(rounded(sheet, 28), (sx, sy))

    # rating ON the photo, outlined white - never in a third box
    d = ImageDraw.Draw(im)
    line = f"★ {meta['rating']:.1f}   {meta['count']:,} ratings"
    tw = d.textlength(line, font=f_rate)
    d.text(((W - tw) / 2, 1706), line, font=f_rate, fill=(255, 255, 255),
           stroke_width=6, stroke_fill=(38, 28, 20))
    im.convert("RGB").save(out, quality=95)
    return out


def frame_cta(poster_path, out):
    im = fit_cover(Image.open(poster_path).convert("RGB"))
    im.save(out, quality=95)
    return out


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="/home/user/eh/frames")
    ap.add_argument("--work", default="/home/user/eh")
    ap.add_argument("--poster", default=None,
                    help="cta_full_poster.jpg; defaults to the repo copy")
    ap.add_argument("--post", default=None,
                    help="module defining APPS / COVER_TITLE / COVER_SUB for a "
                         "later post in the series, e.g. eh_post_hindutech. "
                         "Omitted, the module defaults above build post one, so "
                         "the first post stays reproducible.")
    a = ap.parse_args()

    # A later post in the series supplies its own list and cover text. The
    # layout, background treatment and rules stay here so every post in the
    # series renders identically.
    if a.post:
        import importlib
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
        p = importlib.import_module(a.post)
        g = globals()
        for key in ("APPS", "COVER_TITLE", "COVER_SUB",
                    "COVER_TITLE_PX", "COVER_SUB_PX", "COVER_TOP"):
            if hasattr(p, key):
                g[key] = getattr(p, key)

    work = pathlib.Path(a.work)
    work.mkdir(parents=True, exist_ok=True)
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    repo = pathlib.Path(__file__).resolve().parent.parent
    poster = pathlib.Path(a.poster) if a.poster else repo / "assets" / "cta_full_poster.jpg"
    if not poster.exists():
        raise SystemExit(f"CTA poster not found at {poster}")

    fdir = fonts(work)
    cov = cover(work)
    bg = background(cov)

    made = [frame_cover(cov, fdir, out / "eh_1_cover.jpg")]
    for i, (rank, app_id, name, blurb, shot_ix, join, crop_top) in enumerate(APPS, start=2):
        meta = lookup(app_id)
        meta["name"] = name              # display name, not the long store title
        made.append(frame_rank(bg, rank, meta, blurb, shot_ix, join, crop_top, fdir,
                               out / f"eh_{i}_rank{rank}.jpg"))
        print(f"  {rank}  {name}  {meta['rating']:.2f} / {meta['count']} ratings")
    made.append(frame_cta(poster, out / "eh_7_cta.jpg"))

    for p in made:
        print(p)
    print(f"{len(made)} frames in {out}")


if __name__ == "__main__":
    main()
