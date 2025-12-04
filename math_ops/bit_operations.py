"""
عملیات بیتی روی اعداد
Reference: صفحات 29-31 - مسائل 65-70
"""
import numpy as np


class BitOperations:

    @staticmethod
    def check_bit(number, n):
        return (number >> n) & 1

    @staticmethod
    def set_bit(number, n):
        return number | (1 << n)

    @staticmethod
    def clear_bit(number, n):
        return number & ~(1 << n)

    @staticmethod
    def toggle_bit(number, n):
        return number ^ (1 << n)

    @staticmethod
    def swap_with_xor(a, b):
        a ^= b
        b ^= a
        a ^= b
        return a, b


def main():
    print("\n--- Bit Operations ---")
    try:
        num = int(input("عدد اول را وارد کنید: "))
        bit_pos = int(input("موقعیت بیت (0-31) را وارد کنید: "))

        bit_ops = BitOperations()

        bit_status = bit_ops.check_bit(num, bit_pos)
        set_result = bit_ops.set_bit(num, bit_pos)
        clear_result = bit_ops.clear_bit(num, bit_pos)
        toggle_result = bit_ops.toggle_bit(num, bit_pos)

        print(f"\nنتایج عملیات بیتی:")
        print(f"وضعیت بیت {bit_pos}: {bit_status}")
        print(f"پس از تنظیم بیت: {set_result}")
        print(f"پس از پاک کردن بیت: {clear_result}")
        print(f"پس از تغییر وضعیت بیت: {toggle_result}")

        num2 = int(input("\nعدد دوم برای تعویض وارد کنید: "))
        swapped1, swapped2 = bit_ops.swap_with_xor(num, num2)
        print(f"پس از تعویض: {swapped1}, {swapped2}")

        print(f"\nنمایش باینری:")
        print(f"{num:032b} = {num}")
        print(f"{num2:032b} = {num2}")

    except ValueError:
        print("خطا: لطفاً اعداد صحیح وارد کنید")


if __name__ == "__main__":
    main()