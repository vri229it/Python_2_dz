class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self, title = 'ручка'):
        print('Рисование ручкой')


class Pencil(Stationery):
    def draw(self, title = 'карандаш'):
        print('Чертеж карандашом')

class Handle(Stationery):
    def draw(self, title = 'маркер'):
        print('Выделение маркером')

pen_1 = Pen('ручка')
print(pen_1.draw())
print(pen_1.title)

pencil_1 = Pencil('карандаш')
print(pencil_1.draw())

handle_1 = Handle('маркер')
print(handle_1.draw())

handle_2 = Handle('маркер')
print(handle_2.title)
