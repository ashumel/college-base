
matrix = [1, 2, 3], [4, 5, 6], [7, 8, 9]

for i in range(len(matrix)):
    s = 0
    for j in range(len(matrix[i])):
        s += matrix[i][j]
    matrix[i][-1::] = [s]

for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
