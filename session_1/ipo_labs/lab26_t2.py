import numpy as np


custom_n = int(input('Введите размерность матрицы N: '))
custom_m = int(input('Введите размерность матрицы M: '))

matrix_list = []
for i in range(custom_n):
    m_list = []
    for j in range(custom_m):
        m_list.append(int(input(f'Введите элемент {i}x{j}: ')))
    matrix_list.append(m_list)

matrix = np.array(matrix_list)
print(f'Исходная матрица:\n {matrix}')

result = 1
for i in range(custom_n):
    if i+1 != custom_n:
        result = result * matrix[i][(custom_m-1)-(i+1)]
    if i != 0:
        result = result * matrix[i][(custom_m-1)-(i-1)]
print(f'Ответ: {result}')