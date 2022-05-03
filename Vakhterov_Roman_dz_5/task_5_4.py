src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


result = set()
tmp=[]
tmp.append(src[0])          #есть возможность сократить в одну строчку ?
count = 1

for el in src:
    if el > tmp[count - 1]:
        result.add(el)
    else:
        result.discard(el)
    tmp.append(el)
    count += 1

result_ord = [el for el in src if el in result]

print(result)
print(result_ord)           # result_ord = [12, 44, 4, 10, 78, 123]