"""
محاسبه ارزش آتی پول
Reference: صفحه 11 - مسئله 16
"""
import numpy as np
import pandas as pd


def future_value(principal, rate, years):
    """محاسبه ارزش آتی"""
    return principal * (1 + rate / 100) ** years


def main():
    print("\n--- Future Value Calculator ---")
    try:
        principal = float(input("مبلغ سرمایه‌گذاری: "))
        rate = float(input("نرخ سود سالانه (%): "))
        years = int(input("تعداد سال: "))

        fv = future_value(principal, rate, years)
        print(f"ارزش آتی: {fv:,.0f}")

        # تحلیل سال به سال
        yearly_growth = []
        for year in range(1, years + 1):
            value = future_value(principal, rate, year)
            yearly_growth.append({
                'Year': year,
                'Value': value,
                'Growth': value - principal
            })

        growth_df = pd.DataFrame(yearly_growth)
        print("\nرشد سال به سال:")
        print(growth_df.to_string(index=False))

        # مقایسه با نرخ‌های مختلف
        rates = [rate * 0.5, rate, rate * 1.5, rate * 2]
        comparison = []

        for r in rates:
            fv_comp = future_value(principal, r, years)
            comparison.append({
                'Rate (%)': r,
                'Future Value': fv_comp,
                'Difference': fv_comp - fv
            })

        comp_df = pd.DataFrame(comparison)
        print("\nمقایسه با نرخ‌های مختلف:")
        print(comp_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()