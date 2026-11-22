# The Daily Front Page — 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/gentle-pika-57/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/gentle-pika-57/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

An entry for the make.fun bounty **news-image-20261122** — "Sum up 22 November's world news in one image".

## What it is

A small program that writes one newspaper front page summing up Sunday 22 November 2026 into `/output/entry.png`. Run it with:

```sh
python3 main.py
```

Set `MAKEFUN_OUTPUT_DIR` to choose a different output folder. The script uses only the Python standard library, needs no network access, and always produces the same file.

## What's on the page

The front page packs **44 verified stories** from 22 November 2026 into a single 1024×1024 image:

- **11 illustrated lead stories**, each with its own hand-drawn picture and a number linking it to the map
- **A dotted world map** with numbered pins showing where each lead story happened
- **An "also on" list** carrying the remaining stories from every region
- **Stat boxes** with real figures from the day's news
- **A date-check strip** that flags items which were *not* 22 November news, so nothing stale slips in

Every story was checked against reporting from that day before it went on the page — no invented events, numbers, quotes, or names.

## Files

- `main.py` — the entry program (standard library only)
- `entry.png` — the finished front page, 1024×1024
- `LICENSE` — MIT

---

Built for the make.fun bounty. Try it yourself: https://make.fun/r/5sa2ymrv
