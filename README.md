# reddit-news-bot

Reddit Daily Top5 News Bot

A simple Python bot that collects the top 5 highest‑scoring posts from a set of news‑focused subreddits for the previous day and writes them to a timestamped CSV file.

Features

Logs into Reddit via PRAW.

Iterates through a configurable list of subreddits.

Filters posts by date (yesterday only).

Sorts all collected posts by score and picks the top 5.

Saves results to a CSV file named YYYY-MM-DD_top5_news.csv.

Installation

Clone this repository or download the files.

Ensure you have Python 3.7+ installed.

Install dependencies:

pip install praw pandas

Configuration

Copy config_example.py to config.py.

Fill in your Reddit API credentials in config.py:

username     = "<YOUR_REDDIT_USERNAME>"
password     = "<YOUR_REDDIT_PASSWORD>"
client_id    = "<YOUR_CLIENT_ID>"
client_secret= "<YOUR_CLIENT_SECRET>"

(Optional) Adjust the subs list in reddit_bot.py to include any subreddits you want.

Usage

Run the bot manually or schedule it (e.g. via cron) to execute once a day:

python reddit_bot.py

Each run produces a CSV file with the previous day’s date in its filename, containing the top 5 posts across all configured subreddits.

Schedule with Cron Example

To run every day at 12:00 PM (local time), add this line to your crontab (crontab -e):

0 12 * * * /usr/bin/python3 /path/to/reddit_bot.py >> /path/to/logfile.log 2>&1

Contributing

Feel free to open issues or submit pull requests.

Add support for different output formats (JSON, Google Sheets).

Integrate email or Slack notifications.

Enhance filtering logic (flair, keywords).

License

MIT © Krishayveer Sultania
