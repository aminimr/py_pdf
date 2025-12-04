"""
محاسبه حقوق خالص با کسر بیمه و مالیات
Reference: صفحه 8 - مسئله 9
"""
import pandas as pd


def calculate_net_salary(gross_salary, insurance_rate=0.07, tax_rate=0.10):
    """محاسبه حقوق خالص"""
    insurance = gross_salary * insurance_rate
    tax = gross_salary * tax_rate
    net_salary = gross_salary - insurance - tax
    return insurance, tax, net_salary


def main():
    print("\n--- Salary Calculation ---")
    try:
        gross_salary = float(input("حقوق پایه را وارد کنید: "))

        insurance, tax, net_salary = calculate_net_salary(gross_salary)

        # ایجاد دیتافریم برای نمایش نتایج
        data = {
            'Item': ['Gross Salary', 'Insurance (7%)', 'Tax (10%)', 'Net Salary'],
            'Amount': [gross_salary, insurance, tax, net_salary]
        }
        df = pd.DataFrame(data)
        print("\nمحاسبه حقوق:")
        print(df.to_string(index=False))

        # تحلیل برای حقوق‌های مختلف
        salaries = [gross_salary * 0.5, gross_salary, gross_salary * 1.5, gross_salary * 2]
        results = []

        for salary in salaries:
            ins, tx, net = calculate_net_salary(salary)
            results.append({
                'Gross Salary': salary,
                'Insurance': ins,
                'Tax': tx,
                'Net Salary': net
            })

        analysis_df = pd.DataFrame(results)
        print("\nتحلیل برای سطوح مختلف حقوق:")
        print(analysis_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقدار عددی وارد کنید")


if __name__ == "__main__":
    main()