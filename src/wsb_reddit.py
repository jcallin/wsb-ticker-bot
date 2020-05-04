import logging

from praw.reddit import Reddit
from praw.models import Submission

logger = logging.getLogger()


class WSBReddit:
    def __init__(self):
        self.reddit = Reddit("WSBStockTickerBot")

    def get_submissions(self) -> [Submission]:
        return [s for s in self.reddit.subreddit("wallstreetbets").rising(limit=10)]


