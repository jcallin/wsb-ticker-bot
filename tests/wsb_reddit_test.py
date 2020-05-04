import unittest

from src.wsb_reddit import WSBReddit
from wsb_reddit_utils import get_tickers_for_submission


class WSBRedditTest(unittest.TestCase):
    def setUp(self):
        self.wsb_reddit = WSBReddit()

    def test_get_submissions(self):
        self.wsb_reddit.get_submissions()

    def test_get_tickers_for_submissions(self):
        submissions = self.wsb_reddit.get_submissions()
        [print((s.id, get_tickers_for_submission(s))) for s in submissions]


if __name__ == '__main__':
    unittest.main()
