import sys

name_file_user= sys.argv[1]
name_file_hobby= sys.argv[2]
name_file_res=sys.argv[3]

# users.csv
# hobby.csv
# user_hobby.cvs
# python task_6_5.py users.csv hobby.csv user_hobby.cvs

num_line = 0
with open(name_file_user,'r',encoding='utf-8') as file_1:
    for line in file_1:
        user = line.rstrip()
        with open(name_file_hobby, 'r', encoding='utf-8') as file_2:
            hobby = file_2.readline()

        txt='{} :{}'.format(user,hobby)
        with open(name_file_res, 'a', encoding='utf-8') as file_res:
            file_res.write(txt)

