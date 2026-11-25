#!/usr/bin/env python3
"""
Sum up 25 November's world news in one image — make.fun bounty
https://make.fun/bounty/news-image-20261125

Writes a single 1024x1024 PNG to /output/entry.png (the make.fun
harness path) or, when /output does not exist, to output/entry.png
next to this file.

Deterministic, offline, stdlib + Pillow only. No network, no random
numbers, no timestamps in the image. Running it twice produces
byte-identical output (Pillow writes no timestamps into PNGs).

News facts are hard-coded in STORIES below, each verified against
Reuters / Bloomberg / Le Monde / WSJ / Al Jazeera reporting of
24-25 November 2026 — see NEWS.md for the source list. The program
does not fetch news at run time (the bounty forbids network access).
"""
import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

# ---------------------------------------------------------------- news
# Headlines + summaries as reported on 24 Nov 2026 (the stories that
# dominated the morning of Wed 25 Nov 2026). Wording is kept short so
# every word stays legible at 1024 px. See NEWS.md for full sourcing.
STORIES = [
    dict(tag="UKRAINE  •  WAR AT SEA", colour="#1B4F72",
         head="Zelenskyy confirms Ukraine drone strike on Russian ship",
         body=("Kyiv says the sanctioned cargo vessel Sparta II, hit on "
               "21 Nov in the Gulf of Finland, was carrying weapons. "
               "Norway, a Kyiv ally, urged caution.")),
    dict(tag="MIDDLE EAST  •  RIYADH", colour="#7D2E1D",
         head="Houthi drone hits Riyadh's tallest tower; 11 injured",
         body=("Second hit on the PIF Tower in under a week (first: "
               "19 Nov, no injuries). The UK sanctioned the Houthis "
               "and four officials the same day.")),
    dict(tag="USA / CHINA  •  COURTS", colour="#145A32",
         head="Huawei convicted in US trial over Iran business",
         body=("A Brooklyn jury on 24 Nov found Huawei guilty on 10 of "
               "12 counts: bank fraud, sanctions violations and stealing "
               "trade secrets.")),
    dict(tag="FRANCE  •  COURTS", colour="#5B2C6F",
         head="Sarkozy and Carla Bruni ordered to stand trial",
         body=("Paris judges on 24 Nov sent the ex-president and his wife "
               "to trial in a witness-tampering case. Hearing: 1 Apr 2027. "
               "Both deny wrongdoing.")),
    dict(tag="GAZA", colour="#7D6608",
         head="Israeli strike kills Hamas internal security chief",
         body=("Naeem Abu Nahel, 50, was killed in Gaza City on 24 Nov, "
               "confirmed by both Hamas and Israel. Six others were "
               "reported killed the same day.")),
    dict(tag="IRAQ  •  OIL STANDOFF", colour="#0E6655",
         head="Baghdad orders takeover of Kurdish oilfields",
         body=("Iraq's PM ordered federal forces to seize oilfields and "
               "border crossings in Kurdish-run areas after a smuggling "
               "crackdown. Kurdish leaders rejected it.")),
]

SPORT = ("SPORT  •  Real Madrid 5–1 PSV in the Champions League, 24 Nov — "
         "Mbappé scored twice and Bellingham struck a stunning goal.")
SOURCES = ("Sources: Reuters, Bloomberg, Le Monde, The Wall Street Journal, "
           "Al Jazeera — reports of 24–25 Nov 2026. Facts as reported on "
           "24 Nov; this page is the morning of Wed 25 Nov 2026.")

# ---------------------------------------------------------------- fonts
def load_font(bold=False, serif=False, size=20):
    candidates = []
    if serif:
        candidates += ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"]
    elif bold:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]
    else:
        candidates += [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default(size=size)


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_card(draw, x, y, w, h, story, num, head_size=27, body_size=20, max_body=3):
    tag_f = load_font(bold=True, size=17)
    head_f = load_font(bold=True, size=head_size)
    body_f = load_font(size=body_size)
    # card
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10,
                           fill="white", outline="#D5CFC0", width=2)
    # number badge + tag
    draw.ellipse([x + 16, y + 14, x + 48, y + 46], fill=story["colour"])
    num_f = load_font(bold=True, size=19)
    tw = draw.textlength(str(num), font=num_f)
    draw.text((x + 32 - tw / 2, y + 17), str(num), font=num_f, fill="white")
    draw.text((x + 60, y + 20), story["tag"], font=tag_f, fill=story["colour"])
    # headline
    lines = wrap(draw, story["head"], head_f, w - 32)
    ty = y + 54
    for line in lines[:2]:
        draw.text((x + 16, ty), line, font=head_f, fill="#111111")
        ty += head_size + 6
    # body
    for line in wrap(draw, story["body"], body_f, w - 32)[:max_body]:
        draw.text((x + 16, ty), line, font=body_f, fill="#333333")
        ty += body_size + 5


def main():
    img = Image.new("RGB", (W, H), "#F7F3EA")
    draw = ImageDraw.Draw(img)

    # ---- masthead -------------------------------------------------
    draw.rectangle([0, 0, W, 124], fill="#0F2A44")
    draw.rectangle([0, 124, W, 130], fill="#C0392B")
    title_f = load_font(bold=True, serif=True, size=48)
    draw.text((32, 16), "THE WORLD IN ONE PAGE", font=title_f, fill="white")
    sub_f = load_font(bold=True, size=20)
    draw.text((32, 88),
              "WEDNESDAY 25 NOVEMBER 2026  •  WORLD NEWS IN ONE IMAGE",
              font=sub_f, fill="#F9D976")
    kicker_f = load_font(bold=True, size=20)
    label = "6 STORIES"
    lw = draw.textlength(label, font=kicker_f)
    draw.rounded_rectangle([W - 32 - lw - 24, 76, W - 32, 112],
                           radius=8, fill="#C0392B")
    draw.text((W - 32 - lw - 12, 84), label, font=kicker_f, fill="white")

    # ---- lead story (1) -------------------------------------------
    draw_card(draw, 32, 144, W - 64, 170, STORIES[0], 1,
              head_size=30, body_size=21, max_body=2)

    # ---- grid stories (2-5) ---------------------------------------
    col_w = (W - 64 - 16) // 2
    positions = [(32, 330), (32 + col_w + 16, 330),
                 (32, 531), (32 + col_w + 16, 531)]
    for story, (cx, cy) in zip(STORIES[1:5], positions):
        draw_card(draw, cx, cy, col_w, 185, story,
                  STORIES.index(story) + 1, head_size=23, body_size=18, max_body=3)

    # ---- story 6, full width --------------------------------------
    draw_card(draw, 32, 732, W - 64, 126, STORIES[5], 6,
              head_size=25, body_size=19, max_body=2)

    # ---- sport strip ----------------------------------------------
    draw.rounded_rectangle([32, 874, W - 32, 928], radius=8, fill="#0F2A44")
    sport_f = load_font(bold=True, size=19)
    for i, line in enumerate(wrap(draw, SPORT, sport_f, W - 96)):
        draw.text((48, 882 + i * 24), line, font=sport_f, fill="white")
        if i >= 1:
            break

    # ---- footer / sources -----------------------------------------
    foot_f = load_font(size=16)
    for i, line in enumerate(wrap(draw, SOURCES, foot_f, W - 64)):
        draw.text((32, 942 + i * 21), line, font=foot_f, fill="#555555")
        if i >= 2:
            break

    # ---- output path: make.fun harness wants /output/entry.png ----
    # Write there when it exists, and always also to output/entry.png
    # next to this file, so the repository itself holds the image.
    targets = [Path(__file__).resolve().parent / "output" / "entry.png"]
    if Path("/output").is_dir():
        targets.append(Path("/output/entry.png"))
    for out in targets:
        out.parent.mkdir(parents=True, exist_ok=True)
        img.save(out, format="PNG", optimize=True)
        print(f"Wrote {out} ({out.stat().st_size} bytes, {W}x{H})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
