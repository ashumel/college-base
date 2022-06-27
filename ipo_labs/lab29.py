import pandas as pd

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


def delFromDataFrame(frame : pd.DataFrame):
    while True:
        user_delete = input('Введите строку для удаления: ')
        try:
            frame = frame.drop(user_delete)
            print(f'Обновленный DataFrame: \n{frame}')
            break
        except KeyError:
            print('⚠️ Такой строки не существует!')
    while True:
        user_delete = input('Введите колонку для удаления: ')
        try:
            del frame[user_delete]
            print(f'Обновленный DataFrame: \n{frame}')
            break
        except KeyError:
            print('⚠️ Такой колонки не существует!')

"""
frame = create_DataFrame()
print(f'Задание 1:\n {frame}')
delFromDataFrame(frame)
"""


student_1 = 'Аниськов'
student_2 = 'Костенко'
student_3 = 'Самойлов'
lesson_1 = 'ОАИП'
lesson_2 = 'ИПО'
lesson_3 = 'ОЯЗкБД'

series = pd.Series([8, 6, 8, 9, 7, 9, 7, 9],
                   index=[[student_1, student_1, student_1, student_2, student_2, student_2, student_3, student_3],
                        [lesson_1, lesson_2, lesson_3, lesson_2, lesson_3, lesson_1, lesson_2, lesson_3]])

frame = pd.DataFrame([['≈2,3 МэВ/с^2', '2/3', '1/2'], ['≈4,8 МэВ/с^2', '-1/3', '1/2'], ['≈1,275 ГэВ/с^2', '2/3', '1/2'], ['≈95 МэВ/с^2', '-1/3', '1/2'], ['≈173,07 ГэВ/с^2', '2/3', '1/2'], ['≈2,3 МэВ/с^2', '-1/3', '1/2'],
                      ['0,511 МэВ/с^2', '-1', '1/2'], ['<2,2 эВ/с^2', '0', '1/2'], ['105,7 МэВ/с^2', '-1', '1/2'], ['<0,17 МэВ/с^2', '0', '1/2'], ['1,777 ГэВ/с^2', '-1', '1/2'], ['<15,5 МэВ/с^2', '0', '1/2'],
                      [0, 0, 1], [0, 0, 1], ['91,2 ГэВ/с^2', 0, 1], ['80,4 ГэВ/с^2', '±1', 1], ['≈126 ГэВ/с^2', 0, 0]],
			  index=[['кварки','кварки','кварки','кварки', 'кварки', 'кварки',
             'лептоны', 'лептоны', 'лептоны', 'лептоны', 'лептоны', 'лептоны',
             'бозоны', 'бозоны', 'бозоны', 'бозоны', 'бозоны'],
            ['верхний','нижний','очарованный', 'странный', 'истинный', 'прелесный',
             'электрон', 'электронное нейтрино', 'мюон', 'мюонное нейтрино', 'тау', 'тау нейтрино',
             'глюон', 'фотон', 'Z бозон', 'W бозон', 'бозон Хиггса']],
			  columns=['масса', 'заряд', 'спин'])
print(f'Задание 2:\n{series}\n{frame}')


print(f'''Series в Dataframe:\n{series.unstack()}
Dataframe в Series:\n{frame.stack()}''')
frame.columns.names = ['свойства: ']
frame.index.names = ['тип частицы','наименование']
print(frame)
print(f'''Поменять порядок уровней на оси:\n{frame.swaplevel('тип частицы','наименование')}''')
print(f'''Отсортировать данные для конкретного уровня:\n{frame.sort_index(level='наименование')}''')