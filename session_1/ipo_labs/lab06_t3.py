matrix = [3, 2, 3], [1, 10, 1],  [7, 8, 9]

count = []
for i in range(len(matrix)):
    s = 0
    for j in range(len(matrix[i])):
        s += matrix[i][j]
    count.append(s)

for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()

print(f'''Индекс строки с минимальной суммой элементов: matrix[i] = {count.index(min(count))}''')