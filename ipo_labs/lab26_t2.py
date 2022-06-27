import numpy as np
import math

matrix = np.array([[1, 2, 3, 5], [4, 5, 7, 6], [1, 7, 8, 9], [2, 4, 5, 2]])
print(matrix)
result = np.fliplr(matrix).diagonal()
result_diag = list(result)
print(result)
result = list((np.array(matrix)).reshape(9,))
#result = list((np.array(matrix)).reshape(9,))
#for i in result_diag:
#    result.remove(i)
#result.remove(9)
#
#print(f'''Ответ: {math.prod(result)}''')