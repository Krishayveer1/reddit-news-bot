import praw
import config
import pandas as pd
import time
from datetime import datetime, timedelta, timezone

# 1) Config & subs
subs = [
    'geopolitics'#add more 
]

def bot_login():
    return praw.Reddit(
        client_id     = config.client_id,
        client_secret = config.client_secret,
        user_agent    = "<USERNAME>'s Reddit Bot",
        username      = config.username,
        password      = config.password
    )

def fetch_yesterdays_posts(r):
    """Return a list of dicts for all posts from yesterday."""
    results = []
    now_local      = datetime.now(timezone.utc).astimezone()
    today_date     = now_local.date()
    yesterday_date = (now_local - timedelta(days=1)).date()

    for name in subs:
        for post in r.subreddit(name).new(limit=100):
            post_dt = datetime.fromtimestamp(post.created_utc, timezone.utc) \
                         .astimezone()
            if post_dt.date() == today_date:
                continue
            if post_dt.date() < yesterday_date:
                break  # older than yesterday, stop this subreddit
            # exactly yesterday
            results.append({
                'subreddit': name,
                'id':        post.id,
                'title':     post.title,
                'selftext': post.selftext,
                'score':     post.score,
                'url':       post.url,
                'posted_at': post_dt.isoformat()
            })
    return results

def save_top5_csv(posts):
    """Take a list of post-dicts, pick top 5 by score, write CSV."""

    df = pd.DataFrame(posts)

    top5 = df.sort_values('score', ascending=False).head(5)

    date_str = (datetime.now(timezone.utc).astimezone() - timedelta(days=1))\
                  .date().isoformat()
    filename = f"{date_str}_top5_news.csv"
    top5.to_csv(filename, index=False)
    print(f"Saved top 5 to {filename}")

def main():
    reddit = bot_login()
    posts = fetch_yesterdays_posts(reddit)
    if not posts:
        print("No posts from yesterday found.")
        return
    save_top5_csv(posts)

if __name__ == "__main__":
    main()