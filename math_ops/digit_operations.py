"""
عملیات روی ارقام اعداد
Reference: صفحه 9-10 - مسئله 12
"""
import numpy as np


def reverse_and_sum(number):
    """معکوس کردن عدد و جمع ارقام"""
    # تبدیل به رشته برای معکوس کردن
    str_num = str(number)
    reversed_num = int(str_num[::-1])

    # جمع ارقام
    digit_sum = sum(int(digit) for digit in str_num)

    return reversed_num, digit_sum


def extract_digits(number):
    """جدا کردن ارقام عدد"""
    digits = [int(digit) for digit in str(number)]
    return digits


def main():
    print("\n--- Digit Operations ---")
    try:
        number = int(input("یک عدد وارد کنید: "))

        reversed_num, digit_sum = reverse_and_sum(number)
        digits = extract_digits(number)

        print(f"عدد اصلی: {number}")
        print(f"معکوس عدد: {reversed_num}")
        print(f"مجموع ارقام: {digit_sum}")
        print(f"ارقام: {digits}")

        # تحلیل آماری با numpy
        digits_array = np.array(digits)
        print(f"\nتحلیل آماری ارقام:")
        print(f"میانگین ارقام: {np.mean(digits_array):.2f}")
        print(f"انحراف معیار: {np.std(digits_array):.2f}")
        print(f"بیشترین رقم: {np.max(digits_array)}")
        print(f"کمترین رقم: {np.min(digits_array)}")

    except ValueError:
        print("خطا: لطفاً یک عدد صحیح وارد کنید")


if __name__ == "__main__":
    main()