"""
محاسبه مقاومت الکتریکی
Reference: صفحه 12 - مسئله 19
"""
import numpy as np


def parallel_resistance(resistances):
    return 1 / sum(1 / r for r in resistances)


def series_resistance(resistances):
    return sum(resistances)


def main():
    print("\n--- Electrical Resistance Calculator ---")
    try:
        r1 = float(input("مقاومت اول (Ω): "))
        r2 = float(input("مقاومت دوم (Ω): "))
        r3 = float(input("مقاومت سوم (Ω): "))

        resistances = [r1, r2, r3]

        parallel_eq = parallel_resistance(resistances)
        series_eq = series_resistance(resistances)

        print(f"\nنتایج:")
        print(f"مقاومت معادل موازی: {parallel_eq:.2f} Ω")
        print(f"مقاومت معادل سری: {series_eq:.2f} Ω")

        combinations = [
            [r1, r2],
            [r1, r3],
            [r2, r3],
            [r1, r2, r3]
        ]

        print("\nتحلیل ترکیبات مختلف:")
        for i, combo in enumerate(combinations, 1):
            p_eq = parallel_resistance(combo)
            s_eq = series_resistance(combo)
            print(f"ترکیب {i}: {combo} -> موازی: {p_eq:.2f}Ω, سری: {s_eq:.2f}Ω")

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()