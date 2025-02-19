import unittest

from main import calculate_polynomial

class TestPolynomial(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(calculate_polynomial(3, 0, [1, 2, 3]), -6)
    
    def test_zero_result(self):
        self.assertEqual(calculate_polynomial(2, 5, [5, 3]), 0)
    
    def test_negative_numbers(self):
        self.assertEqual(calculate_polynomial(2, -2, [1, -3]), -3)

if __name__ == "__main__":
    unittest.main()
