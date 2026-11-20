#!/usr/bin/env python3
"""Render the 20 November 2026 front page as a 1024x1024 PNG.

Every word on the page is fixed text chosen for Friday 20 November 2026
and drawn with PIL from the DejaVu fonts on this machine. The script takes
no input, reads no clock, rolls no dice and makes no network calls, so
running it twice produces the same bytes twice. The picture lands in the
repository root as entry.png.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
MARGIN = 28
EDGE = PAGE - MARGIN

PALETTE = {
    "ink": (18, 18, 18),
    "body": (42, 42, 42),
    "paper": (250, 248, 242),
    "red": (178, 24, 24),
    "rule": (190, 185, 175),
    "white": (255, 255, 255),
}

FONT_FILES = {
    "bold": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "regular": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "serif": "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
}


def font(name, size):
    return ImageFont.truetype(FONT_FILES[name], size)


def shrink_to_fit(draw, text, name, size, width):
    """Largest size at or below `size` that fits `text` in `width`."""
    while size > 10:
        candidate = font(name, size)
        if draw.textlength(text, font=candidate) <= width:
            return candidate
        size -= 2
    return font(name, 10)


def wrap_text(draw, text, face, width):
    """Split `text` into lines no wider than `width` in `face`."""
    lines, current = [], ""
    for word in text.split():
        attempt = f"{current} {word}".strip()
        if draw.textlength(attempt, font=face) <= width:
            current = attempt
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_centered(draw, y, text, face, colour):
    x = (PAGE - draw.textlength(text, font=face)) / 2
    draw.text((x, y), text, font=face, fill=colour)


LEAD = {
    "kicker": "DIPLOMACY  •  SHENZHEN",
    "lines": ["THREE POWERS SIGN", "PEACE DECLARATION"],
    "standfirst": (
        "Trump, Xi and Putin pledge nuclear-risk talks; no arms cuts, "
        "and no mention of Ukraine or Iran."
    ),
}

GRID = [
    {
        "kicker": "JUSTICE • THE HAGUE",
        "head": "ICJ: Myanmar guilty of genocide",
        "body": (
            "First state ever found guilty by the UN court, over the 2017 "
            "Rohingya crackdown; reparations ordered."
        ),
    },
    {
        "kicker": "GAMING",
        "head": "GTA VI: 19m copies, $1.84bn",
        "body": (
            "Sensor Tower estimate for launch day; PS5 takes 75% of sales. "
            "Rockstar has published no official figure."
        ),
    },
    {
        "kicker": "UKRAINE WAR",
        "head": "Kyiv raid hits two embassies",
        "body": (
            "Russian drones kill one and wound five; Dutch and Austrian "
            "embassies damaged, cathedral windows shattered."
        ),
    },
    {
        "kicker": "WEATHER • INDIA",
        "head": "Cyclone Akvan lands today",
        "body": (
            "Due ashore near Gopalpur by noon, 90-100 km/h; 72,000 "
            "evacuated as red alerts cover the coast."
        ),
    },
    {
        "kicker": "MARKETS • AI",
        "head": "Anthropic soars on debut",
        "body": (
            "Record $81bn IPO priced at $83; shares open at $111.50, "
            "briefly valuing Claude's maker near $2tn."
        ),
    },
    {
        "kicker": "SOUTH KOREA",
        "head": "Ex-PM Han's sentence quashed",
        "body": (
            "Top court overturns Han Duck-soo's 15-year term over the 2024 "
            "martial law bid and orders a retrial."
        ),
    },
]

TICKER_ITEMS = [
    "Nicholls 113* as NZ reach 243-5 vs India",
    "Ukraine hits Crimean Bridge, trains halted",
    "Fiji declares disaster over drought",
    "Fire at Yunus ancestral home probed",
    "Trump: Putin wants to end the war",
]


def draw_story(draw, x, y, width, item):
    """Draw one grid story; return the y just below it."""
    draw.text((x, y), item["kicker"], font=font("bold", 17), fill=PALETTE["red"])
    y += 23
    headline = font("bold", 25)
    head_lines = wrap_text(draw, item["head"], headline, width)
    assert len(head_lines) <= 2, f"head too long: {item['head']}"
    for line in head_lines:
        draw.text((x, y), line, font=headline, fill=PALETTE["ink"])
        y += 30
    y += 1
    body_face = font("regular", 18)
    body_lines = wrap_text(draw, item["body"], body_face, width)
    assert len(body_lines) <= 3, f"body too long: {item['body']}"
    for line in body_lines:
        draw.text((x, y), line, font=body_face, fill=PALETTE["body"])
        y += 23
    return y


def build_page():
    img = Image.new("RGB", (PAGE, PAGE), PALETTE["paper"])
    draw = ImageDraw.Draw(img)

    # Masthead: red rule, nameplate, black date bar.
    draw.rectangle([0, 0, PAGE, 9], fill=PALETTE["red"])
    nameplate = shrink_to_fit(draw, "THE WORLD TODAY", "serif", 80, 950)
    draw_centered(draw, 12, "THE WORLD TODAY", nameplate, PALETTE["ink"])
    draw.rectangle([MARGIN, 100, EDGE, 146], fill=PALETTE["ink"])
    date_face = font("bold", 32)
    draw_centered(draw, 108, "FRIDAY  20  NOVEMBER  2026", date_face, PALETTE["white"])

    # Lead story: kicker, two-line splash headline, standfirst.
    draw_centered(draw, 158, LEAD["kicker"], font("bold", 23), PALETTE["red"])
    y = 190
    splash = font("bold", 57)
    for line in LEAD["lines"]:
        draw_centered(draw, y, line, splash, PALETTE["ink"])
        y += 66
    standfirst = font("regular", 23)
    for line in wrap_text(draw, LEAD["standfirst"], standfirst, 930):
        draw_centered(draw, y + 2, line, standfirst, PALETTE["body"])
        y += 30
    y += 8
    draw.line([MARGIN, y, EDGE, y], fill=PALETTE["ink"], width=4)
    y += 14

    # Secondary stories: two columns, three rows, ruled between rows.
    column = 462
    left_x, right_x = 32, 530
    for index in range(0, len(GRID), 2):
        left_end = draw_story(draw, left_x, y, column, GRID[index])
        right_end = draw_story(draw, right_x, y, column, GRID[index + 1])
        y = max(left_end, right_end) + 7
        draw.line([MARGIN, y - 5, EDGE, y - 5], fill=PALETTE["rule"], width=2)
    assert y <= PAGE - 124, f"grid overflow: y={y}"

    # Ticker strip along the foot of the page.
    draw.rectangle([0, PAGE - 118, PAGE, PAGE], fill=PALETTE["ink"])
    ticker = "ALSO TODAY  ▸  " + "  ▸  ".join(TICKER_ITEMS)
    ty = PAGE - 100
    for line in wrap_text(draw, ticker, font("bold", 23), 950):
        draw_centered(draw, ty, line, font("bold", 23), PALETTE["white"])
        ty += 33
    return img


def main():
    out = Path(__file__).resolve().parent.parent / "entry.png"
    build_page().save(out, format="PNG", optimize=False)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
