import numpy as np

def getCustomSize():
    print('Введите размерность таблицы: ')
    i = int(input())
    j = int(input())
    return i, j


task_1 = np.zeros(10)
print(f'---- Задание 1 ----\n{task_1}')

task_2 = np.full(40, 4.6)
print(f'---- Задание 2 ----\n{task_2}')

task_3 = np.arange(50, 1050)
print(f'---- Задание 3 ----\n{task_3}')

task_4 = task_3[::-1]
print(f'---- Задание 4 ----\n{task_4}')
np.line


#task_5 = np.arange(200, 399).reshape((20, 10))
task_5 = np.arange(200, 399)
print(f'---- Задание 5 ----\n{task_5.transpose()}')

task_6 = np.eye(30)
print(f'---- Задание 6 ----\n{task_6}')

task_7 = np.random.random((5, 5, 5))
print(f'---- Задание 7 ----\n{task_7}')

task_8 = np.ones((getCustomSize()))
task_8[1:-1,1:-1] = 0
print(f'---- Задание 8 ----\n{task_8}')

task_9 = np.zeros((getCustomSize()), dtype = int)
task_9[1::2,::2] = 1
task_9[::2,1::2] = 1
print(f'---- Задание 9 ----\n{task_9}')


