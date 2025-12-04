"""
شاخص سرمایش باد (Wind Chill)
Reference: صفحه 6-7 - مسئله 5
"""
import numpy as np


def calculate_wind_chill(temperature, wind_speed):
    wci = 13.12 + 0.6215 * temperature - 11.37 * (wind_speed ** 0.16) + 0.3965 * temperature * (wind_speed ** 0.16)
    return round(wci)


def main():
    print("\n--- Wind Chill Index ---")
    try:
        wind_speed = float(input("سرعت باد (کیلومتر بر ساعت): "))
        temperature = float(input("دمای هوا (درجه سانتی‌گراد): "))

        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"شاخص سرمایش باد: {wind_chill}")

        temps = np.array([-10, 0, 10, 20])
        winds = np.array([10, 20, 30, 40])

        print("\nتحلیل حساسیت:")
        for temp in temps:
            for wind in winds:
                wci = calculate_wind_chill(temp, wind)
                print(f"دما: {temp}°C, باد: {wind} km/h -> شاخص: {wci}")

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()