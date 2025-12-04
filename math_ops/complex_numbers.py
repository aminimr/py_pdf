"""
اعداد مختلط
Reference: صفحه 7 - مسئله 7
"""
import numpy as np
import cmath


class ComplexNumberOperations:

    @staticmethod
    def create_complex(real, imag):
        return complex(real, imag)

    @staticmethod
    def complex_operations(z1, z2):
        return {
            'Addition': z1 + z2,
            'Subtraction': z1 - z2,
            'Multiplication': z1 * z2,
            'Division': z1 / z2 if z2 != 0 else 'Undefined',
            'Conjugate z1': z1.conjugate(),
            'Conjugate z2': z2.conjugate(),
            'Magnitude z1': abs(z1),
            'Magnitude z2': abs(z2),
            'Phase z1': cmath.phase(z1),
            'Phase z2': cmath.phase(z2)
        }


def main():
    print("\n--- Complex Number Operations ---")
    try:
        real1 = float(input("قسمت حقیقی عدد اول: "))
        imag1 = float(input("قسمت موهومی عدد اول: "))
        real2 = float(input("قسمت حقیقی عدد دوم: "))
        imag2 = float(input("قسمت موهومی عدد دوم: "))

        ops = ComplexNumberOperations()
        z1 = ops.create_complex(real1, imag1)
        z2 = ops.create_complex(real2, imag2)

        print(f"\nعدد اول: {z1}")
        print(f"عدد دوم: {z2}")

        results = ops.complex_operations(z1, z2)

        print("\nنتایج عملیات:")
        for operation, result in results.items():
            print(f"{operation}: {result}")

        points = np.array([[z1.real, z1.imag], [z2.real, z2.imag],
                           [(z1 + z2).real, (z1 + z2).imag]])

        print(f"\nمختصات در صفحه:")
        for i, point in enumerate(points, 1):
            print(f"Point {i}: ({point[0]}, {point[1]})")

    except ValueError:
        print("خطا: لطفاً مقادیر عددی وارد کنید")


if __name__ == "__main__":
    main()