def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num



odd_to_15 = odd_nums(15)

for i in odd_to_15:
    print(i)

# print(*odd_to_15,sep=' ')
