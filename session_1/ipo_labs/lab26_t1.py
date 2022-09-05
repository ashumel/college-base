import numpy as np

# Задание 1
massiv_size = int(input('Введите размер массива: '))

massiv_1 = np.arange(massiv_size)
massiv_2 = np.arange(massiv_size, massiv_size * 2)

print(f'1 массив: {massiv_1}\n2 массив: {massiv_2}')
print(f'''Сумма этих массивов: {massiv_1 + massiv_2}
Вычитание этих массивов: {massiv_1 - massiv_2}
Разность массивов: {massiv_1 / massiv_2}
Произведение этих массивов {massiv_1 * massiv_2}''')

# Задание 2

massiv = np.random.randint(-20, 10, size=(50))
print(f'''\nЗадание 2: {massiv}
Операция сложения всех элементов в массиве: {massiv.sum()}
Максимальный элемент в массиве: {massiv.max()}
Минимальный элемент в массиве: {massiv.min()}
Уникальные элементы в массиве: {np.unique(massiv)}''')

# Задание 3

def getCustomSize():
    print('Введите размерность массива: ')
    i = int(input())
    j = int(input())
    return i, j

massiv = np.ones((getCustomSize()), dtype = int)
values, vector = np.linalg.eig(massiv)
print(f'''\nЗадание 3: {massiv}
Определитель матрицы: {np.linalg.det(massiv)}
Cобственный вектор: {vector}
Cобственное значение матрицы: {values}''')