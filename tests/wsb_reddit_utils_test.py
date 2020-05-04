import unittest

from src.wsb_reddit_utils import *


class WsbRedditUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.text = f'''
                $Rip airlines
                VEM is going to moon
                {str(TICKER_EXCLUSIONS)} 
                TLDR: should be excluded
                Invest in What's Real: SPY
                OTM and ITM should not be matched nor at the end OTM
                $DIS yolo on earnings and DD
                Welcome to Fabulous Wallstreetbets
                ASMR will crash
                BBWT will also moon
                $Z sucks, more like $ZZ
                Papa Buffet $ASMR
                South Park has known how the fed operates since 2009
                SPY Perhaps my friend isn’t ready for trading after all...
                Warren Buffet
            '''

    def test_parse_tickers_from_text(self):
        expected_out = ['$ASMR', '$BBWT', '$DIS', '$SPY', '$VEM', '$Z', '$ZZ']

        self.assertEqual(parse_tickers_from_text(self.text), expected_out)


if __name__ == '__main__':
    unittest.main()
