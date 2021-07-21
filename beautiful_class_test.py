from beautiful_class import MyBeautifulClass
from unittest.mock import patch
from unittest.mock import MagicMock
import unittest

# @patch('MyBeautifulClass')

class TestBeautifulClass(unittest.TestCase):

    def testMyBeautifulClass(self):
        x = MyBeautifulClass()
        x.splitQuote = MagicMock(return_value=['bye', 'world'])
        x.publishQuoteToMq = MagicMock(name='publishQuoteToMq')

        res = x.splitCusotmQuote('bye world')
        x.publishQuoteToMq()

        unittest.TestCase.assertEqual(self, res, ['bye', 'world'])
        x.publishQuoteToMq.assert_called()

if __name__ == "__main__":
    unittest.main()