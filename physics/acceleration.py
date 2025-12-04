"""
محاسبه شتاب
Reference: صفحه 14 - مسئله 24
"""
import numpy as np
import pandas as pd


def calculate_acceleration(initial_velocity, final_velocity, time_minutes):
    time_seconds = time_minutes * 60  # تبدیل به ثانیه
    return (final_velocity - initial_velocity) * 60 / time_minutes


def main():
    print("\n--- Acceleration Calculation ---")
    try:
        k = float(input("سرعت نهایی (km/h): "))
        x = float(input("سرعت اولیه (km/h): "))
        n = float(input("زمان (دقیقه): "))

        acceleration = calculate_acceleration(x, k, n)
        print(f"شتاب: {acceleration:.2f} km/h²")

        time_points = np.linspace(0, n, 10)  # 10 نقطه زمانی
        velocities = x + (acceleration / 60) * time_points  # سرعت در هر لحظه

        motion_df = pd.DataFrame({
            'Time (min)': time_points,
            'Velocity (km/h)': velocities,
            'Acceleration': [acceleration] * len(time_points)
        })

        print("\nتحلیل حرکت:")
        print(motion_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()