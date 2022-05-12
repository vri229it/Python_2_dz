class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income



class Position(Worker):

    def __init__(self,name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        return '{} {}'.format(self.name,self.surname)

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


incomes ={
    1: {'wage': 200000, 'bonus': 20000},
    2: {'wage': 150000, 'bonus': 10000},
    3: {'wage': 100000, 'bonus': 5000},
    4: {'wage': 80000, 'bonus': 3000},
}

p1 = Position ('Roman', 'Vakhterov', 'ingeneer', incomes[4])
print(p1.name)
print(p1.surname)
print(p1.position)
print(p1._income)

print(p1.get_full_name())
print(p1.get_total_income())