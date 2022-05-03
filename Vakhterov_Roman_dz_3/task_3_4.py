"""
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

"""

def thesaurus_adv(*args):
    thesaurus = {}

    for name in args:
        names_dict = {}
        names_list=[]
        key_lastname = name[name.find(' ')+1]      #первая буква фамилии (1-я буква после пробела)
        key_firstname = name[0]
        if key_lastname in thesaurus:
            names_dict = thesaurus[key_lastname]
            if key_firstname in names_dict:
                names_list = names_dict[key_firstname]
        names_list.append(name)
        names_dict[key_firstname]=names_list
        thesaurus[key_lastname] = names_dict

    return thesaurus


names = [
    "Иван Сергеев",
    "Илья Серов",
    "Вячеслав Слободенюк",
    "Мария Петрова",
    "Петр Романов",
    "Роман Савельев",
    "Адам Новак",
    "Александр Бабушкин",
    "Владимир Авдеев",
    "Владислав Автюк",
    "Александр Антонов"
]




names_thesaurus = thesaurus_adv(*names)

print(names_thesaurus)
# print(sorted(names_thesaurus.items()))