import unittest
from reverselib import *

class TestReverse(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(reverse(0), 0)

    def test_ott(self):
        self.assertEqual(reverse(234), 432)

    def test_tva(self):
        self.assertEqual(reverse(2345), 5432)
    
    def test_tre(self):
        self.assertNotEqual(reverse(234), 234)
    
    def test_tre(self):
        self.assertEqual(reverse(21), 12)
if __name__ == '__main__':
    unittest.main()
