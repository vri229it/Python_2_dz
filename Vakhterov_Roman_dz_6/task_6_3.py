import sys

users_hobbies = {}

with open('users.csv', 'r', encoding='utf-8') as file_1:
    content = file_1.read()
    users = content.splitlines()

with open('hobby.csv', 'r', encoding='utf-8') as file_2:
    content = file_2.read()
    hobbies = content.splitlines()

if len(hobbies) <= len(users):

    for i in range(len(users)):
        try:
            user = users[i]
            users_hobbies[user] = hobbies[i]
        except IndexError:
            users_hobbies[user] = None                  # есть другой способ ?
else:
    sys.exit(1)

# for user, hobby in zip(users, hobbies):
#     users_hobbies[user] = hobby

print(users_hobbies)

with open('users_hobbies.cvs', 'w', encoding='utf-8') as file_res:
    for k,v in users_hobbies.items():
        file_res.write('{}: {}\n'.format(k,v))