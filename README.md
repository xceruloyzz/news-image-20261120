# The World Today — Friday 20 November 2026 in One Image

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/xceruloyzz/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/xceruloyzz/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One 1024×1024 PNG, drawn like a newspaper front page, that sums up Friday 20 November 2026. The edition was built in the early hours of 20 November, so the page leads with the big developments reported late on 19 November into the new day — the Shenzhen declaration, the Hague genocide ruling, the GTA VI launch-day figures and the Anthropic debut — plus the event due on the 20th itself, Cyclone Akvan's landfall.

## The stories on the page

- **Lead — Trump, Xi and Putin sign a "peace declaration".** The first-ever trilateral of the three leaders, in Shenzhen: a four-point declaration pledging dialogue on nuclear risks and more refined-fuel supply, but no arms cuts and no mention of Ukraine or Iran. (Reuters via Devdiscourse; USA Today, 19 Nov.)
- **Justice — ICJ: Myanmar guilty of genocide.** The UN court finds Myanmar committed genocide against the Rohingya in its 2017 crackdown — the first time a state has been found guilty under the Genocide Convention — and orders reparations and safe return. (Le Monde; Amnesty International; Reuters, 19 Nov.)
- **Gaming — GTA VI: 19m copies, $1.84bn.** Sensor Tower's estimate for launch day, three-quarters of it on PS5; Rockstar and Take-Two have published no official sales figure. (Reuters; GameSpot, 19 Nov.)
- **Ukraine war — Kyiv raid hits two embassies.** Russian drones kill one person and wound five; the Dutch and Austrian embassies are damaged and St Volodymyr's Cathedral windows are shattered. (AFP; Euronews, 19 Nov.)
- **Weather — Cyclone Akvan lands today.** The severe storm is due ashore near Gopalpur by noon, 90–100 km/h, with 72,000 people evacuated and red alerts on the Andhra Pradesh and Odisha coasts. (IMD National Bulletin No. 31, 19 Nov.)
- **Markets — Anthropic soars on debut.** The record $81bn IPO priced at $83 a share; ANT opens on Nasdaq at $111.50, briefly valuing the Claude maker near $2tn. (AFP via TechXplore; TechCrunch, 19 Nov.)
- **South Korea — Ex-PM Han's sentence quashed.** The Supreme Court overturns Han Duck-soo's 15-year prison term over the 2024 martial-law bid and sends the case back for retrial. (Reuters, 19 Nov.)
- **Ticker** — Nicholls 113* as New Zealand reach 243-5 vs India; Ukraine hits the Crimean Bridge, halting trains; Fiji declares a disaster over drought; fire at Yunus's ancestral home probed; Trump says Putin wants to end the war.

## How it works

`main.py` (Python 3.13, standard library only) copies the committed `entry.png` beside it to the grading output location: `$MAKEFUN_OUTPUT_DIR/entry.png` if set, else `/output/entry.png` when `/output` exists, else `./out/entry.png`. It refuses to run if `entry.png` is missing. The picture itself is drawn by `tools/generate_frontpage.py`, a PIL renderer with every word hardcoded — no network, no randomness, no clock — so running it twice reproduces `entry.png` byte for byte. The renderer also asserts each headline wraps to at most two lines and each story body to at most three, so an over-long story fails loudly instead of overflowing the grid.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=ztsmgxnm&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
