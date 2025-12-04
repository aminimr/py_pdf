"""
محاسبات پیشرفته فیزیکی
Reference: صفحات 13-14 - مسائل 22-23
"""
import numpy as np
import pandas as pd
import math


class AdvancedPhysics:
    """محاسبات پیشرفته فیزیکی"""

    @staticmethod
    def distance_2d(x1, y1, x2, y2):
        """محاسبه فاصله بین دو نقطه در صفحه"""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    @staticmethod
    def line_intersection(a1, b1, c1, a2, b2, c2):
        """پیدا کردن نقطه تقاطع دو خط"""
        # معادلات: a1x + b1y = c1 و a2x + b2y = c2
        determinant = a1 * b2 - a2 * b1

        if determinant == 0:
            return None  # خطوط موازی

        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return x, y

    @staticmethod
    def trigonometric_calculation(angle_degrees, amplitude=1):
        """محاسبات مثلثاتی"""
        angle_rad = math.radians(angle_degrees)
        return {
            'sin': amplitude * math.sin(angle_rad),
            'cos': amplitude * math.cos(angle_rad),
            'tan': amplitude * math.tan(angle_rad) if angle_degrees % 90 != 0 else 'Undefined',
            'radians': angle_rad
        }


def main():
    print("\n--- Advanced Physics Calculations ---")
    physics = AdvancedPhysics()

    try:
        # فاصله بین دو نقطه
        print("--- محاسبه فاصله بین دو نقطه ---")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))

        distance = physics.distance_2d(x1, y1, x2, y2)
        print(f"فاصله بین نقاط: {distance:.2f}")

        # نقطه تقاطع دو خط
        print("\n--- نقطه تقاطع دو خط ---")
        print("معادله اول: a1x + b1y = c1")
        a1 = float(input("a1: "))
        b1 = float(input("b1: "))
        c1 = float(input("c1: "))

        print("معادله دوم: a2x + b2y = c2")
        a2 = float(input("a2: "))
        b2 = float(input("b2: "))
        c2 = float(input("c2: "))

        intersection = physics.line_intersection(a1, b1, c1, a2, b2, c2)
        if intersection:
            x, y = intersection
            print(f"نقطه تقاطع: ({x:.2f}, {y:.2f})")
        else:
            print("خطوط موازی هستند - نقطه تقاطع وجود ندارد")

        # محاسبات مثلثاتی
        print("\n--- محاسبات مثلثاتی ---")
        angle = float(input("زاویه (درجه): "))
        amplitude = float(input("دامنه: ") or 1)

        trig_results = physics.trigonometric_calculation(angle, amplitude)
        print("نتایج مثلثاتی:")
        for func, value in trig_results.items():
            print(f"  {func}: {value}")

        # تحلیل برای زوایای مختلف
        angles = np.array([0, 30, 45, 60, 90, 180])
        analysis_data = []

        for ang in angles:
            results = physics.trigonometric_calculation(ang)
            analysis_data.append({
                'Angle (deg)': ang,
                'sin': results['sin'],
                'cos': results['cos'],
                'radians': results['radians']
            })

        analysis_df = pd.DataFrame(analysis_data)
        print("\nتحلیل برای زوایای مختلف:")
        print(analysis_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()