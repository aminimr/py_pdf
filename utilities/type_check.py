"""
بررسی نوع داده‌ها
Reference: صفحه 33 - مسئله 78
"""
import numpy as np
import pandas as pd


class TypeChecker:
    """بررسی کننده انواع داده"""

    @staticmethod
    def get_type_info(value):
        """دریافت اطلاعات نوع داده"""
        return {
            'Value': value,
            'Type': type(value).__name__,
            'Python Type': str(type(value)),
            'Memory Size': sys.getsizeof(value),
            'Is Numeric': isinstance(value, (int, float, complex)),
            'Is Sequence': isinstance(value, (str, list, tuple)),
            'Is Callable': callable(value)
        }


def main():
    print("\n--- Data Type Checking ---")
    checker = TypeChecker()

    # دریافت ورودی‌های مختلف
    inputs = []

    try:
        # عدد صحیح
        int_val = int(input("یک عدد صحیح وارد کنید: "))
        inputs.append(int_val)

        # عدد اعشاری
        float_val = float(input("یک عدد اعشاری وارد کنید: "))
        inputs.append(float_val)

        # رشته
        str_val = input("یک رشته وارد کنید: ")
        inputs.append(str_val)

        # لیست
        list_str = input("اعداد برای لیست (با کاما جدا کنید): ")
        if list_str:
            list_val = [float(x.strip()) for x in list_str.split(',')]
            inputs.append(list_val)

        # نمایش اطلاعات انواع
        print("\n=== اطلاعات انواع داده ===")
        type_info_list = []

        for value in inputs:
            info = checker.get_type_info(value)
            type_info_list.append(info)

            print(f"\nمقدار: {info['Value']}")
            print(f"  نوع: {info['Type']}")
            print(f"  نوع پایتون: {info['Python Type']}")
            print(f"  اندازه حافظه: {info['Memory Size']} بایت")
            print(f"  عددی است: {info['Is Numeric']}")
            print(f"  دنباله است: {info['Is Sequence']}")

        # ایجاد جدول مقایسه
        if type_info_list:
            df = pd.DataFrame(type_info_list)
            print("\nجدول مقایسه انواع داده:")
            print(df[['Value', 'Type', 'Memory Size', 'Is Numeric']].to_string(index=False))

        # تحلیل آماری داده‌های عددی
        numeric_values = [x for x in inputs if isinstance(x, (int, float))]
        if numeric_values:
            print(f"\nتحلیل داده‌های عددی ({len(numeric_values)} مقدار):")
            arr = np.array(numeric_values)
            print(f"  مجموع: {arr.sum()}")
            print(f"  میانگین: {arr.mean():.2f}")
            print(f"  انحراف معیار: {arr.std():.2f}")
            print(f"  محدوده: {arr.min()} تا {arr.max()}")

    except ValueError as e:
        print(f"خطا در ورودی: {e}")


if __name__ == "__main__":
    import sys

    main()