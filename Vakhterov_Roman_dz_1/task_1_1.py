'''
1. Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек
'''

duration=int(input('Введите время в секундах: '))
if duration < 60:
    print(duration,'сек')
elif 60 <= duration < 3600:
    m = duration // 60
    s = duration % 60
    print(m, 'мин', s, 'сек')
elif 3600 <= duration < 86400:
    h = duration // 3600
    m = duration % 3600 // 60
    s = duration % 3600 % 60
    print(h, 'час', m, 'мин', s, 'сек')
elif duration >= 86400:
    d = duration // 86400
    h = duration % 86400 // 3600
    m = duration % 86400 % 3600 // 60
    s = duration % 86400 % 3600 % 60
    print(d, 'дн',h, 'час', m, 'мин', s, 'сек')