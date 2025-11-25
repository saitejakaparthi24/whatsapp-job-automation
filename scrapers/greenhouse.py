import feedparser
from datetime import datetime

def fetch_greenhouse_jobs():
    jobs = []
    boards = feedparser.parse("https://boards.greenhouse.io/boards.xml")

    for b in boards.entries[:50]:  # limit for free GitHub runner
        company_feed = b.link + ".xml"
        feed = feedparser.parse(company_feed)

        for entry in feed.entries:
            jobs.append({
                "id": entry.id,
                "company": b.title,
                "title": entry.title,
                "url": entry.link,
                "posted_at": datetime(*entry.published_parsed[:6])
            })
    return jobs
