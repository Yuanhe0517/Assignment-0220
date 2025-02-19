# test.py
import unittest
from main import find_num_terms

class TestNumberOfTerms(unittest.TestCase):

    def test_find_num_terms(self):
        x = 0.25
        expected_num_terms = 4  
        num_terms = find_num_terms(x)
        self.assertEqual(num_terms, expected_num_terms)

if __name__ == "__main__":
    unittest.main()
