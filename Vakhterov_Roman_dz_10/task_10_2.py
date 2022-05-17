from abc import ABC, abstractmethod


class ClothesAbstract(ABC):
    @abstractmethod
    def add_coat(self,name,v, h):
        pass

    @abstractmethod
    def add_costume(self,name,v, h):
        pass

class Clothes(ClothesAbstract):

    def __init__(self):
        self.l = 0
        self.clothes = []

    def add_coat(self, name, v, h):
        self.clothes.append(Coat(name, v, h))

    def add_costume(self, name, v, h):
        self.clothes.append(Costume(name, v, h))

    @property
    def sum_l(self):
        sum_l = self.l
        for el in self.clothes:
            sum_l += el.l
        return sum_l


class Coat(Clothes):

    def __init__(self, name, v, h):
        self.name = name
        self.v = v
        self.h = h
        self.l = round(v / 6.5 + 0.5, 2)


class Costume(Clothes):

    def __init__(self, name, v, h):
        self.name = name
        self.v = v
        self.h = h
        self.l = round(2 * h + 0.3,2)


cl = Clothes()
print(cl.l, cl.clothes, '\n')

cl.add_coat('пальто Cardin', 45, 1.76)
cl.add_coat('пальто XX', 35, 1.62)
cl.add_costume('костюм Cardin', 48, 1.8)
cl.add_coat('пальто Fashion', 38, 1.75)
cl.add_costume('костюм FL', 50, 1.9)
cl.add_costume('костюм Brand', 42, 1.72)


for el in cl.clothes:
    print(el.name,el.l)

print(cl.sum_l)