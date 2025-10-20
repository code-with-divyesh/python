class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overload + operator
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # Overload - operator
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    # Overload * operator
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    # Overload / operator
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    # Overload str() for printing
    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Creating complex numbers
c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

# Addition
c3 = c1 + c2
print("Addition:", c3)

# Subtraction
c4 = c1 - c2
print("Subtraction:", c4)

# Multiplication
c5 = c1 * c2
print("Multiplication:", c5)

# Division
c6 = c1 / c2
print("Division:", c6)
