import numpy as np

size = int(input('Введите размер массива: '))
last_array = np.random.randint(-20, 20, size)
print(last_array)
print(np.sort(last_array))