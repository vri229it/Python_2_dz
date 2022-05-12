class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print('Car go')

    def stop(self):
        print('Car stop')

    def turn(self, direction):
        self.direction = direction
        print(f'Car turn {direction}')

    def show_speed(self):
        print(f'Speed is {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed is {self.speed}')
        if self.speed > 60:
            print('Is speeding!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed is {self.speed}')
        if self.speed > 40:
            print('Is speeding!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)



car1 = Car(100, 'black', 'Chevrolet', True)
print(car1.color, car1.name, car1.speed, car1.is_police)
print(car1.go())
print(car1.show_speed())
print(car1.stop(),'\n')

car2 = TownCar(100, 'white', 'Ford')
print(car2.color, car2.name, car2.speed)
print(car2.go())
print(car2.show_speed())
print(car2.stop(),'\n')

car3 = SportCar(200, 'red', 'Porsche')
print(car3.color, car3.name, car3.speed)
print(car3.show_speed(),'\n')

car4 = WorkCar(80, 'green', 'Volksvagen')
print(car4.color, car4.name, car4.speed, car4.is_police)
print(car4.go())
print(car4.show_speed())
print(car4.turn('left'),'\n')



car5 = PoliceCar(150, 'black', 'Audi')
print(car5.color, car5.name, car5.speed, car5.is_police)
print(car5.go())
print(car5.turn('right'),'\n')
print(car5.show_speed(),'\n')
