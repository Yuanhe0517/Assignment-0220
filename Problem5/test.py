# test.py

import unittest

from main import calculate_S

class TestCalculateS(unittest.TestCase):
    def test_normal_case(self):
        """测试正常插值情况"""
        self.assertAlmostEqual(
            calculate_S(a0=3, a1=5, x0=1, x1=3, x=2),
            4.0,  # (3*(2-3)/(1-3) + 5*(2-1)/(3-1)) = (3*0.5 + 5*0.5)=4.0
            delta=1e-6

        )
if __name__ == "__main__":
    unittest.main(verbosity=2)