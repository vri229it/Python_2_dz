class Complex:
    def __init__(self, r, im):
        self.r = r
        self.im = im

    def __add__(self, other):
        return Complex(self.r + other.r, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.im * other.im , self.im * other.r + self.r * other.im)

    def __str__(self):
        return f'{self.r} + j{self.im}'

c_1 = Complex (5, 2)
c_2 = Complex (3, 7)
print(c_1 + c_2)
print(c_1 * c_2)