import requests
import xmltodict
import datetime
from decimal import Decimal
import pprint


def currency_rates(charcode):
    charcode=charcode.upper()
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)

    text = response.text
    dict = xmltodict.parse(text)
    # pprint.pprint(dict)
    charcodes = []
    for valute in dict['ValCurs']['Valute']:
        charcodes.append(valute['CharCode'])

    if charcode in charcodes:
        for valute in dict['ValCurs']['Valute']:
            if valute['CharCode'] == charcode:
                cur_value = Decimal(valute['Value'].replace(',','.'))
        cur_date = datetime.datetime.strptime(dict['ValCurs']['@Date'],'%d.%m.%Y').date()
        return cur_value, cur_date
    else:
        return None

    # pprint.pprint(text)

    # print(value)

charcode = input('Enter charcode valute: ')

print(currency_rates(charcode))
# print(type(currency_rates(charcode)))