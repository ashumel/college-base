import pandas as pd
import numpy as np

def create_DataFrame():
    x = int(input('Введите X: '))
    y = int(input('Введите Y: '))
    elementsList = []
    indexList = []
    columnList = []
    for i in range(1, x+1):
        elementList = []
        for j in range(1, y+1):
            elementList.append(int(input(f'Элемент {i}x{j}: ')))
        elementsList.append(elementList)
    for i in range(1, x+1):
        indexList.append(input(f'Индекс {i}: '))
    for j in range(1, y+1):
        columnList.append(input(f'Колонка {j}: '))
    return pd.DataFrame(elementsList, index = indexList, columns = columnList)


frame = create_DataFrame()


while True:
    user_delete = input('Введите строку для удаления: ')
    try:
        frame = frame.drop(user_delete)
        print(f'Новый DataFrame\n{frame}')
        break
    except KeyError:
        print('⚠️ Такой строки не существует!')
while True:
    user_delete = input('Введите колонку для удаления: ')
    try:
        del frame[user_delete]
        print(f'Новый DataFrame\n{frame}')
        break
    except KeyError:
        print('⚠️ Такой колонки не существует!')