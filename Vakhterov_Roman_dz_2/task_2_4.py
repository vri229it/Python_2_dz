"""
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?

"""

profession_name = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита'
]

names = []

print('Способ №1')
for item in profession_name:
    profession_name_parts = item.split()
    name = profession_name_parts.pop()
    name = name.title()
    names.append(name)

for name in names:
    meeting = f'Привет, {name}!'
    print(meeting)

print()
print('Способ №2')
for item in profession_name:
    name = item.split().pop().title()
    meeting = f'Привет, {name}!'
    print(meeting)

