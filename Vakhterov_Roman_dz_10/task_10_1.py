class Matrix:
    def __init__(self, matr):
        self.matr = matr


    def __str__(self):
        s_list = [str(self.matr[i]).replace(',','')[1:-1] for i in range(len(self.matr))]
        s = '\n'.join(s_list)

        return s

        # for i in range(len(self.matr):
        #     print(*self.matr[i])

    def __add__(self, other):

        matrix_sum = [
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.matr, other.matr)]

        return Matrix(matrix_sum)


matr_1 = [
    [31, 22, 45],
    [37, 43, 21],
    [51, 86, 56]
]

matr_2 = [
    [10, 25, 15],
    [137, 443, 17],
    [34, 98, 20]
]


m_1 = Matrix(matr_1)
m_2 = Matrix(matr_2)

print(m_1, '\n')
print(m_2, '\n')
print(m_1 + m_2)


