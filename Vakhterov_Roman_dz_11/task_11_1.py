from datetime import datetime
import traceback


class MyDate:

    def __init__(self, dt):
        self.dt = datetime.strptime(dt, '%d-%m-%Y')

    @classmethod
    def get_num(cls, dt):
        dt = datetime.strptime(dt, '%d-%m-%Y')
        day = int(dt.strftime('%d'))
        month = int(dt.strftime('%m'))
        year = int(dt.strftime('%Y'))
        return day, month, year

    @staticmethod
    def valid_date(dt):
        try:
            dt = datetime.strptime(dt, '%d-%m-%Y')

        except ValueError:
            print('Ошибка значения даты. Введите корректно день, месяц, год')

        except Exception as e:
            print('Ошибка:\n', traceback.format_exc())

        else:
            print('Дата введена верно')

d_1 = MyDate('22-10-1990')
print(MyDate.get_num('22-10-1990'))

d_2 = MyDate('01-01-2022')

print(MyDate.valid_date('32-01-2022'))
print(MyDate.valid_date('01-01-2022'))
