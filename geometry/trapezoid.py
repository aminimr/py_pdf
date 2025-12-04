"""
محاسبه مساحت ذوزنقه
Reference: صفحه 31 - مسئله 71
"""
import numpy as np


def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height


def main():
    print("\n--- Trapezoid Area ---")
    try:
        a = float(input("قاعده کوچک را وارد کنید: "))
        b = float(input("قاعده بزرگ را وارد کنید: "))
        c = float(input("ارتفاع را وارد کنید: "))

        area = trapezoid_area(a, b, c)
        print(f"مساحت ذوزنقه: {area:.2f}")

        import pandas as pd

        heights = np.array([c * 0.5, c, c * 1.5, c * 2])
        areas = [trapezoid_area(a, b, h) for h in heights]

        sensitivity_df = pd.DataFrame({
            'Height': heights,
            'Area': areas,
            'Change %': [(area - areas[0]) / areas[0] * 100 for area in areas]
        })

        print("\nتحلیل حساسیت نسبت به ارتفاع:")
        print(sensitivity_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()