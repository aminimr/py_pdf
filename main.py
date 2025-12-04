import importlib
import sys
import os
from typing import List, Dict

try:
    import colorama
    colorama.init()
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False

class ProblemRunner:

    def __init__(self):
        self.modules = self._get_modules_list()

    def _get_modules_list(self) -> List[Dict]:
        return [
            {"category": "Geometry", "module": "geometry.parallelogram", "name": "مساحت متوازی الاضلاع"},
            {"category": "Geometry", "module": "geometry.cylinder", "name": "حجم و مساحت استوانه"},
            {"category": "Geometry", "module": "geometry.sphere", "name": "مساحت و حجم کره"},
            {"category": "Geometry", "module": "geometry.polygon", "name": "مساحت چندضلعی منتظم"},
            {"category": "Geometry", "module": "geometry.trapezoid", "name": "مساحت ذوزنقه"},

            # ---------------------------------------------------------------------------------------

            {"category": "Physics", "module": "physics.wind_chill", "name": "شاخص سرمایش باد"},
            {"category": "Physics", "module": "physics.acceleration", "name": "محاسبه شتاب"},
            {"category": "Physics", "module": "physics.resistance", "name": "مقاومت الکتریکی"},
            {"category": "Physics", "module": "physics.advanced_calculations", "name": "محاسبات پیشرفته فیزیکی"},

            # ---------------------------------------------------------------------------------------

            {"category": "Finance", "module": "finance.salary", "name": "محاسبه حقوق خالص"},
            {"category": "Finance", "module": "finance.inflation", "name": "محاسبه تورم"},
            {"category": "Finance", "module": "finance.future_value", "name": "ارزش آتی پول"},
            {"category": "Finance", "module": "finance.bonus", "name": "محاسبه پاداش"},
            {"category": "Finance", "module": "finance.loan_calculations", "name": "محاسبات وام"},

            # ---------------------------------------------------------------------------------------

            {"category": "Math Operations", "module": "math_ops.digit_operations", "name": "عملیات روی ارقام"},
            {"category": "Math Operations", "module": "math_ops.bit_operations", "name": "عملیات بیتی"},
            {"category": "Math Operations", "module": "math_ops.complex_numbers", "name": "اعداد مختلط"},
            {"category": "Math Operations", "module": "math_ops.series", "name": "سری های ریاضی"},
            {"category": "Math Operations", "module": "math_ops.expressions", "name": "عبارات ریاضی"},
            {"category": "Math Operations", "module": "math_ops.advanced_series", "name": "سری های پیشرفته"},

            # ---------------------------------------------------------------------------------------

            {"category": "Utilities", "module": "utilities.datetime_ops", "name": "عملیات تاریخ و زمان"},
            {"category": "Utilities", "module": "utilities.string_ops", "name": "عملیات رشته ای"},
            {"category": "Utilities", "module": "utilities.conversions", "name": "تبدیل واحدها"},
            {"category": "Utilities", "module": "utilities.system_info", "name": "اطلاعات سیستم"},
            {"category": "Utilities", "module": "utilities.type_check", "name": "بررسی نوع داده"},
        ]

    def print_colored(self, text, color=None):
        if HAS_COLORAMA and color:
            color_codes = {
                'red': colorama.Fore.RED,
                'green': colorama.Fore.GREEN,
                'yellow': colorama.Fore.YELLOW,
                'blue': colorama.Fore.BLUE,
                'magenta': colorama.Fore.MAGENTA,
                'cyan': colorama.Fore.CYAN,
                'white': colorama.Fore.WHITE,
                'reset': colorama.Fore.RESET
            }
            print(f"{color_codes.get(color, '')}{text}{color_codes['reset']}")
        else:
            print(text)

    def setup_console(self):
        if os.name == 'nt':  # Windows
            try:
                os.system('chcp 65001 > nul')
                os.system('powershell -Command "Set-ItemProperty HKCU:\\Console VirtualTerminalLevel -Type DWORD 1"')
            except:
                pass

    def run_single_module(self, module_path: str):
        try:
            module = importlib.import_module(module_path)
            if hasattr(module, 'main'):
                print(f"\n{'='*60}")
                self.print_colored(f"در حال اجرای: {module_path}", 'green')
                print(f"{'='*60}")
                module.main()
            else:
                self.print_colored(f"  تابع main() در ماژول {module_path} یافت نشد", 'yellow')
        except ImportError as e:
            self.print_colored(f" خطا در ایمپورت ماژول {module_path}: {e}", 'red')
        except Exception as e:
            self.print_colored(f" خطا در اجرای ماژول {module_path}: {e}", 'red')

    def run_by_category(self, category: str):
        category_modules = [m for m in self.modules if m["category"] == category]

        if not category_modules:
            print(f"دسته‌بندی '{category}' یافت نشد")
            return

        self.print_colored(f"\n اجرای دسته‌بندی: {category}", 'cyan')
        print("=" * 50)

        for module_info in category_modules:
            print(f"\n در حال اجرای: {module_info['name']}")
            print("-" * 30)
            self.run_single_module(module_info["module"])

    def run_all(self):
        self.print_colored(" شروع اجرای تمام مسائل پایتون", 'green')
        print("=" * 60)

        current_category = None
        for module_info in self.modules:
            if module_info["category"] != current_category:
                current_category = module_info["category"]
                print(f"\n دسته‌بندی: {current_category}")
                print("=" * 40)

            print(f"\n  در حال اجرای: {module_info['name']}")
            print("-" * 35)
            self.run_single_module(module_info["module"])

        self.print_colored("\nاجرای تمام مسائل به پایان رسید!", 'green')

    def show_menu(self):
        print("\n" + "=" * 60)
        self.print_colored(" پروژه حل مسائل پایتون - منوی اصلی", 'cyan')
        print("=" * 60)

        categories = sorted(set(m["category"] for m in self.modules))
        print("\nدسته‌بندی های موجود:")
        for i, category in enumerate(categories, 1):
            count = len([m for m in self.modules if m["category"] == category])
            print(f"  {i}. {category} ({count} مسئله)")

        print(f"  {len(categories) + 1}. اجرای تمام مسائل")
        print(f"  {len(categories) + 2}. خروج")

    def interactive_menu(self):
        while True:
            self.show_menu()

            try:
                choice = input("\nانتخاب شما (عدد): ").strip()

                if choice == "":
                    continue

                categories = sorted(set(m["category"] for m in self.modules))

                if choice.isdigit():
                    choice_num = int(choice)

                    if 1 <= choice_num <= len(categories):
                        selected_category = categories[choice_num - 1]
                        self.run_by_category(selected_category)

                    elif choice_num == len(categories) + 1:
                        self.run_all()

                    elif choice_num == len(categories) + 2:
                        break
                    else:
                        self.print_colored("انتخاب نامعتبر!", 'red')

                else:
                    matching_modules = [
                        m for m in self.modules
                        if choice.lower() in m["name"].lower() or choice.lower() in m["module"].lower()
                    ]

                    if matching_modules:
                        for module_info in matching_modules:
                            self.run_single_module(module_info["module"])
                    else:
                        self.print_colored(" ماژول یافت نشد!", 'red')

            except KeyboardInterrupt:
                break
            except Exception as e:
                self.print_colored(f" خطای ناشناخته: {e}", 'red')

def check_dependencies():
    required_packages = ['numpy', 'pandas']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)

    if missing_packages:
        print(" پکیج های زیر نصب نیستند:")
        for pkg in missing_packages:
            print(f"   - {pkg}")
        print("\n💡 برای نصب از دستور زیر استفاده کنید:")
        print("   pip install numpy pandas")
        return False

    return True

def main():
    runner = ProblemRunner()
    runner.setup_console()

    print(" در حال بررسی وابستگی ها...")

    if not check_dependencies():
        print("\n  لطفا ابتدا وابستگی ها را نصب کنید")
        return

    print("تمام وابستگی ها نصب هستند!")

    if len(sys.argv) > 1:
        if sys.argv[1] == "--all":
            runner.run_all()
        elif sys.argv[1] == "--category":
            if len(sys.argv) > 2:
                runner.run_by_category(sys.argv[2])
            else:
                print(" نام دسته بندی را مشخص کنید")
        elif sys.argv[1] == "--module":
            if len(sys.argv) > 2:
                runner.run_single_module(sys.argv[2])
            else:
                print(" نام ماژول را مشخص کنید")
        else:
            runner.interactive_menu()
    else:
        runner.interactive_menu()

if __name__ == "__main__":
    main()