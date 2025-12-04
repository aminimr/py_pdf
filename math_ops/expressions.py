"""
محاسبه عبارات ریاضی پیچیده
Reference: صفحات 10, 19, 24 - مسائل 13, 39, 51
"""
import numpy as np
import math


class ExpressionCalculator:

    @staticmethod
    def expression1(x, y):
        return x ** 3 + 2 * x ** 2 + 3 * y - 5

    @staticmethod
    def expression2(m, n):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        return a, b, c

    @staticmethod
    def expression3(a, b):
        sum_squares = a ** 2 + b ** 2
        sum_cubes = a ** 3 + b ** 3
        return sum_squares, sum_cubes


def main():
    print("\n--- Mathematical Expressions ---")
    calc = ExpressionCalculator()

    try:
        x = float(input("مقدار x: "))
        y = float(input("مقدار y: "))
        result1 = calc.expression1(x, y)
        print(f"x³ + 2x² + 3y - 5 = {result1}")

        m = float(input("\nمقدار m: "))
        n = float(input("مقدار n: "))
        a, b, c = calc.expression2(m, n)
        print(f"a = m² - n² = {a}")
        print(f"b = 2mn = {b}")
        print(f"c = m² + n² = {c}")

        pythagorean_check = abs(a ** 2 + b ** 2 - c ** 2) < 1e-10
        print(f"بررسی فیثاغورث: a² + b² = c² -> {pythagorean_check}")

        a_val = float(input("\nمقدار a برای عبارت سوم: "))
        b_val = float(input("مقدار b برای عبارت سوم: "))
        squares, cubes = calc.expression3(a_val, b_val)
        print(f"a² + b² = {squares}")
        print(f"a³ + b³ = {cubes}")

        print("\nتحلیل ریاضی:")
        print(f"(a + b)² = {(a_val + b_val) ** 2}")
        print(f"(a + b)³ = {(a_val + b_val) ** 3}")

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()