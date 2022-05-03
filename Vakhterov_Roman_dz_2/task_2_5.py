"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

"""
sep = 50 * '-'

prices = [
    57.8,
    46.51,
    157.98,
    1005.32,
    503.52,
    123.45,
    8.95,
    760.32,
    2465.98,
    3245.5
]

prices_str = prices.copy()  # чтобы сохранить исходн.список с числовыми форматами

rub = []
kop = []
prices_rub_kop = []

for idx, price in enumerate(prices_str):
    prices_str[idx] = str(price)
    parts_rub_kop = prices_str[idx].split('.')
    rub = int(parts_rub_kop[0])
    kop = int(parts_rub_kop[1])
    # rub_kop='{} руб {} коп'.format(rub,kop)           # формат  <r> руб <k>
    price_formated = f'{rub:02d} руб {kop:02d} коп'  # формат  <rr> руб <kk>
    prices_rub_kop.append(price_formated)

print(', '.join(prices_rub_kop))

print(sep)

print(id(prices))
prices.sort()
print(prices)
print(id(prices))

print(sep)

prices_sort = sorted(prices, reverse=True)
print(prices_sort)

print(sep)

prices_top_5 =prices_sort[:4]
print(prices_top_5)

print(sorted(prices_top_5))
