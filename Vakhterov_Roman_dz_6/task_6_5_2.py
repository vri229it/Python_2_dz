import sys
name_file_user=input('Введите имя файла с пользователями: ')
name_file_hobby=input('Введите имя файла с хобби: ')
name_file_res=input('Введите имя файла результатов: ')

# users.csv
# hobby.csv
# user_hobby.cvs


num_line = 0
with open(name_file_user,'r',encoding='utf-8') as file_1:
    for line in file_1:
        user = line.rstrip()
        with open(name_file_hobby, 'r', encoding='utf-8') as file_2:
            hobby = file_2.readline()

        txt='{} :{}'.format(user,hobby)
        with open(name_file_res, 'a', encoding='utf-8') as file_res:
            file_res.write(txt)

