import codecs

class group():
    college = 'ВГКЭ'
    students_list = []
    students_count = 0
    avg_mark = 0
    def __init__(self, group, course):
        self.group = group
        self.course = course
    def __str__(self):
        return f'{group.college}\nЭто {self.group}\n{self.course}\nКоличество студентов: {self.students_count}\nСписок студентов: {self.students_list}\nСредняя оценка: {round(self.avg_mark, 2)}'
    def __setattr__(self, attribute, value):
        self.__dict__[attribute] = value
    def __getattr__(self, attribute):
        return f'⚠️ Такого поля нет: {attribute}'
    def __delattr__(self, attribute):
        print(f'⚠️ Это поле невозможно удалить! {attribute}')
    def students_set(self, file):
        file = codecs.open(rf'ipo_labs/lab15/{file}.txt', 'r', 'utf_8')
        for line in file:
            group.students_list.append(line.rstrip())
            group.students_count += 1

pz = group('ПЗ-56', '2-й курс')
print(pz)
pz.group = 'ПЗ-55'
pz.college = 'ВГУ им. Машерова'
print(pz)
print(pz.not_exist)
del pz.avg_mark
pz.students_set('students')
print(pz)
temp_mark = 0
for i in range(0, len(pz.students_list)):
    print('Введите оценку: ', pz.students_list[i])
    temp_mark += int(input())
pz.avg_mark = temp_mark / pz.students_count
print(pz)