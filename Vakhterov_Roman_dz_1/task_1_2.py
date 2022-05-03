'''
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
числа X):
a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
делится нацело на 7. Внимание: использовать только арифметические операции!
b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
списка, сумма цифр которых делится нацело на 7.
c. * Решить задачу под пунктом b, не создавая новый список.

'''

# Список кубов нечетных чисел
numbers = range(1000)
cub_numbers=[]
for num in numbers:
    if num%2:
        cub_numbers.append(num**3)
print(cub_numbers)

# Cумма чисел списка
total_sum = 0
for num in cub_numbers:
    sum_num = num//10**8 + num%10**8//10**7 + num%10**8%10**7//10**6 + num%10**8%10**7%10**6//10**5 + num%10**8%10**7%10**6%10**5//10**4 + num%10**8%10**7%10**6%10**5%10**4//1000 + num%10**8%10**7%10**6%10**5%10**4%1000//100 + num%10**8%10**7%10**6%10**5%10**4%1000%100//10 + num%10**8%10**7%10**6%10**5%10**4%1000%100%10

    #num//100 + num%100//10 + num%100%10
    #print(sum_num)
    if not sum_num % 7:
        total_sum += num
print('Сумма',total_sum)

# Сумма чисел списка (+17)
cub_numbers_plus=[]
for num in cub_numbers:
    cub_numbers_plus.append(num+17)

total_sum_plus=0
for num in cub_numbers_plus:
    sum_num = num//10**8 + num%10**8//10**7 + num%10**8%10**7//10**6 + num%10**8%10**7%10**6//10**5 + num%10**8%10**7%10**6%10**5//10**4 + num%10**8%10**7%10**6%10**5%10**4//1000 + num%10**8%10**7%10**6%10**5%10**4%1000//100 + num%10**8%10**7%10**6%10**5%10**4%1000%100//10 + num%10**8%10**7%10**6%10**5%10**4%1000%100%10

    #num//100 + num%100//10 + num%100%10
    #print(sum_num)
    if not sum_num % 7:
        total_sum_plus += num
print('Сумма плюс',total_sum_plus)


# # Вычисление суммы без создания нового списка
# for idx in range(len(cub_numbers)):
#     cub_numbers[idx]+=17
#
# for num in cub_numbers:
#     sum_num = num//10**8 + num%10**8//10**7 + num%10**8%10**7//10**6 + num%10**8%10**7%10**6//10**5 + num%10**8%10**7%10**6%10**5//10**4 + num%10**8%10**7%10**6%10**5%10**4//1000 + num%10**8%10**7%10**6%10**5%10**4%1000//100 + num%10**8%10**7%10**6%10**5%10**4%1000%100//10 + num%10**8%10**7%10**6%10**5%10**4%1000%100%10
#
#     #num//100 + num%100//10 + num%100%10
#     #print(sum_num)
#     if not sum_num % 7:
#         total_sum += num
# print(total_sum)