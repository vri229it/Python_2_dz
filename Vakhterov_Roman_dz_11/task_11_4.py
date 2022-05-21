class DigTypeError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Store:
    def __init__(self):
        self.equipments = {}
        self.count = 0

    def add_equipment(self, equip, count):
        try:
            if type(count) != int:
                raise DigTypeError('Неверный параметр Кол-во. Необходимо ввести число.')
        except DigTypeError as err:
            print(err)
        else:
            if equip in self.equipments.keys():
                self.equipments[equip] += count
            else:
                self.equipments[equip] = count

    @property
    def sum_price(self):
        sum_price = 0
        for eq, count in self.equipments.items():
            sum_price += eq.price *count

        return sum_price


class Equipment(Store):
    def __init__(self, name, price, max_format):
        self.name = name
        self.price = price
        self.max_format = max_format


class Printer(Equipment):
    def __init__(self, name, price, max_format, qual_paper):
        super().__init__(name, price, max_format)
        self.qual_paper = qual_paper


class Scaner(Equipment):
    def __init__(self, name, price, max_format, screen):
        super().__init__(name, price, max_format)
        self.screen = screen


class Xerox(Equipment):
    def __init__(self, name, price, max_format, print_speed):
        super().__init__(name, price, max_format)
        self.print_speed = print_speed


st = Store()
pr_1 = Printer('HP', 6000, 'A4', 'premium')
pr_2 = Printer('HP', 2000, 'A4', 'normal')
sc_1 = Scaner('Epson', 15000, 'A3', '600pcs')
xer_1 = Xerox('Xerox', 1500, 'A4', 150)

st.add_equipment(pr_1, 10)
st.add_equipment(pr_1, 20)
st.add_equipment(pr_2, 50)
st.add_equipment(sc_1, 100)
st.add_equipment(xer_1, 5)
# st.add_equipment(xer_1, 'j')
st.add_equipment(xer_1, 10)

print(st.equipments)

count_pr_1 = st.equipments[pr_1]
print(count_pr_1)

print(st.sum_price)
