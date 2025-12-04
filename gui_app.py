"""
Python Problems GUI Application
یک رابط گرافیکی برای اجرای مسائل پایتون
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import importlib
import sys
import threading
import io
import contextlib
from typing import List, Dict

class OutputRedirector(io.StringIO):
    """کلاس برای redirect کردن خروجی"""
    def __init__(self, text_widget, tag=None):
        io.StringIO.__init__(self)
        self.text_widget = text_widget
        self.tag = tag

    def write(self, string):
        self.text_widget.insert(tk.END, string, self.tag)
        self.text_widget.see(tk.END)
        self.text_widget.update_idletasks()

    def flush(self):
        pass

class PythonProblemsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 پروژه مسائل پایتون")
        self.root.geometry("1000x700")

        self.modules = self._get_modules_list()
        self.current_output_redirector = None
        self.is_running = False
        self.setup_gui()

    def _get_modules_list(self) -> List[Dict]:
        """لیست تمام ماژول‌های قابل اجرا"""
        return [
            # هندسی
            {"category": "Geometry", "module": "geometry.parallelogram", "name": "مساحت متوازی‌الأضلاع", "page": "5"},
            {"category": "Geometry", "module": "geometry.cylinder", "name": "حجم و مساحت استوانه", "page": "5"},
            {"category": "Geometry", "module": "geometry.sphere", "name": "مساحت و حجم کره", "page": "5-6"},
            {"category": "Geometry", "module": "geometry.polygon", "name": "مساحت چندضلعی منتظم", "page": "6"},
            {"category": "Geometry", "module": "geometry.trapezoid", "name": "مساحت ذوزنقه", "page": "31"},

            # فیزیک
            {"category": "Physics", "module": "physics.wind_chill", "name": "شاخص سرمایش باد", "page": "6-7"},
            {"category": "Physics", "module": "physics.acceleration", "name": "محاسبه شتاب", "page": "14"},
            {"category": "Physics", "module": "physics.resistance", "name": "مقاومت الکتریکی", "page": "12"},
            {"category": "Physics", "module": "physics.advanced_calculations", "name": "محاسبات پیشرفته فیزیکی", "page": "13-14"},

            # مالی
            {"category": "Finance", "module": "finance.salary", "name": "محاسبه حقوق خالص", "page": "8"},
            {"category": "Finance", "module": "finance.inflation", "name": "محاسبه تورم", "page": "9"},
            {"category": "Finance", "module": "finance.future_value", "name": "ارزش آتی پول", "page": "11"},
            {"category": "Finance", "module": "finance.bonus", "name": "محاسبه پاداش", "page": "13"},
            {"category": "Finance", "module": "finance.loan_calculations", "name": "محاسبات وام", "page": "37-38"},

            # عملیات ریاضی
            {"category": "Math Operations", "module": "math_ops.digit_operations", "name": "عملیات روی ارقام", "page": "9-10"},
            {"category": "Math Operations", "module": "math_ops.bit_operations", "name": "عملیات بیتی", "page": "29-31"},
            {"category": "Math Operations", "module": "math_ops.complex_numbers", "name": "اعداد مختلط", "page": "7"},
            {"category": "Math Operations", "module": "math_ops.series", "name": "سری‌های ریاضی", "page": "11"},
            {"category": "Math Operations", "module": "math_ops.expressions", "name": "عبارات ریاضی", "page": "10,19,24"},
            {"category": "Math Operations", "module": "math_ops.advanced_series", "name": "سری‌های پیشرفته", "page": "36-37"},

            # ابزارها
            {"category": "Utilities", "module": "utilities.datetime_ops", "name": "عملیات تاریخ و زمان", "page": "10,24,31-32"},
            {"category": "Utilities", "module": "utilities.string_ops", "name": "عملیات رشته‌ای", "page": "7,16,28"},
            {"category": "Utilities", "module": "utilities.conversions", "name": "تبدیل واحدها", "page": "8,12,14,22"},
            {"category": "Utilities", "module": "utilities.system_info", "name": "اطلاعات سیستم", "page": "15,21,23,28"},
            {"category": "Utilities", "module": "utilities.type_check", "name": "بررسی نوع داده", "page": "33"},
        ]

    def setup_gui(self):
        """تنظیم رابط گرافیکی"""
        # فریم اصلی
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # تنظیم وزن برای ریسایز
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # هدر
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        title_label = tk.Label(
            header_frame,
            text="🎯 پروژه مسائل پایتون",
            font=("Arial", 16, "bold"),
            fg="#2c3e50"
        )
        title_label.pack(pady=10)

        # فریم سمت چپ (لیست مسائل)
        left_frame = ttk.LabelFrame(main_frame, text="📂 مسائل موجود", padding="10")
        left_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))

        # فریم سمت راست (خروجی)
        right_frame = ttk.LabelFrame(main_frame, text="📊 خروجی برنامه", padding="10")
        right_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # تنظیم وزن برای فریم‌ها
        main_frame.rowconfigure(1, weight=1)
        main_frame.columnconfigure(1, weight=1)
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(1, weight=1)
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)

        # کنترل‌های سمت چپ
        self.setup_left_controls(left_frame)

        # کنترل‌های سمت راست
        self.setup_right_controls(right_frame)

        # نوار وضعیت
        self.setup_status_bar(main_frame)

    def setup_left_controls(self, parent):
        """کنترل‌های سمت چپ"""
        # فیلتر دسته‌بندی
        category_frame = ttk.Frame(parent)
        category_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(category_frame, text="فیلتر بر اساس دسته‌بندی:").grid(row=0, column=0, sticky=tk.W)

        self.category_var = tk.StringVar(value="همه")
        categories = ["همه"] + sorted(set(m["category"] for m in self.modules))
        category_combo = ttk.Combobox(
            category_frame,
            textvariable=self.category_var,
            values=categories,
            state="readonly",
            width=20
        )
        category_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        category_combo.bind('<<ComboboxSelected>>', self.filter_problems)

        category_frame.columnconfigure(1, weight=1)

        # جستجو
        search_frame = ttk.Frame(parent)
        search_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(search_frame, text="جستجو:").grid(row=0, column=0, sticky=tk.W)

        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            width=25
        )
        search_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        search_entry.bind('<KeyRelease>', self.filter_problems)

        search_frame.columnconfigure(1, weight=1)

        # لیست مسائل
        list_frame = ttk.Frame(parent)
        list_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))

        # Treeview برای نمایش مسائل
        columns = ('name', 'category', 'page')
        self.tree = ttk.Treeview(
            list_frame,
            columns=columns,
            show='headings',
            height=15,
            selectmode='browse'
        )

        # تعریف ستون‌ها
        self.tree.heading('name', text='نام مسئله')
        self.tree.heading('category', text='دسته‌بندی')
        self.tree.heading('page', text='صفحه')

        self.tree.column('name', width=250)
        self.tree.column('category', width=150)
        self.tree.column('page', width=80)

        # اسکرول بار
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)

        # دکمه‌های عملیاتی
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))

        self.run_button = ttk.Button(
            button_frame,
            text="▶️ اجرای انتخاب شده",
            command=self.run_selected
        )
        self.run_button.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)

        ttk.Button(
            button_frame,
            text="🧹 پاک کردن خروجی",
            command=self.clear_output
        ).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        ttk.Button(
            button_frame,
            text="❌ خروج",
            command=self.root.quit
        ).pack(side=tk.LEFT, padx=(5, 0), fill=tk.X, expand=True)

        # پر کردن Treeview
        self.populate_tree()

        # bind دابل کلیک
        self.tree.bind('<Double-1>', lambda e: self.run_selected())

    def setup_right_controls(self, parent):
        """کنترل‌های سمت راست"""
        # ناحیه خروجی
        self.output_text = scrolledtext.ScrolledText(
            parent,
            wrap=tk.WORD,
            width=60,
            height=20,
            font=("Consolas", 10),
            bg="#1e1e1e",
            fg="#ffffff",
            insertbackground="white"
        )
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # تگ‌های رنگی برای خروجی
        self.output_text.tag_configure("success", foreground="#00ff00")
        self.output_text.tag_configure("error", foreground="#ff0000")
        self.output_text.tag_configure("warning", foreground="#ffff00")
        self.output_text.tag_configure("info", foreground="#00ffff")

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        # نمایش راهنما
        self.show_welcome_message()

    def setup_status_bar(self, parent):
        """نوار وضعیت"""
        status_frame = ttk.Frame(parent)
        status_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))

        self.status_var = tk.StringVar(value="آماده")
        status_label = ttk.Label(
            status_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_label.pack(fill=tk.X)

        parent.columnconfigure(0, weight=1)

    def populate_tree(self, modules=None):
        """پر کردن Treeview با مسائل"""
        if modules is None:
            modules = self.modules

        # پاک کردن موارد موجود
        for item in self.tree.get_children():
            self.tree.delete(item)

        # اضافه کردن مسائل جدید
        for module in modules:
            self.tree.insert(
                '',
                tk.END,
                values=(
                    module['name'],
                    module['category'],
                    f"ص {module['page']}"
                ),
                tags=(module['module'],)
            )

    def filter_problems(self, event=None):
        """فیلتر کردن مسائل بر اساس دسته‌بندی و جستجو"""
        category = self.category_var.get()
        search_text = self.search_var.get().lower()

        filtered_modules = self.modules.copy()

        # فیلتر دسته‌بندی
        if category != "همه":
            filtered_modules = [m for m in filtered_modules if m['category'] == category]

        # فیلتر جستجو
        if search_text:
            filtered_modules = [
                m for m in filtered_modules
                if search_text in m['name'].lower() or search_text in m['category'].lower()
            ]

        self.populate_tree(filtered_modules)
        self.status_var.set(f"تعداد مسائل نمایش داده شده: {len(filtered_modules)}")

    def run_selected(self):
        """اجرای مسئله انتخاب شده"""
        if self.is_running:
            messagebox.showinfo("info", "لطفاً صبر کنید تا اجرای قبلی تمام شود")
            return

        selected_items = self.tree.selection()

        if not selected_items:
            messagebox.showwarning("هشدار", "لطفاً یک مسئله را انتخاب کنید")
            return

        # گرفتن ماژول از تگ آیتم انتخاب شده
        item = selected_items[0]
        module_path = self.tree.item(item, 'tags')[0]

        # پیدا کردن اطلاعات ماژول
        module_info = next((m for m in self.modules if m['module'] == module_path), None)

        if module_info:
            self.is_running = True
            self.run_button.config(state='disabled')
            self.status_var.set(f"در حال اجرای: {module_info['name']}")
            self.add_output(f"\n🎯 اجرای: {module_info['name']}\n", "info")
            self.add_output(f"📁 دسته‌بندی: {module_info['category']}\n", "info")
            self.add_output(f"📄 صفحه مرجع: {module_info['page']}\n", "info")
            self.add_output("="*50 + "\n", "info")

            # اجرا در یک thread جداگانه
            thread = threading.Thread(
                target=self.execute_module,
                args=(module_path,),
                daemon=True
            )
            thread.start()

    def execute_module(self, module_path):
        """اجرای ماژول در thread جداگانه"""
        try:
            # ایجاد redirector برای خروجی
            self.current_output_redirector = OutputRedirector(self.output_text)

            # redirect کردن stdout و stderr
            old_stdout = sys.stdout
            old_stderr = sys.stderr
            sys.stdout = self.current_output_redirector
            sys.stderr = self.current_output_redirector

            # ایمپورت و اجرای ماژول
            module = importlib.import_module(module_path)
            if hasattr(module, 'main'):
                module.main()
            else:
                print(f"⚠️ تابع main() در ماژول {module_path} یافت نشد")

            # بازگرداندن stdout و stderr
            sys.stdout = old_stdout
            sys.stderr = old_stderr

            self.add_output("\n✅ اجرا با موفقیت به پایان رسید\n", "success")

        except ImportError as e:
            error_msg = f"❌ خطا در ایمپورت ماژول {module_path}:\n{str(e)}\n"
            self.add_output(error_msg, "error")
        except Exception as e:
            error_msg = f"❌ خطا در اجرای ماژول {module_path}:\n{str(e)}\n"
            self.add_output(error_msg, "error")
        finally:
            # فعال کردن مجدد دکمه
            self.is_running = False
            self.root.after(0, lambda: self.run_button.config(state='normal'))
            self.root.after(0, lambda: self.status_var.set("آماده"))
            self.root.after(0, lambda: self.add_output("="*50 + "\n", "info"))

    def add_output(self, text, tag=None):
        """اضافه کردن متن به خروجی از thread اصلی"""
        def _add():
            if tag:
                self.output_text.insert(tk.END, text, tag)
            else:
                self.output_text.insert(tk.END, text)
            self.output_text.see(tk.END)
            self.output_text.update_idletasks()

        self.root.after(0, _add)

    def clear_output(self):
        """پاک کردن ناحیه خروجی"""
        self.output_text.delete(1.0, tk.END)
        self.show_welcome_message()

    def show_welcome_message(self):
        """نمایش پیام خوشامد"""
        welcome_msg = """🎯 به پروژه مسائل پایتون خوش آمدید!

📖 این برنامه شامل ۳۰ مسئله مختلف از کتاب "حل مسائل پایتون" می‌باشد.

🛠️ روش استفاده:
1. یک مسئله از لیست سمت چپ انتخاب کنید
2. روی "اجرای انتخاب شده" کلیک کنید یا دابل کلیک کنید
3. خروجی برنامه در اینجا نمایش داده می‌شود

🔍 امکانات:
• فیلتر بر اساس دسته‌بندی
• جستجوی مسائل
• نمایش صفحه مرجع هر مسئله
• محیط تعاملی برای تست کدها

💡 برای شروع، یک مسئله از لیست انتخاب کنید!
"""
        self.output_text.insert(tk.END, welcome_msg)

def main():
    """تابع اصلی اجرای GUI"""
    try:
        # ایجاد پنجره اصلی
        root = tk.Tk()

        # تنظیم استایل
        style = ttk.Style()
        style.theme_use('clam')

        # ایجاد برنامه
        app = PythonProblemsGUI(root)

        # اجرای حلقه اصلی
        root.mainloop()

    except Exception as e:
        print(f"❌ خطا در اجرای برنامه گرافیکی: {e}")

if __name__ == "__main__":
    main()