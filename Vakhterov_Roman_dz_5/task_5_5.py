src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result=set()
tmp=set()
for el in src:
    if el not in tmp:
        result.add(el)
    else:
        result.discard(el)
    tmp.add(el)

result_ord = [el for el in src if el in result]

print(result_ord)

# result_ord = [23, 1, 3, 10, 4, 11]