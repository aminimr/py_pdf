"""
حجم و مساحت استوانه
Reference: صفحه 5 - مسئله 2
"""
import numpy as np
import math


def calculate_cylinder_properties(radius, height):
    volume = math.pi * radius ** 2 * height
    surface_area = 2 * math.pi * radius * (radius + height)
    return volume, surface_area


def main():
    print("\n--- Cylinder Properties ---")
    try:
        radius = float(input("شعاع استوانه را وارد کنید: "))
        height = float(input("ارتفاع استوانه را وارد کنید: "))

        volume, surface_area = calculate_cylinder_properties(radius, height)
        print(f"حجم استوانه: {volume:.2f}")
        print(f"مساحت سطح استوانه: {surface_area:.2f}")

        import pandas as pd
        data = {
            'Property': ['Radius', 'Height', 'Volume', 'Surface Area'],
            'Value': [radius, height, volume, surface_area]
        }
        df = pd.DataFrame(data)
        print("\nخلاصه محاسبات:")
        print(df)

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()