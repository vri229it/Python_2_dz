"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
"""


def thesaurus(*args):
    names_dict = {}

    for name in args:
        name_list = []
        key = name[0]
        if key in names_dict:
            name_list = names_dict[key]
        name_list.append(name)
        names_dict[key] = name_list

    return names_dict


names = [
    "Иван",
    "Илья",
    "Мария",
    "Петр",
    "Роман",
    "Адам",
    "Александр",
    "Владимир",
    "Нина"
]

names_thesaurus = thesaurus(*names)

print(names_thesaurus)
print(sorted(names_thesaurus.items()))