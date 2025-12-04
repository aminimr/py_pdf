"""
محاسبه نرخ تورم و قیمت آینده
Reference: صفحه 9 - مسئله 10
"""
import numpy as np
import pandas as pd


def calculate_inflation(price_year1, price_year2):
    inflation_rate = (price_year2 - price_year1) / price_year1
    return inflation_rate


def predict_future_price(current_price, inflation_rate, years):
    return current_price * (1 + inflation_rate) ** years


def main():
    print("\n--- Inflation Calculator ---")
    try:
        y1 = float(input("قیمت سال قبل: "))
        y2 = float(input("قیمت سال جاری: "))

        inflation = calculate_inflation(y1, y2)
        print(f"نرخ تورم: {inflation:.2%}")

        years = int(input("تعداد سال برای پیش‌بینی: "))

        future_prices = []
        for year in range(1, years + 1):
            future_price = predict_future_price(y2, inflation, year)
            future_prices.append(future_price)
            print(f"سال {year}: {future_price:,.0f}")

        # ایجاد جدول پیش‌بینی
        forecast_df = pd.DataFrame({
            'Year': range(1, years + 1),
            'Predicted Price': future_prices,
            'Inflation Rate': [inflation] * years
        })

        print("\nجدول پیش‌بینی:")
        print(forecast_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()