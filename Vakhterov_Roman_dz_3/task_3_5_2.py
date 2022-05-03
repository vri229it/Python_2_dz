"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ.
"""

from random import choices, sample


def get_jokes(n, rep):
    """
    Get random jokes from dictionaries: nouns, adverbs, adjectives
    :param n: count of jokes
    :param rep: True - repeat jokes is allowed
    :return: list of random jokes
    """

    nouns = [
        "автомобиль",
        "лес",
        "огонь",
        "город",
        "дом"
    ]

    adverbs = [
        "сегодня",
        "вчера",
        "завтра",
        "позавчера",
        "ночью"
    ]

    adjectives = [
        "веселый",
        "яркий",
        "зеленый",
        "утопичный",
        "мягкий"
    ]

    if rep:
        nouns_rnd = sample(nouns, n)
        adverbs_rnd = sample(adverbs, n)
        adjectives_rnd = sample(adjectives, n)
    else:
        nouns_rnd = choices(nouns, k=n)
        adverbs_rnd = choices(adverbs, k=n)
        adjectives_rnd = choices(adjectives, k=n)
    jokes_list = []

    for noun, adverb, adjective in zip(nouns_rnd, adverbs_rnd, adjectives_rnd):
        joke=f'{noun} {adverb} {adjective}'
        jokes_list.append(joke)
    return jokes_list


print(get_jokes(n=5, rep=False))
