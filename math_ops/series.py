"""
محاسبه سری‌های ریاضی
Reference: صفحه 11 - مسئله 17
"""
import numpy as np
import math


def calculate_series(x, n_terms=10):
    """محاسبه سری 1/(x² + x + 1)"""
    return 1.0 / (x * x + x + 1)


def factorial_series(n_terms):
    """محاسبه سری فاکتوریل: 1/1! + 1/2! + ... + 1/n!"""
    total = 0
    fact = 1

    for i in range(1, n_terms + 1):
        fact *= i
        total += 1 / fact

    return total


def main():
    print("\n--- Mathematical Series ---")

    try:
        # سری اول
        x = float(input("مقدار x برای سری اول: "))
        result1 = calculate_series(x)
        print(f"نتیجه سری 1/(x²+x+1): {result1}")

        # سری فاکتوریل
        n = int(input("تعداد جملات سری فاکتوریل: "))
        result2 = factorial_series(n)
        print(f"نتیجه سری فاکتوریل: {result2}")

        # محاسبه خطا
        actual_e = math.e - 1  # e^1 - 1 ≈ سری فاکتوریل برای n بزرگ
        error = abs(actual_e - result2)
        print(f"خطای تقریب: {error:.10f}")

        # تحلیل همگرایی
        convergence = []
        for terms in range(1, min(n + 1, 11)):  # تا 10 جمله اول
            partial_sum = factorial_series(terms)
            convergence.append({
                'Terms': terms,
                'Partial Sum': partial_sum,
                'Error': abs(actual_e - partial_sum)
            })

        if convergence:
            print("\nتحلیل همگرایی:")
            for item in convergence:
                print(f"جملات: {item['Terms']:2d} - مجموع: {item['Partial Sum']:.8f} - خطا: {item['Error']:.8f}")

    except ValueError:
        print("خطا: لطفاً مقادیر عددی صحیح وارد کنید")


if __name__ == "__main__":
    main()