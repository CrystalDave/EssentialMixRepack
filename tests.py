"""
Test cases for EssentialMix Repack
"""

# Import context without requiring package installation
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import essentialmix_repack as repack


class TestTitleExtract(unittest.TestCase):
    """ Title extraction is currently brittle, so we can use known cases """

    def setUp(self):
        pass

    def test_happypath(self):
        """ make sure the happy path extracts artist and date"""
        testStrings = [
            "Carista - Essential Mix 2020-02-08",
            "Kölsch - Essential Mix 2018-12-22",
        ]
        expectedResults = [
            {"artist": "Carista", "date": "2020-02-08"},
            {"artist": "Kölsch", "date": "2018-12-22"},
        ]
        for n, test in enumerate(testStrings):
            result = repack.extractTitleData(test)
            self.assertDictEqual(result, expectedResults[n])

    def test_fallbackpath(self):
        """ make sure the fallback path extracts artist"""
        testStrings = [
            "Seb Wildwood - BBC Radio 1 Essential Mix",
            "Dimension Essential Mix - BBC Radio 1",
            "Maya Jane Coles - Live @ Ants Ushuaia Ibiza 2019 [Essential Mix]",
        ]
        expectedResults = [
            {"artist": "Seb Wildwood", "date": None},
            {"artist": "Dimension", "date": None},
            {"artist": "Maya Jane Coles", "date": None},
        ]
        for n, test in enumerate(testStrings):
            result = repack.extractTitleData(test)
            self.assertDictEqual(result, expectedResults[n])


if __name__ == "__main__":
    unittest.main()
