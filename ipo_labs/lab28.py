import pandas as pd
import numpy as np
import random
print('---- Задание 1 ----\n')
column = int(input('Введите кол-во колонок: '))
dict_1 = {}
while True:
    column_name = input('Введите название новой колонки: ')
    if column_name == '0': break
    column_content = []
    for i in range(column):
        user_content = input(f'Введите содержимое {column_name}: ')
        column_content.append(user_content)
    dict_1[column_name] = column_content
print(dict_1)
frame_1 = pd.DataFrame(dict_1)
print(frame_1)


print('---- Задание 2 ----\n')
index_list = []
for i in range(column):
    index_list.append(input(f'Введите индекс {i}: '))
frame_2 = pd.DataFrame(dict_1, index = index_list)
print(frame_2)


print(f'''---- Задание 3 ----
Названия колонок: {frame_1.columns}
Набор данных: {frame_1.values}
Случайное значение: {frame_1[random.choice(list(dict_1))][random.randint(0, column)]}\n''')

print(f'''---- Задание 4-5 ----
{frame_1.loc[[int(input('Введите на какой строке начать: ')), int(input('Введите на какой строке закончить: '))]]}''')

print('---- Задание 6 ----\n')
column_name = input('Введите название новой колонки: ')
column_content = []
for i in range(column):
    user_content = input(f'Введите содержимое {column_name}: ')
    column_content.append(user_content)
frame_1[column_name] = column_content
print(frame_1)

print('---- Задание 7 ----\n')
user_search_content = input('Введите значение для проверки его присутствия: ')
if True in frame_1.isin([user_search_content]): print('Значение присутствует в DataFrame :)')
else: print('Значение отсутствует :(')


print('---- Задание 8----\n')
while True:
    user_column = input('Введите колонку, которую хотите удалить: ')
    if user_column in list(dict_1.keys()): break
    print('Такая колонка не найдена :(')
del frame_1[user_column]
print(frame_1)


print('---- Задание 9----\n')
print(frame_1.T)