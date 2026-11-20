"""Draw the 20 November 2026 front page as a single PNG.

Everything on the page is fixed text in this file: no network, no
clock and no randomness, so running it twice gives the same bytes.
The picture is a broadsheet-style front page, 1024 by 1024 pixels,
with a masthead, a black date bar, one splash story, six shorter
stories in a two-column grid, and a black ticker along the foot.

Run it from the repository root with:  python3 tools/generate_frontpage.py
It writes entry.png next to main.py.
"""

from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SHEET = 1024
MARGIN = 40
INNER = SHEET - 2 * MARGIN
INK = (12, 12, 12)
PAPER = (252, 250, 244)
RULE = (30, 30, 30)
ACCENT = (178, 34, 34)
MUTED = (90, 86, 78)
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def pick_font(stem: str, size: int) -> ImageFont.FreeTypeFont:
    """Return a DejaVu font, falling back to PIL's built-in face."""
    candidate = FONT_DIR / stem
    if candidate.exists():
        return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default(size=size)


def serif_bold(size: int):
    return pick_font("DejaVuSerif-Bold.ttf", size)


def serif(size: int):
    return pick_font("DejaVuSerif.ttf", size)


def sans_bold(size: int):
    return pick_font("DejaVuSans-Bold.ttf", size)


def sans(size: int):
    return pick_font("DejaVuSans.ttf", size)


LEAD_KICKER = "SHENZHEN  •  APEC SUMMIT  •  FIRST TRILATERAL MEETING"
LEAD_SPLASH = ["THREE LEADERS SIGN", "A PEACE DECLARATION"]
LEAD_STANDFIRST = (
    "Trump, Xi and Putin met for the first time as a trio in Shenzhen on "
    "Thursday and issued a joint declaration on nuclear risk, energy "
    "supplies and reform of the United Nations — with no timetable, no "
    "cuts to arsenals, and no mention of Ukraine."
)

# Each entry: kicker, headline, body, source line.
GRID = [
    (
        "THE HAGUE  •  WORLD COURT",
        "Myanmar guilty of genocide, world court rules",
        "The ICJ found Myanmar committed genocide against the Rohingya in "
        "2017, a first for a state, and ordered reparations and return.",
        "CNN / Le Monde — 19 Nov 2026",
    ),
    (
        "KYIV  •  UKRAINE",
        "Kyiv raid kills one and damages two embassies",
        "Russian drones struck Kyiv all day, killing one and injuring five. "
        "The Dutch and Austrian embassies and a cathedral were damaged.",
        "AFP / Kyiv Independent — 19 Nov 2026",
    ),
    (
        "INDIA  •  CYCLONE AKVAN",
        "Cyclone Akvan bears down on the Odisha coast",
        "Landfall is due around noon on Friday near Gopalpur, with winds "
        "of 90–100 km/h. About 72,000 people have already been evacuated.",
        "IMD / The Hindu — 19–20 Nov 2026",
    ),
    (
        "GAMES  •  GTA VI",
        "GTA VI launch put at 19m copies and $1.84bn",
        "Sensor Tower estimates 19.1 million copies sold on launch day, "
        "more than twice GTA V's first-day takings. Take-Two gave no figure.",
        "Reuters — 19 Nov 2026",
    ),
    (
        "MARKETS  •  ANTHROPIC IPO",
        "Anthropic soars, then slips, on its debut",
        "Priced at $83, shares opened at $111.50 on Nasdaq and closed at "
        "$97.17 — the biggest IPO on record, raising over $100bn in all.",
        "Motley Fool / NPR — 19 Nov 2026",
    ),
    (
        "SEOUL  •  SOUTH KOREA",
        "Seoul court overturns ex-PM's 15-year term",
        "The Supreme Court overturned Han Duck-soo's sentence over the 2024 "
        "martial-law attempt and sent the case back for a retrial.",
        "Reuters — 19 Nov 2026",
    ),
]

TICKER = [
    "Trump: no rush on Iran decision, looks to next year — Reuters, 20 Nov",
    "NASA: Voyager 1 passes a light-day from Earth — Marketscreener, 20 Nov",
    "Europe ready for talks with Russia on ending the Ukraine war — BBC, 20 Nov",
    "Anthropic's IPO offering due to close today — dpa, 20 Nov",
    "Nicholls 113* as New Zealand reach 243/5 v India — Times of India, 19 Nov",
]

FOOTNOTE = (
    "Built in the early hours of 20 Nov 2026 from reports of 19–20 Nov. "
    "Full sources are listed in the README."
)


def fold(draw: ImageDraw.ImageDraw, text: str, font, width: int) -> list[str]:
    """Wrap text on word boundaries so no line is wider than width."""
    lines: list[str] = []
    current = ""
    for word in text.split():
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font) <= width or not current:
            current = trial
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paint_lines(draw, lines, x, y, font, fill, gap):
    """Draw lines top to bottom, returning the y just below the last."""
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += font.size + gap
    return y


def paint_masthead(draw):
    draw.text((MARGIN, 26), "THE WORLD TODAY", font=serif_bold(62), fill=INK)
    draw.text(
        (MARGIN, 102),
        "One day's world news, in one image  •  Friday's paper, drawn at dawn",
        font=sans(17),
        fill=MUTED,
    )
    draw.line([(MARGIN, 132), (SHEET - MARGIN, 132)], fill=RULE, width=3)


def paint_date_bar(draw):
    top, height = 146, 40
    draw.rectangle([0, top, SHEET, top + height], fill=INK)
    draw.text(
        (MARGIN, top + 7),
        "FRIDAY  20  NOVEMBER  2026",
        font=sans_bold(24),
        fill=PAPER,
    )
    note = "THE DAY IN FULL"
    right = sans(18)
    wide = draw.textlength(note, font=right)
    draw.text((SHEET - MARGIN - wide, top + 10), note, font=right, fill=PAPER)


def paint_lead(draw):
    """Paint the kicker, splash and standfirst; return the grid's top y."""
    y = 202
    draw.text((MARGIN, y), LEAD_KICKER, font=sans_bold(18), fill=ACCENT)
    y = paint_lines(draw, LEAD_SPLASH, MARGIN, y + 30, serif_bold(58), INK, 6)
    wrapped = fold(draw, LEAD_STANDFIRST, serif(21), INNER)
    assert len(wrapped) <= 4, f"standfirst ran to {len(wrapped)} lines"
    y = paint_lines(draw, wrapped, MARGIN, y + 8, serif(21), (40, 40, 40), 4)
    # The rule sits below the standfirst's last line, never through it.
    draw.line([(MARGIN, y + 4), (SHEET - MARGIN, y + 4)], fill=RULE, width=2)
    return y + 14


def paint_grid(draw, top):
    """Paint the six grid stories; each row is as tall as its content needs.

    Rows used to share one fixed height, which let a tall story run into
    the next row's kicker. Now every row is measured from what was actually
    painted, so nothing overlaps.
    """
    col_w = (INNER - 24) // 2
    y = top
    for row in range(3):
        row_bottom = y
        for col in range(2):
            index = row * 2 + col
            kicker, headline, body, source = GRID[index]
            x = MARGIN + col * (col_w + 24)
            draw.text((x, y), kicker, font=sans_bold(15), fill=ACCENT)
            head_lines = fold(draw, headline, serif_bold(23), col_w)
            assert len(head_lines) <= 2, f"headline too long: {headline!r}"
            after_head = paint_lines(
                draw, head_lines, x, y + 21, serif_bold(23), INK, 2
            )
            body_lines = fold(draw, body, sans(16), col_w)
            assert len(body_lines) <= 3, f"body too long: {body!r}"
            after_body = paint_lines(
                draw, body_lines, x, after_head + 3, sans(16), (45, 45, 45), 2
            )
            draw.text((x, after_body + 1), source, font=sans(12), fill=MUTED)
            row_bottom = max(row_bottom, after_body + 1 + 12)
        if row < 2:
            rule_y = row_bottom + 4
            draw.line(
                [(MARGIN, rule_y), (SHEET - MARGIN, rule_y)],
                fill=(200, 196, 188),
                width=1,
            )
            y = row_bottom + 8
        else:
            y = row_bottom
    assert y <= 900, f"grid ends at {y}, too low for the ticker"
    return y


def paint_ticker(draw):
    top, height = 900, 84
    draw.rectangle([0, top, SHEET, top + height], fill=INK)
    joined = "   •   ".join(TICKER)
    lines = fold(draw, joined, sans_bold(14), INNER)
    assert len(lines) <= 4, f"ticker ran to {len(lines)} lines"
    y = top + 6
    for line in lines:
        draw.text((MARGIN, y), line, font=sans_bold(14), fill=PAPER)
        y += 18
    draw.text((MARGIN, 990), FOOTNOTE, font=sans(13), fill=MUTED)


def render() -> Image.Image:
    sheet = Image.new("RGB", (SHEET, SHEET), PAPER)
    draw = ImageDraw.Draw(sheet)
    paint_masthead(draw)
    paint_date_bar(draw)
    grid_top = paint_lead(draw)
    paint_grid(draw, grid_top)
    paint_ticker(draw)
    return sheet


def main() -> None:
    here = Path(__file__).resolve().parent.parent
    target = here / "entry.png"
    render().save(target, format="PNG", optimize=True)
    print(f"wrote {target}")


if __name__ == "__main__":
    main()
