count_students = tuple()
for i in range(1, 16):
    count_students = count_students + tuple({i})
print(count_students)

lastName_students = tuple(['Авсюкевич', 'Шумель', 'Аниськов', 'Баранов', 'Войтович', 'Волков',
                        'Дубровский', 'Егелявичус', 'Задора', 'Исаков', 'Казимиренко', 'Ковзель',
                        'Корнеенко', 'Костенко', 'Самойлов'])

number_student = int(input('Введите номер студента: '))
print(lastName_students[number_student-1])

union = count_students + lastName_students
print(union)

user_slice = union[8:18]

print(user_slice)
