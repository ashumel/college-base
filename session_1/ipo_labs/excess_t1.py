clientsEstimations = []
goodEstimations = 0
notGoodEstimations = 0


for i in range(5):
    print('Как вы оцениваете кофейню от 1 до 10: ')
    try:
        mark = int(input())
    except:
        mark = 11
    if mark > 1 and mark <= 10:
        clientsEstimations.append(mark)
print(clientsEstimations)


for i in clientsEstimations:
    if i > 5:
        goodEstimations = goodEstimations + 1
    elif i <= 5:
        notGoodEstimations = notGoodEstimations + 1


print(f'''Всего положительных оценок: {goodEstimations}''')
print(f'''Всего отрицательных оценок: {notGoodEstimations}''')