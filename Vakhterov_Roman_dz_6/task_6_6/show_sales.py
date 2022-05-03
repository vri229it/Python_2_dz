import sys


# cd task_6_6
# python show_sales.py 1 2

#
count_start = int(sys.argv[1])-1



with open('bakery.csv','r',encoding='utf-8') as f:

    try:
        count_end = int(sys.argv[2])
        sales = f.readlines()[count_start:count_end]
    except IndexError:
        sales = f.readlines()[count_start:]

for sale in sales:
    print(sale.strip())