
def find_class():
    if user_class in school:
        return school.get(user_class)
    else: return 'Такого класса не существует!'


school = {
    '1а' : 21,
    '1б' : 25,
    '2в' : 30
}

print(school)

user_class = input('Введите класс для получения кол-ва учеников в ней: ')

print(find_class())