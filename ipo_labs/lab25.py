import numpy as np

file = open('matrix.txt', 'w')

task = np.random.randint(100, size=(5))

print(f'''Изначальный массив: {task}\nЗадание 1: {task[::-1]}''')

print(f'Задание 1: {np.zeros(10)}, {np.zeros(15)}')

task_2 = np.identity(5, dtype=int)
task_2[task_2 == 0] = 2

print(f'''Задание 2: \n{task_2}''')


task_3 = np.identity(5, dtype=int)
for i in range(0, 5):
    task_3[i:,] = i+1

print(f'''Задание 3: \n{task_3}''')

file.write(f'{task_2}\n{task_3}')