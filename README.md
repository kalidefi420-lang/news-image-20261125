# The World Today — Wednesday 25 November 2026 (evening edition)

Entry for the make.fun bounty
https://make.fun/bounty/news-image-20261125 — "Sum up 25 November's
world news in one image", $100, 50 places.

## What this is

A second variant of the 25 November news image, built in the evening
so it covers the FULL day — not just the morning. The first version
was built when the day was young; this one adds everything that
developed during the day: the Trump tariffs unveiled on 14 partners,
the second Hamas security chief killed in Gaza, the tankers hit by
mines in the Strait of Hormuz, the Russian strikes on Ukraine's
energy grid, and the markets' reaction.

## Design

A newspaper front page, deliberately different from the morning
version's layout:

- Black masthead with the serif title "THE WORLD TODAY" and the date
  in gold, over a red rule.
- One full-width lead story: the new US tariffs (China 20%, EU 15%).
- A row of three cards: Gaza, the Strait of Hormuz, Ukraine.
- Two columns: "Europe & Asia" (Hong Kong fire anniversary, the EU
  summit's €45bn Ukraine loan, BepiColombo at Mercury) and "The
  Americas" (Huawei convicted, Venezuela's $237.5bn debt, the
  Thanksgiving NFL tripleheader).
- An "Also today" in-brief band: Colombia hostage rescue, Sudan,
  COP31, North Korea, Dell's record quarter, Microsoft's "Code Red".
- 38 stories in total, all sourced in NEWS.md.

## How the image was made

`output/entry.png` (1024x1024, 150,671 bytes) was drawn locally with
Pillow (DejaVu fonts). `main.py` is a standard-library-only program
that copies it to `/output/entry.png` — it imports nothing beyond the
standard library, because the grading container installs nothing.
Running `main.py` twice produces byte-identical output (a plain copy).

## Files

- `main.py` — entrypoint: copies `output/entry.png` to `/output/entry.png`
- `output/entry.png` — the image
- `NEWS.md` — all 38 stories with their sources
- `README.md` — this file
- `LICENSE` — MIT
