import re
import logging

from praw.models import Submission

logger = logging.getLogger()

TICKER_EXCLUSIONS = ["OTM", "ITM", "ATM", "ATH", "MACD", "ROI", "GAIN", "LOSS", "TLDR", "CEO"]


def parse_tickers_from_text(text) -> [str]:
    match_3_4_maybe_with_dollar = r'\$?[A-Z]{3,4}(?=\s|$)'
    match_1_2_with_dollar = r'\$[A-Z]{1,2}(?=\s|$)'
    match_spy = r'\$?SPY|\$?SPX'
    ticker_regex = f"{match_3_4_maybe_with_dollar}|{match_1_2_with_dollar}|${match_spy}"
    logger.debug(ticker_regex)

    raw_tickers = [t for t in re.findall(ticker_regex, text)]

    # Exclude some common terms which we know are not tickers
    for exclusion in TICKER_EXCLUSIONS:
        while exclusion in raw_tickers:
            raw_tickers.remove(exclusion)

    # Add $ to front if it is not there, unique, and sort
    return list(sorted(set(['$' + ticker if ticker[0] != '$' else ticker for ticker in raw_tickers])))


# Return a list of tickers for a submission in format $AAPL
def get_tickers_for_submission(submission: Submission) -> [str]:
    logger.debug(submission.title + "\n" + (submission.selftext if submission.is_self else "LINK POST\n"))
    tickers = parse_tickers_from_text(submission.title + "\n" + ((submission.selftext + "\n") if submission.is_self else "\n"))
    return [t for t in tickers if len(t) != 0]
