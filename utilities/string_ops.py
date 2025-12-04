"""
عملیات روی رشته‌ها
Reference: صفحات 7, 16, 28 - مسائل 6, 30, 63
"""
import numpy as np
import pandas as pd


class StringOperations:

    @staticmethod
    def repeat_string(s, n):
        return s * n

    @staticmethod
    def string_statistics(s):
        return {
            'Length': len(s),
            'Words': len(s.split()),
            'Uppercase': sum(1 for c in s if c.isupper()),
            'Lowercase': sum(1 for c in s if c.islower()),
            'Digits': sum(1 for c in s if c.isdigit()),
            'Spaces': sum(1 for c in s if c.isspace())
        }

    @staticmethod
    def char_to_ascii(ch):
        return ord(ch)

    @staticmethod
    def spaced_string(s):
        return ' '.join(s)


def main():
    print("\n--- String Operations ---")
    ops = StringOperations()

    text = input("یک رشته وارد کنید: ")
    repeat_count = int(input("تعداد تکرار: "))
    repeated = ops.repeat_string(text, repeat_count)
    print(f"رشته تکرار شده: {repeated}")
    stats = ops.string_statistics(text)
    print("\nآمار رشته:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    if text:
        first_char = text[0]
        ascii_code = ops.char_to_ascii(first_char)
        print(f"\nکد ASCII کاراکتر اول ('{first_char}'): {ascii_code}")

    spaced = ops.spaced_string(text)
    print(f"رشته با فاصله: {spaced}")

    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1

    if char_freq:
        freq_df = pd.DataFrame({
            'Character': list(char_freq.keys()),
            'Frequency': list(char_freq.values())
        }).sort_values('Frequency', ascending=False)

        print("\nفراوانی کاراکترها:")
        print(freq_df.to_string(index=False))


if __name__ == "__main__":
    main()