import sys

num_line = 0
with open('users.csv','r',encoding='utf-8') as file_1:
    for line in file_1:
        user = line.rstrip()
        with open('hobby.csv', 'r', encoding='utf-8') as file_2:
            hobby = file_2.readline()

        txt='{} :{}'.format(user,hobby)
        with open('users_hobbies.cvs', 'a', encoding='utf-8') as file_res:
            file_res.write(txt)

