myList = [-1, -2], [-3, 4], [5, 6], [7, 8], [9, 10]
count = 0

for i in range(len(myList)):
    for j in range(len(myList[i])):
        print()
        if myList[i][j] < 0:
            count = count + 1

for row in myList:
    for elem in row:
        print(elem, end=' ')
    print()

print(f'''Количество отрицательных элементов: {count}''')