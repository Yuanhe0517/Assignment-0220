import unittest

from main import horner_method  # 直接导入函数

class TestHornerMethod(unittest.TestCase):
    def test_case_1(self):
        coefficients = [3, 2, 5, 7]
        x0 = 2

        expected = 49.0

        self.assertAlmostEqual(horner_method(coefficients, x0), expected, delta=1e-6)

    # 其他测试用例同理，直接调用函数

if __name__ == "__main__":
    unittest.main()
