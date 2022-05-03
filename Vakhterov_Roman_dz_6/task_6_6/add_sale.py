import sys

# cd task_6_6
# python add_sale.py 1532,72

sale = sys.argv[1] + '\n'

with open('bakery.csv','a',encoding='utf-8') as f:
    f.write(sale)