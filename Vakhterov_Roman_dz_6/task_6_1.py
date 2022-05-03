FILENAME = 'nginx_logs.txt'

list_parce = []

with open(FILENAME, 'r', encoding='UTF-8') as f:
    for line in f:
        line_list = line.split(' ')
        remote_addr = line_list[0]
        request_type = line_list[5][1:]
        requested_resource = line_list[6]
        line_parce = (remote_addr, request_type, requested_resource)
        list_parce.append(line_parce)

print(list_parce)
