'''
3.Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов

'''

percents=range(1,100)
for perc in percents:
    if perc%10 ==1:
        print(perc,'процент')
    elif 2 <= perc%10 <= 4:
        print(perc, 'процента')
    elif perc%10 >= 5 or perc%10 ==0:
        print(perc, 'процентов')
