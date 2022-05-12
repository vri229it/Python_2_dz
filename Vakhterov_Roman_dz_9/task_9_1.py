from time import sleep, perf_counter, time


class TrafficLight:

    __color = ''

    def running(self):
        while True:
            self.__color = 'red'
            print(self.__color)
            sleep(7)

            self.__color = 'yellow'
            print(self.__color)
            sleep(2)

            self.__color = 'green'
            print(self.__color)
            sleep(5)



tl = TrafficLight()

tl.running()