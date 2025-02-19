# main.py

def left_side(x, num_terms):
    """
    计算方程左侧前 num_terms 项的和。
    """
    result = 0

    for n in range(num_terms):
        # 第 n 项的通项公式：
        # 分子 = 2^n * (x^{2^n} - x^{2^{n+1}})
        # 分母 = 1 - x^{2^n} + x^{2^{n+1}}
        num = (2**n) * (x**(2**n) - x**(2**(n+1)))
        denom = 1 - x**(2**n) + x**(2**(n+1))
        result += num / denom

    return result

def right_side(x):
    """
    计算方程右侧的固定值。
    """
    return (1 + 2 * x) / (1 + x + x**2)

def find_num_terms(x, tolerance=1e-6):
    """
    寻找满足左侧与右侧差异小于容差的最小项数。
    """
    num_terms = 1

    while True:
        left = left_side(x, num_terms)
        right = right_side(x)
        if abs(left - right) < tolerance:
            break

        num_terms += 1

    return num_terms

if __name__ == "__main__":
    x = 0.25  # 题目给定的 x 值

    num_terms = find_num_terms(x)
    print(f"所需最小项数: {num_terms}")