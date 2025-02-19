# test_main.py

import main

def test_calculate_sum():
    assert main.calculate_sum() == 1275, "求和结果错误，应为1+2+...+50=1275"
