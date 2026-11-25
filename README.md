# Sum up 25 November's world news in one image

make.fun bounty: **“Sum up 25 November's world news in one image”**
https://make.fun/bounty/news-image-20261125

- Reward: $100 total, 50 places paid (1st $20, 2nd $12, 3rd $6, 4th–10th $2 each, 11th–50th $1.20 each)
- Ends: Fri 27 Nov 2026, 00:00 UTC (03:30 Tehran)
- Round 1 closes: Wed 25 Nov 2026, 12:00 UTC (15:30 Tehran)
- Entry by: kali — make.fun `@kali-defi-2`, GitHub `@kalidefi`, Solana wallet `BvNG…R8hv`

## What it does

`main.py` (Python 3, Pillow only, no network) renders a single
1024×1024 PNG newspaper front page — **“THE WORLD IN ONE PAGE —
WEDNESDAY 25 NOVEMBER 2026”** — with the six stories that dominated
the morning of 25 Nov 2026, plus a sport strip. It writes the image to:

- `/output/entry.png` when `/output` exists (the make.fun harness path), **and**
- `output/entry.png` next to this file (so the repo always holds the image)

Running it twice produces byte-identical output: no network, no
randomness, no timestamps, fixed fonts (DejaVu, with Liberation fallback).

## The six stories (all verified, see NEWS.md)

1. **Ukraine — war at sea:** Zelenskyy confirms Ukraine's drone strike on the Russian cargo ship *Sparta II* in the Gulf of Finland (hit 21 Nov; confirmed 24 Nov). Norway urged caution.
2. **Riyadh:** Houthi drone hits the PIF Tower, Riyadh's tallest tower — 11 injured; second strike in under a week. UK sanctioned the Houthis and four officials the same day (24 Nov).
3. **Huawei convicted:** Brooklyn jury, 24 Nov — guilty on 10 of 12 counts over Iran business and stealing trade secrets.
4. **France:** Sarkozy and Carla Bruni ordered to stand trial (24 Nov) in a witness-tampering case; hearing 1 Apr 2027.
5. **Gaza:** Israeli strike kills Hamas internal security chief Naeem Abu Nahel, 50, in Gaza City (24 Nov), confirmed by both sides.
6. **Iraq:** Baghdad orders federal forces to take over Kurdish oilfields and border crossings; Kurdish leaders reject the move.

Sport strip: Real Madrid 5–1 PSV, Champions League, 24 Nov (Mbappé ×2, Bellingham).

**Honest dating note:** the bounty is for “25 November's news” and the
contest opened at the start of 25 Nov UTC. At build time (Wed 25 Nov,
~06:15 Tehran / 02:45 UTC) the verified reporting available was dated
24 Nov (Tue) / overnight 25 Nov — that is what the image sums up, and
the footer says so: “Facts as reported on 24 Nov; this page is the
morning of Wed 25 Nov 2026.” No news was invented. Later developments
on 25 Nov itself are **not** in this image.

## How to run

```bash
python3 main.py
# Wrote .../output/entry.png (140944 bytes, 1024x1024)
# Wrote /output/entry.png (140944 bytes, 1024x1024)   # if /output exists
```

Requirements: Python 3.10+ and Pillow (`pip install pillow`).
Fonts: DejaVu Sans / DejaVu Serif (standard on most Linux systems);
falls back to Liberation Sans, then Pillow's default font.

## Verification (done 25 Nov 2026, ~06:20 Tehran)

- Ran `python3 main.py` twice; `sha256sum` identical on both runs
  for both output paths (deterministic — see `output/`).
- Output checked with Pillow: 1024×1024, RGB, PNG, **140,944 bytes
  (< 1 MiB limit)**.
- Image viewed directly: all six headlines, bodies, sport strip and
  source line are fully inside their cards and legible; no clipped
  text. (An earlier draft clipped body text in the grid cards; the
  layout was fixed and re-checked.)
- Dates checked with `date`: Wed 25 Nov 2026, 06:15 Tehran.

## Files

| File | What it is |
|---|---|
| `main.py` | The entry program (root, as the bounty requires) |
| `output/entry.png` | Generated image (1024×1024, 140,944 bytes) |
| `output/summary-2026-11-25.png` | Copy of the same image, dated name |
| `NEWS.md` | Story-by-story sources, dates and extra detail |
| `README.md` | This file |
| `LICENSE` | MIT licence (OSI-approved, as the bounty requires) |

## What is still missing to submit (NOT done here)

- [ ] Create a **public GitHub repository** under `@kalidefi` (created after the competition opened), containing `main.py` at the root, under the MIT licence.
- [ ] Upload the **agent transcripts** of the sessions that built this entry with the submission.
- [ ] **Link GitHub and X** on make.fun for `@kalidefi` / `@kali_defi2` (linking needs the user in their own browser; GitHub needs a Phantom wallet approval).
- [ ] **Submit / sign** the entry on make.fun with the wallet `BvNG…R8hv` — no submission, signature, post, funding or account-linking was done by this agent, as instructed.
- [ ] Optional: if later news on 25 Nov changes the picture materially before Round 1 closes (15:30 Tehran), rebuild and re-submit — the last submission before the deadline is the final entry (max 10/day, 20 total).
