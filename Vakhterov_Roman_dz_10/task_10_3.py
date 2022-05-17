class Cell:

    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):

        if self.count - other.count > 0:
            return Cell(self.count - other.count)
        else:
            print('Разность количества ячеек двух клеток отрицательная')

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __floordiv__(self, other):
        return Cell(self.count // other.count)

    def __truediv__(self, other):
        return Cell(self.count / other.count)

    def __str__(self):
        return str(self.count)

    def make_order(self, col):
        self.col = col
        rows = self.count // self.col
        rest = self.count % self.col
        s_list = ['*' * self.col for i in range(rows)]
        s_list.append('*' * rest)
        s = '\n'.join(s_list)

        return s


c_1 = Cell(14)
c_2 = Cell(25)
print(c_1, c_2)
print('cумма', c_1 + c_2)
print('разность', c_1 - c_2)
print('разность', c_2 - c_1)
print('умножение', c_1 * c_2)
print('целочисленное деление', c_1 // c_2)
print('деление', c_1 / c_2)

# print(c_1.count)
print(c_1.make_order(3))
print('\n')
print(c_2.make_order(4))

# c_1 = Cell(10)
# c_2 = Cell(5)
# c_3 = Cell(15)
# c_4 = Cell(2)
# c_5 = Cell(2)

# print('арифметические операции', c_1+c_2-c_4, c_1*c_2-c_3, c_4+c_3*c_1, c_3//c_4, c_3+c_2/(c_4+c_5))
