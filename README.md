# The World Today: Friday 20 November 2026 in one image

[![news-image-20261120 on make.fun](https://img.shields.io/badge/make.fun-news--image--20261120-blue)](https://make.fun/c/news-image-20261120)
[![Friday 20 November 2026](https://img.shields.io/badge/date-20%20November%202026-black)](https://make.fun/c/news-image-20261120)

A newspaper front page that sums up Friday 20 November 2026 in a
single 1024×1024 image. It was drawn in the early hours of the 20th,
so it leads with the big developments reported late on Thursday
19 November and into the new day, plus the events due on the 20th
itself — above all the first-ever trilateral meeting of the American,
Chinese and Russian leaders in Shenzhen.

## What is on the page

**Lead — Trump, Xi and Putin sign a peace declaration in Shenzhen.**
The three leaders met for the first time as a trio on 19 November,
on the sidelines of the APEC summit, and issued a four-point joint
declaration on nuclear risk, energy supplies and UN reform. It sets
no timetable and no arsenal cuts, and says nothing about Ukraine.
Sources: The Times, 19–20 Nov 2026; Qazinform, 19 Nov 2026;
Reuters / Associated Press, 19 Nov 2026.

**The Hague — Myanmar guilty of genocide, world court rules.**
The International Court of Justice found Myanmar committed genocide
against the Rohingya in its 2017 clearance operations — the first
time the court has held a state responsible for genocide — and
ordered reparations and the return of the displaced.
Sources: CNN, 19 Nov 2026; Le Monde, 19 Nov 2026.

**Kyiv — Raid kills one and damages two embassies.**
Russian drones struck Kyiv through the day on 19 November, killing
one person and injuring five. The Dutch and Austrian embassies and
St Volodymyr's Cathedral were damaged; embassy staff were unharmed.
Sources: AFP, 19 Nov 2026; Kyiv Independent, 19 Nov 2026.

**India — Cyclone Akvan bears down on the Odisha coast.**
Severe Cyclonic Storm Akvan is due to make landfall around noon on
Friday 20 November near Gopalpur, with sustained winds of
90–100 km/h. About 72,000 people in Odisha had already been
evacuated by Thursday evening.
Sources: India Meteorological Department, 19 Nov 2026; The Hindu,
20 Nov 2026.

**Games — GTA VI launch put at 19m copies and $1.84bn.**
Sensor Tower estimates 19.1 million copies of Grand Theft Auto VI
were sold on launch day, 19 November, worth about $1.84 billion —
more than twice GTA V's first-day takings. Take-Two has given no
official figure yet.
Source: Reuters, 19 Nov 2026.

**Markets — Anthropic soars, then slips, on its debut.**
Anthropic priced its IPO at $83 a share, opened at $111.50 on
Nasdaq on 19 November and closed at $97.17. The offering, with its
private placement, raised over $100 billion — the biggest IPO
on record.
Sources: Motley Fool, 19 Nov 2026; NPR, 19 Nov 2026.

**Seoul — Court overturns ex-PM's 15-year term.**
South Korea's Supreme Court overturned former Prime Minister Han
Duck-soo's 15-year prison sentence over his role in the December
2024 martial-law attempt and sent the case back for a retrial.
Source: Reuters, 19 Nov 2026.

**Ticker —** Trump says there is no rush on an Iran decision and he
will look at it next year (Reuters, 20 Nov); NASA confirms Voyager 1
has passed a light-day from Earth (Marketscreener, 20 Nov); European
leaders say Europe is ready for talks with Russia on ending the
Ukraine war (BBC, 20 Nov); Anthropic's IPO offering is due to close
today (dpa, 20 Nov); Henry Nicholls made 113 not out as New Zealand
reached 243/5 against India in Wellington (Times of India, 19 Nov).

## How it works

`tools/generate_frontpage.py` draws the page with Pillow. All of the
news text is written into that file, and the program uses no network,
no clock and no randomness, so every run produces the same image.
It draws a masthead, a black date bar, the splash story with a
standfirst, six stories in a two-column grid, and a black ticker
strip at the foot. Built-in checks keep each headline to two lines,
each body to three lines, and the grid above the ticker.

`main.py` (Python 3.13, standard library only) simply copies the
committed `entry.png` to the grading output folder: it prefers
`$MAKEFUN_OUTPUT_DIR`, then `/output` when that directory exists,
then `./out`. It refuses to run if `entry.png` is missing.

## How to run it

```sh
python3 tools/generate_frontpage.py   # redraw entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copy it to out/entry.png
```

The output image is exactly 1024×1024 pixels and under 1 MiB.

## make.fun

This is an entry for the make.fun bounty
[news-image-20261120](https://make.fun/c/news-image-20261120):
"Sum up 20 November's world news in one image". Prizes total $250,
shared by the 50 highest-ranked entries.

Built for make.fun — https://make.fun/?ref=ztsmgxnm
