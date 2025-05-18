import schedule
import time
from telegram_scraper import get_telegram_posts
from rewriter import simple_rewrite
from facebook_poster import post_to_facebook

posted = set()

def job():
    posts = get_telegram_posts()
    for post in posts:
        if post not in posted:
            rewritten = simple_rewrite(post)
            post_to_facebook(rewritten)
            posted.add(post)

schedule.every(3).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)