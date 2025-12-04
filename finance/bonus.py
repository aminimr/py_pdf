"""
محاسبه پاداش و حقوق
 صفحه 13 - مسئله 21
"""
import pandas as pd


def calculate_bonus(salary, bonus_rate=0.15):
    return salary * bonus_rate


def main():
    print("\n--- Bonus Calculator ---")
    try:
        salary = float(input("حقوق پایه را وارد کنید: "))

        bonus = calculate_bonus(salary)
        total_compensation = salary + bonus

        compensation_data = {
            'Item': ['Base Salary', 'Bonus (15%)', 'Total Compensation'],
            'Amount': [salary, bonus, total_compensation],
            'Percentage': ['100%', '15%', '115%']
        }

        df = pd.DataFrame(compensation_data)
        print("\nگزارش حقوق و پاداش:")
        print(df.to_string(index=False))

        salary_levels = [salary * 0.7, salary, salary * 1.3, salary * 1.6]
        analysis = []

        for level in salary_levels:
            b = calculate_bonus(level)
            total = level + b
            analysis.append({
                'Base Salary': level,
                'Bonus': b,
                'Total': total,
                'Bonus %': (b / level) * 100
            })

        analysis_df = pd.DataFrame(analysis)
        print("\nتحلیل سطوح مختلف حقوق:")
        print(analysis_df.to_string(index=False))

    except ValueError:
        print("خطا: لطفاً مقدار عددی وارد کنید")


if __name__ == "__main__":
    main()