import unittest
from reverselib import *

class TestReverse(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(reverse(0), 0)

    def test_ott(self):
        self.assertEqual(reverse(234), 432)

    def test_something(self):
        self.assertEqual(reverse(321), 123)

if __name__ == '__main__':
    unittest.main()
