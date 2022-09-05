import pandas as pd
import numpy as np

action = True
numbers_list = []
print('---- Задание 1 ----\n')
while (action):
    number = int(input('Введите число, (для отмены введите 0): '))
    if number == 0: action = False
    else: numbers_list.append(number)
print(pd.Series(numbers_list))

print('---- Задание 2 ----\n')
action = True
numbers_list = []
index_list = []

while(action):
    number = int(input('Введите число: '))
    index = input('Введите индекс(для отмены введите 0): ')
    if index == '0': action = False
    else:
        numbers_list.append(number)
        index_list.append(index)
series = pd.Series(numbers_list, index = index_list)
print(series)

print('---- Задание 3 ----\n')
n = int(input())
print(series[:n])

print('---- Задание 4 ----\n')
user_custom_index = input('Введите метку: ')
print(series[user_custom_index])

print('---- Задание 5 ----\n')
print(series[series > 2])

print('---- Задание 6 ----\n')
print(series + series)
print(series / 2)

print('---- Задание 7 ----\n')
series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],
                   index = ['one', 'two', 'two', 'three', 'three', 'three',
                            'four', 'four', 'four', 'four', 'five', 'five',
                            'five', 'five', 'five'])
print(series.unique())

print('---- Задание 8 ----\n')
print(series.count())
print(series.value_counts())

print('---- Задание 9 ----\n')
user_number = []
for i in range(3):
    user_number.append(input('Введите число: '))
print(series.isin(user_number))
print(series[series.isin(user_number)])


print('---- Задание 10 ----\n')
while True:
    number = input('Введите число, (для отмены введите N): ')
    if number == 'N': break
    elif int(number) == 0: number = np.NaN
    numbers_list.append(int(number))
series = pd.Series(numbers_list)
print(series)

print('---- Задание 11 ----\n')
print(series.isnull())
print(series.notnull())


print('---- Задание 12 ----')
series_dict = {}
while True:
    user_value = int(input('Введите значение: '))
    key_value = int(input('Введите ключ: '))
    if key_value == 0: break
    series_dict[key_value] = user_value
series_1 = pd.Series(series_dict)
print(series_1)

print('---- Задание 13 ----')
series_dict = {}
while True:
    user_value = int(input('Введите значение: '))
    key_value = int(input('Введите ключ: '))
    if key_value == 0: break
    series_dict['copy_{key_value}'] = user_value
series_2 = pd.Series(series_dict)
print(series_2)

print('---- Задание 14 ----')
print(series_1 + series_2)
print(series_1 * series_2)