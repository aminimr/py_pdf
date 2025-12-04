"""
تبدیل واحدها
Reference: صفحات 8, 12, 14, 22 - مسائل 8, 20, 25, 46
"""
import numpy as np
import pandas as pd


class UnitConverter:

    @staticmethod
    def kg_to_grams(kg):
        return kg * 1000

    @staticmethod
    def years_to_seconds(years):
        return years * 365.25 * 24 * 60 * 60

    @staticmethod
    def years_to_minutes(years):
        return years * 365.25 * 24 * 60

    @staticmethod
    def miles_feet_to_km_meters(miles, feet):
        M_PER_MILE = 1609.35
        M_PER_FOOT = 0.30480

        total_meters = miles * M_PER_MILE + feet * M_PER_FOOT
        kilometers = int(total_meters / 1000)
        meters = total_meters - kilometers * 1000

        return kilometers, meters

    @staticmethod
    def fuel_consumption(distance_km, fuel_liters):
        return (fuel_liters / distance_km) * 100  # لیتر در 100 کیلومتر


def main():
    print("\n--- Unit Conversions ---")
    converter = UnitConverter()

    try:
        kg = float(input("وزن بر حسب کیلوگرم: "))
        grams = converter.kg_to_grams(kg)
        print(f"{kg} kg = {grams} grams")

        years = float(input("\nسن بر حسب سال: "))
        seconds = converter.years_to_seconds(years)
        minutes = converter.years_to_minutes(years)
        print(f"{years} years = {seconds:,.0f} seconds")
        print(f"{years} years = {minutes:,.0f} minutes")

        miles = float(input("\nمسافت بر حسب مایل: "))
        feet = float(input("مسافت بر حسب فوت: "))
        km, meters = converter.miles_feet_to_km_meters(miles, feet)
        print(f"{miles} miles + {feet} feet = {km} km + {meters:.2f} meters")

        distance = float(input("\nمسافت طی شده (کیلومتر): "))
        fuel = float(input("سوخت مصرفی (لیتر): "))
        consumption = converter.fuel_consumption(distance, fuel)
        print(f"مصرف سوخت: {consumption:.2f} لیتر در 100 کیلومتر")

        conversions_data = []
        test_values = [1, 2.5, 5, 10]

        for val in test_values:
            conversions_data.append({
                'Value': val,
                'kg_to_g': converter.kg_to_grams(val),
                'years_to_sec': converter.years_to_seconds(val),
                'years_to_min': converter.years_to_minutes(val)
            })

        conversions_df = pd.DataFrame(conversions_data)
        print("\nجدول تبدیل‌ها:")
        print(conversions_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()