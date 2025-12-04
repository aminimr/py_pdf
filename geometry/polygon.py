"""
محاسبه مساحت چندضلعی منتظم
Reference: صفحه 6 - مسئله 4
"""
import numpy as np
import math


def regular_polygon_area(n_sides, side_length):
    return (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))


def main():
    print("\n--- Regular Polygon Area ---")
    try:
        n_sides = int(input("تعداد اضلاع را وارد کنید: "))
        side_length = float(input("طول هر ضلع را وارد کنید: "))

        area = regular_polygon_area(n_sides, side_length)
        print(f"مساحت چندضلعی: {area:.2f}")

        polygons = [3, 4, 5, 6, 8, n_sides]
        areas = []

        for sides in polygons:
            a = regular_polygon_area(sides, side_length)
            areas.append(a)
            print(f"{sides}-ضلعی: {a:.2f}")

    except ValueError:
        print("خطا: لطفاً مقادیر عددی صحیح وارد کنید")


if __name__ == "__main__":
    main()