"""
عملیات تاریخ و زمان
Reference: صفحات 10, 24, 31-32 - مسائل 14, 51, 74-75
"""
import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta


class DateTimeOperations:
    """کلاس برای عملیات تاریخ و زمان"""

    @staticmethod
    def current_datetime():
        """زمان فعلی"""
        return datetime.datetime.now()

    @staticmethod
    def add_seconds(dt, seconds):
        """افزودن ثانیه به تاریخ"""
        return dt + datetime.timedelta(seconds=seconds)

    @staticmethod
    def calculate_age(birth_date, current_date):
        """محاسبه سن"""
        delta = relativedelta(current_date, birth_date)
        return delta.years, delta.months, delta.days

    @staticmethod
    def datetime_to_seconds(dt):
        """تبدیل تاریخ به ثانیه از epoch"""
        return int(dt.timestamp())


def main():
    print("\n--- DateTime Operations ---")

    # ایجاد نمونه کلاس
    dt_ops = DateTimeOperations()

    # زمان فعلی
    now = dt_ops.current_datetime()
    print(f"زمان فعلی: {now}")
    print(f"فرمت‌های مختلف:")
    print(f"  ISO: {now.isoformat()}")
    print(f"  Custom: {now.strftime('%Y-%m-%d %H:%M:%S')}")

    # افزودن ثانیه
    seconds_to_add = int(input("\nثانیه برای افزودن وارد کنید: "))
    future_time = dt_ops.add_seconds(now, seconds_to_add)
    print(f"زمان پس از {seconds_to_add} ثانیه: {future_time}")

    # محاسبه سن
    print("\n--- محاسبه سن ---")
    try:
        birth_year = int(input("سال تولد: "))
        birth_month = int(input("ماه تولد: "))
        birth_day = int(input("روز تولد: "))

        birth_date = datetime.datetime(birth_year, birth_month, birth_day)
        years, months, days = dt_ops.calculate_age(birth_date, now)

        print(f"سن: {years} سال, {months} ماه, {days} روز")

        # ایجاد جدول زمانی
        dates = pd.date_range(birth_date, now, freq='YS')  # سالانه
        ages = [dt_ops.calculate_age(birth_date, date)[0] for date in dates]

        timeline_df = pd.DataFrame({
            'Date': dates,
            'Age': ages
        })
        print("\nخط زمانی سن:")
        print(timeline_df.to_string(index=False))

    except ValueError as e:
        print(f"خطا در ورودی تاریخ: {e}")


if __name__ == "__main__":
    main()