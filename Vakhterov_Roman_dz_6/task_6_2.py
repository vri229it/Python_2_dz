FILENAME = 'nginx_logs.txt'

with open(FILENAME, 'r', encoding='UTF-8') as f:
    count = 0
    addr_count = {}
    spamer = False
    tmp = 0

    for line in f:                              # выигрыш по памяти - если чтение из файла по строкам, а не всего файла
        addr = line[:line.index(' ')]
        if addr not in addr_count:
            addr_count[addr] = 1
            spamer_count= 1
        else:
            addr_count[addr] += 1
            if addr_count[addr] > spamer_count:
                spamer = addr
                spamer_count = addr_count[addr]

            else:
                continue

print(addr_count)

print(spamer, spamer_count)
