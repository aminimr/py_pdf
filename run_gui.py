import os
import sys
import subprocess


def install_requirements():
    """نصب خودکار requirements"""
    requirements = ["numpy", "pandas", "python-dateutil", "numpy-financial"]

    print("🔍 بررسی وابستگی‌ها...")

    for package in requirements:
        try:
            if package == "python-dateutil":
                import dateutil
            elif package == "numpy-financial":
                import numpy_financial
            else:
                __import__(package)
            print(f"✅ {package} نصب است")
        except ImportError:
            print(f"📦 در حال نصب {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"✅ {package} با موفقیت نصب شد")
            except subprocess.CalledProcessError:
                print(f"❌ خطا در نصب {package}")
                return False
    return True


def main():
    """تابع اصلی"""
    print("🚀 راه‌اندازی برنامه گرافیکی مسائل پایتون")
    print("=" * 50)

    # نصب وابستگی‌ها
    if not install_requirements():
        print("❌ برخی وابستگی‌ها نصب نشدند. برنامه متوقف شد.")
        input("Enter برای خروج...")
        return

    # اجرای برنامه گرافیکی
    try:
        from gui_app import main as gui_main
        print("✅ اجرای رابط گرافیکی...")
        gui_main()
    except ImportError as e:
        print(f"❌ خطا در ایمپورت ماژول‌ها: {e}")
        input("Enter برای خروج...")
    except Exception as e:
        print(f"❌ خطای ناشناخته: {e}")
        input("Enter برای خروج...")


if __name__ == "__main__":
    main()