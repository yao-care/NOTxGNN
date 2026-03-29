#!/usr/bin/env python3
"""Google News RSS Fetcher - Norway"""

import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import feedparser

PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/search?"
    "q=helse+legemiddel&hl=no&gl=NO&ceid=NO:no"
)


def generate_id(title: str, link: str) -> str:
    content = f"{title}:{link}"
    return hashlib.md5(content.encode()).hexdigest()[:12]


def parse_source(entry) -> dict:
    source = getattr(entry, "source", {})
    return {
        "name": source.get("title", "Unknown"),
        "url": source.get("href", ""),
    }


def fetch_google_news() -> list:
    print(f"Fetching: {GOOGLE_NEWS_HEALTH_RSS}")
    feed = feedparser.parse(GOOGLE_NEWS_HEALTH_RSS)
    articles = []
    for entry in feed.entries:
        pub_date = ""
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc).isoformat()
        source = parse_source(entry)
        articles.append({
            "id": generate_id(entry.get("title", ""), entry.get("link", "")),
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": pub_date,
            "source": source,
        })
    print(f"  Found {len(articles)} articles")
    return articles


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    articles = fetch_google_news()
    output = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "source": "Google News Health RSS",
        "count": len(articles),
        "articles": articles,
    }
    output_path = DATA_DIR / "google_rss.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(articles)} articles to {output_path}")


if __name__ == "__main__":
    main()
