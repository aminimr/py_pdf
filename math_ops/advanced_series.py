"""
سری‌های پیشرفته و دنباله فیبوناچی
Reference: صفحات 36-37 - مسئله 3
"""
import numpy as np
import pandas as pd

class AdvancedSeries:
    """سری‌های ریاضی پیشرفته"""

    @staticmethod
    def fibonacci(n):
        """تولید n جمله اول دنباله فیبوناچی"""
        if n <= 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 1]

        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib

    @staticmethod
    def perfect_numbers(limit):
        """پیدا کردن اعداد کامل تا حد مشخص"""
        perfects = []
        for num in range(2, limit + 1):
            divisors = [i for i in range(1, num) if num % i == 0]
            if sum(divisors) == num:
                perfects.append(num)
        return perfects

    @staticmethod
    def arithmetic_series(first, difference, n):
        """سری حسابی"""
        return [first + i * difference for i in range(n)]

    @staticmethod
    def geometric_series(first, ratio, n):
        """سری هندسی"""
        return [first * (ratio ** i) for i in range(n)]

def main():
    print("\n--- Advanced Mathematical Series ---")
    series = AdvancedSeries()

    try:
        # دنباله فیبوناچی
        n_fib = int(input("تعداد جملات فیبوناچی: "))
        fib_seq = series.fibonacci(n_fib)
        print(f"دنباله فیبوناچی: {fib_seq}")

        # تحلیل فیبوناچی
        if len(fib_seq) >= 3:
            ratios = [fib_seq[i] / fib_seq[i-1] for i in range(2, len(fib_seq))]
            print(f"نسبت‌های متوالی: {ratios}")
            print(f"میانگین نسبت‌ها: {np.mean(ratios):.6f} (نزدیک به نسبت طلایی)")

        # اعداد کامل
        limit = int(input("\nحد بالای جستجوی اعداد کامل: "))
        perfect_nums = series.perfect_numbers(limit)
        print(f"اعداد کامل تا {limit}: {perfect_nums}")

        # سری‌های حسابی و هندسی
        print("\n--- سری‌های ریاضی ---")
        a1 = float(input("جمله اول: "))
        diff = float(input("تفاضل/نسبت: "))
        n_terms = int(input("تعداد جملات: "))

        arith_seq = series.arithmetic_series(a1, diff, n_terms)
        geo_seq = series.geometric_series(a1, diff, n_terms)

        print(f"سری حسابی: {arith_seq}")
        print(f"سری هندسی: {geo_seq}")

        # ایجاد جدول مقایسه
        comparison_data = []
        for i in range(n_terms):
            comparison_data.append({
                'Term': i + 1,
                'Arithmetic': arith_seq[i],
                'Geometric': geo_seq[i],
                'Ratio': geo_seq[i] / arith_seq[i] if arith_seq[i] != 0 else 'Inf'
            })

        comp_df = pd.DataFrame(comparison_data)
        print("\nمقایسه سری‌ها:")
        print(comp_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقادیر عددی صحیح وارد کنید")

if __name__ == "__main__":
    main()