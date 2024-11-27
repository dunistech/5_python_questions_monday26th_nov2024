import math

class Complex:
    def __init__(self, a=0, b=0):
        """Initialize the complex number as a + bi."""
        self.a = a  # Real part
        self.b = b  # Imaginary part

    def __add__(self, other):
        """Add two complex numbers."""
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        """Subtract two complex numbers."""
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        """Multiply two complex numbers."""
        real_part = self.a * other.a - self.b * other.b
        imaginary_part = self.b * other.a + self.a * other.b
        return Complex(real_part, imaginary_part)

    def __truediv__(self, other):
        """Divide two complex numbers."""
        denominator = other.a ** 2 + other.b ** 2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        real_part = (self.a * other.a + self.b * other.b) / denominator
        imaginary_part = (self.b * other.a - self.a * other.b) / denominator
        return Complex(real_part, imaginary_part)

    def __abs__(self):
        """Return the absolute value of the complex number."""
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def __str__(self):
        """Return the string representation of the complex number."""
        if self.b == 0:
            return f"{self.a}"
        return f"({self.a}+{self.b}i)"

    def getRealPart(self):
        """Return the real part of the complex number."""
        return self.a

    def getImaginaryPart(self):
        """Return the imaginary part of the complex number."""
        return self.b


def main():
    print("Enter the first complex number:")
    a1 = float(input("Real part: "))
    b1 = float(input("Imaginary part: "))
    c1 = Complex(a1, b1)

    print("Enter the second complex number:")
    a2 = float(input("Real part: "))
    b2 = float(input("Imaginary part: "))
    c2 = Complex(a2, b2)

    print(f"\nFirst complex number: {c1}")
    print(f"Second complex number: {c2}")

    print("\nResults:")
    print(f"Addition: {c1 + c2}")
    print(f"Subtraction: {c1 - c2}")
    print(f"Multiplication: {c1 * c2}")
    try:
        print(f"Division: {c1 / c2}")
    except ZeroDivisionError as e:
        print(f"Division: {e}")
    print(f"Absolute value of first number: {abs(c1):.2f}")
    print(f"Absolute value of second number: {abs(c2):.2f}")


if __name__ == "__main__":
    main()
