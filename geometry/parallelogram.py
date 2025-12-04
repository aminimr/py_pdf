"""
مساحت متوازی‌الأضلاع
Reference: صفحه 5 - مسئله 1
"""
import numpy as np


def calculate_parallelogram_area(base, height):
    return base * height


def main():
    print("\n--- Parallelogram Area ---")
    try:
        base = float(input("طول قاعده را وارد کنید: "))
        height = float(input("ارتفاع را وارد کنید: "))

        area = calculate_parallelogram_area(base, height)
        print(f"مساحت متوازی‌الأضلاع: {area}")

        dimensions = np.array([base, height, area])
        print(f"ابعاد و مساحت (قاعده، ارتفاع، مساحت): {dimensions}")

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()