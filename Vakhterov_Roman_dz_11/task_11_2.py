class DivZeroError(Exception):
    def __init(self, txt):
        self.txt = txt


num_1 = int(input('Введите делимое число: '))
num_2 = int(input('Введите число делитель: '))

try:

    if num_2 == 0:
        raise DivZeroError('Деление на ноль')

except DivZeroError as err:
    print(err)
else:
    div = num_1 / num_2
    print('Результат = ',div)
