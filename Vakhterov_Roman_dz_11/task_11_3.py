class DigError(Exception):
    def __init__(self, txt):
        self.txt = txt



is_stop=False
my_list =[]
while not is_stop:
    el = input('введите элемент списка (для остановки введите stop): ')
    if el != 'stop':
        try:
            if not el.isdigit():
                raise DigError('Неверно. Необходимо ввести число')
        except DigError as err:
            print(err)
        else:
            my_list.append(el)
    else:
        is_stop = True
print(my_list)
