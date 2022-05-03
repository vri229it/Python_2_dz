# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В'
]

def tutors_generator(tutors, klasses):
    for i in range(len(tutors)):
        tutor = tutors[i]
        try:                                        #    можно использовать try - except или лучше сделать по другому проверку? if klasses[i] - вызывавет ошибку IndexError
            klass = klasses[i]
            tutor_klass = (tutor, klass)
        except IndexError:
            tutor_klass = (tutor, None)
        yield tutor_klass

tutors_gen = tutors_generator(tutors, klasses)

print(type(tutors_gen),*tutors_gen,sep="\n")
# print(next(tutors_gen),next(tutors_gen),next(tutors_gen), sep='\n')


# def tutors_generator(tutors, klasses):
#
#     for tutor, klass in zip(tutors, klasses):
#         tutor_klass = (tutor, klass)
#         yield tutor_klass