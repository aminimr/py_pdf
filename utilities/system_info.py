"""
اطلاعات سیستم
Reference: صفحات 15, 21, 23, 28 - مسائل 27, 28, 47, 61
"""
import platform
import os
import sys
import socket
import multiprocessing
import struct
import pandas as pd


class SystemInfo:

    @staticmethod
    def get_system_info():
        return {
            'System': platform.system(),
            'Release': platform.release(),
            'Version': platform.version(),
            'Architecture': platform.architecture()[0],
            'Processor': platform.processor()
        }

    @staticmethod
    def get_python_info():
        return {
            'Version': platform.python_version(),
            'Implementation': platform.python_implementation(),
            'Compiler': platform.python_compiler(),
            'Build': platform.python_build()
        }

    @staticmethod
    def get_hardware_info():
        return {
            'CPU Count': multiprocessing.cpu_count(),
            'Machine': platform.machine(),
            'Platform': platform.platform(),
            'Hostname': socket.gethostname()
        }

    @staticmethod
    def get_environment_info():
        return {
            'Current Directory': os.getcwd(),
            'User': os.getenv('USERNAME') or os.getenv('USER'),
            'Home': os.getenv('HOME') or os.getenv('USERPROFILE')
        }


def main():
    print("\n--- System Information ---")
    sys_info = SystemInfo()

    system_data = sys_info.get_system_info()
    python_data = sys_info.get_python_info()
    hardware_data = sys_info.get_hardware_info()
    environment_data = sys_info.get_environment_info()

    print("\n=== اطلاعات سیستم عامل ===")
    for key, value in system_data.items():
        print(f"{key}: {value}")

    print("\n=== اطلاعات پایتون ===")
    for key, value in python_data.items():
        print(f"{key}: {value}")

    print("\n=== اطلاعات سخت‌افزار ===")
    for key, value in hardware_data.items():
        print(f"{key}: {value}")

    print("\n=== اطلاعات محیطی ===")
    for key, value in environment_data.items():
        print(f"{key}: {value}")

    print(f"\nاطلاعات اضافی:")
    print(f"اندازه اشاره‌گر: {struct.calcsize('P') * 8} بیت")
    print(f"ماژول‌های سایت: {len(sys.path)} مسیر")

    all_info = {**system_data, **python_data, **hardware_data, **environment_data}
    info_df = pd.DataFrame(list(all_info.items()), columns=['Property', 'Value'])

    print("\nگزارش جامع سیستم:")
    print(info_df.to_string(index=False))


if __name__ == "__main__":
    main()