"""
مساحت و حجم کره
Reference: صفحه 5-6 - مسئله 3
"""
import numpy as np
import math


def calculate_sphere_properties(radius):
    surface_area = 4 * math.pi * radius ** 2
    volume = (4 / 3) * math.pi * radius ** 3
    return surface_area, volume


def main():
    print("\n--- Sphere Properties ---")
    try:
        radius = float(input("شعاع کره را وارد کنید: "))

        surface_area, volume = calculate_sphere_properties(radius)
        print(f"مساحت سطح کره: {surface_area:.2f}")
        print(f"حجم کره: {volume:.2f}")

        radii = np.array([radius, radius / 2, radius * 2])
        surface_areas = 4 * math.pi * radii ** 2
        volumes = (4 / 3) * math.pi * radii ** 3

        print("\nمقایسه با شعاع‌های مختلف:")
        for r, sa, v in zip(radii, surface_areas, volumes):
            print(f"شعاع: {r:.1f}, مساحت: {sa:.2f}, حجم: {v:.2f}")

    except ValueError:
        print("خطا: لطفاً مقدار عددی وارد کنید")


if __name__ == "__main__":
    main()