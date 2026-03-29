#!/usr/bin/env python3
"""Norway Health News Fetcher"""

from pathlib import Path
from .google_rss import fetch_google_news, DATA_DIR
import json
from datetime import datetime, timezone


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    articles = fetch_google_news()
    output = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "source": "Google News Norway Health",
        "count": len(articles),
        "articles": articles,
    }
    output_path = DATA_DIR / "no_news.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(articles)} articles to {output_path}")


if __name__ == "__main__":
    main()
