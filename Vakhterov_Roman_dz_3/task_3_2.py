"""
2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
>>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"

"""


def num_translate(num_eng_input):
    num_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }

    num_eng = num_eng_input.lower()
    num_rus = num_dict.get(num_eng)

    if num_eng_input.istitle():
        num_rus=num_rus.title()

    return num_rus


num_eng = input('Enter text number: ')

print(
    num_translate(num_eng)
)
