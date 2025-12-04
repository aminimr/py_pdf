"""
محاسبات وام و اقساط
Reference: صفحات 37-38 - مسئله 5
"""
import numpy as np
import pandas as pd


class LoanCalculator:
    """ماشین حساب وام"""

    @staticmethod
    def calculate_loan(principal, annual_rate, months):
        """محاسبه وام با بهره"""
        monthly_rate = annual_rate / 1200  # تبدیل به نرخ ماهانه
        total_interest = principal * (months + 1) * monthly_rate
        total_payment = principal + total_interest
        monthly_payment = total_payment / months
        return total_payment, monthly_payment, total_interest

    @staticmethod
    def calculate_compound_loan(principal, annual_rate, months):
        """محاسبه وام با بهره مرکب"""
        monthly_rate = annual_rate / 1200
        monthly_payment = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)
        total_payment = monthly_payment * months
        total_interest = total_payment - principal
        return total_payment, monthly_payment, total_interest


def main():
    print("\n--- Loan Calculations ---")
    calculator = LoanCalculator()

    try:
        principal = float(input("مبلغ وام: "))
        annual_rate = float(input("نرخ بهره سالانه (%): "))
        months = int(input("تعداد اقساط (ماه): "))

        print(f"\n📊 محاسبات وام:")
        print(f"مبلغ وام: {principal:,.0f}")
        print(f"نرخ بهره سالانه: {annual_rate}%")
        print(f"تعداد اقساط: {months} ماه")

        # محاسبه بهره ساده
        total_simple, monthly_simple, interest_simple = calculator.calculate_loan(principal, annual_rate, months)

        print(f"\n💡 محاسبه بهره ساده:")
        print(f"قسط ماهانه: {monthly_simple:,.0f}")
        print(f"کل پرداختی: {total_simple:,.0f}")
        print(f"بهره کل: {interest_simple:,.0f}")

        # محاسبه بهره مرکب
        total_compound, monthly_compound, interest_compound = calculator.calculate_compound_loan(principal, annual_rate,
                                                                                                 months)

        print(f"\n💡 محاسبه بهره مرکب:")
        print(f"قسط ماهانه: {monthly_compound:,.0f}")
        print(f"کل پرداختی: {total_compound:,.0f}")
        print(f"بهره کل: {interest_compound:,.0f}")

        # مقایسه
        difference = total_compound - total_simple
        print(f"\n📈 مقایسه:")
        print(f"تفاوت کل پرداختی: {difference:,.0f}")
        print(f"تفاوت قسط ماهانه: {monthly_compound - monthly_simple:,.0f}")

        # تحلیل برای دوره‌های مختلف
        periods = [12, 24, 36, 48, 60]  # 1 تا 5 سال
        analysis_data = []

        for period in periods:
            _, monthly, interest = calculator.calculate_compound_loan(principal, annual_rate, period)
            analysis_data.append({
                'Months': period,
                'Years': period // 12,
                'Monthly Payment': monthly,
                'Total Interest': interest,
                'Interest/Principal Ratio': interest / principal
            })

        analysis_df = pd.DataFrame(analysis_data)
        print("\n📋 تحلیل برای دوره‌های مختلف:")
        print(analysis_df.to_string(index=False, float_format='%.0f'))

    except ValueError:
        print("❌ خطا: لطفاً مقادیر عددی وارد کنید")
    except ZeroDivisionError:
        print("❌ خطا: تعداد اقساط نمی‌تواند صفر باشد")


if __name__ == "__main__":
    main()