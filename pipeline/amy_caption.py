"""
@amysharma_dharma caption overlay.

Style measured 2026-11-03 off the account's own live grid (Avi: "This is the
font that's working"). Tiles were 440px wide standing in for a 1080px frame,
so everything below is the tile measurement x2.4545:

    font        Poppins Bold, white
    size        60px, line-height 71px   (tile: line pitch 29px)
    stroke      black, ~7px, plus a soft drop shadow
    width       wraps at ~780px          (tile: widest line 301px)
    align       centred, horizontally centred in frame
    position    text block around 55-64% down the frame - the neck/collar
                line. NEVER over the face or chest.
    case        sentence case, first letter of the first word capitalised;
                a single word may be shouted in caps for emphasis
                ("pray to BHAGWAN first")
    reveal      the whole block appears at once. No staged lines.

Rules this must keep (from the account's standing notes, not from the image):
  * reaction clip first, CTA clip appended after
  * the hook must tie back to the Hindu app, not just name her expression
  * music baked into BOTH the Instagram and TikTok cuts - nothing ships
    silent on this account unless Avi says he is posting that one himself
  * captions on the post itself stay short, in her voice, no pitch
  * OVERLAY VOICE: one short thought, and VARY THE OPENER. Avi,
    2026-11-12: "I see that you have been using the same reaction for the
    last 3 posts" - the POV formula below went stale in two days. Discovery
    is the register; "POV:" is only one way into it, and a plain reaction
    line ("ok i'm actually keeping this one", "genuinely did not expect
    that") is what the two best-performing posts on this account used. Check
    the last two posts before writing a third.
  * The rule that formula came from, kept for the reasoning. Avi,
    2026-11-10, on a narrative three-liner: "the captions on the girls face
    for Amy is not great either. Why not something like 'POV: finally found
    this app during new years #saalMubarak'". So: open with "POV:", say the
    one thing, and put the day's hashtag in the overlay rather than only in
    the post caption. Narration about how she feels is not the register -
    the two best-performing posts on this account are both plain discovery.

Renders a transparent PNG the size of the frame; composite it with
ffmpeg overlay so the caption never re-encodes the reaction underneath more
than once.
"""
import pathlib, base64, subprocess

_REPO = pathlib.Path(__file__).resolve().parent.parent
A = _REPO / "assets"
OUT = _REPO / "out"
OUT.mkdir(exist_ok=True)

FONT_PX = 60
LINE_PX = 71
STROKE_PX = 7
MAX_W = 780
DEFAULT_Y = 0.57          # fraction of frame height for the block's centre


def _b64(p):
    return base64.b64encode((A / p).read_bytes()).decode()


def caption_png(lines, out_path, w=1080, h=1920, y_frac=DEFAULT_Y):
    """Transparent overlay with the hook text. `lines` is a list of strings —
    break them yourself so the line breaks read the way you want."""
    from playwright.sync_api import sync_playwright
    body = "".join(f"<div>{l}</div>" for l in lines)
    html = f"""<html><head><meta charset='utf-8'><style>
@font-face{{font-family:'Pop';font-weight:700;
  src:url(data:font/ttf;base64,{_b64('Poppins-Bold.ttf')}) format('truetype');}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{w}px;height:{h}px;background:transparent;}}
.cap{{position:absolute;left:50%;top:{y_frac*100:.2f}%;
      transform:translate(-50%,-50%);width:{MAX_W}px;
      font-family:'Pop';font-weight:700;font-size:{FONT_PX}px;
      line-height:{LINE_PX}px;color:#fff;text-align:center;
      paint-order:stroke fill;
      -webkit-text-stroke:{STROKE_PX}px #000;
      text-shadow:0 3px 10px rgba(0,0,0,.45);}}
</style></head><body><div class='cap'>{body}</div></body></html>"""
    tmp = OUT / "_cap.html"
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": h},
                        device_scale_factor=1)
        pg.goto(f"file://{tmp}")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        pg.screenshot(path=str(out_path), omit_background=True)
        b.close()
    return out_path


def burn(clip, overlay_png, out_path):
    """Composite the caption onto a reaction clip without touching its audio."""
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-i", str(clip),
        "-i", str(overlay_png), "-filter_complex", "[0:v][1:v]overlay=0:0[v]",
        "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-preset", "medium",
        "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "copy",
        str(out_path)
    ], check=True)
    return out_path


if __name__ == "__main__":
    caption_png(["POV: you found the Hindu app",
                 "that blocks your socials",
                 "until you pray"], OUT / "amy_caption_sample.png")
    print("sample written to out/amy_caption_sample.png")
