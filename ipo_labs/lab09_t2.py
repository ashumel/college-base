def bank(a, years = int):
    for i in range(0, years):
        a = a + a / 100 * 10
    return a

money = int(input('Введите размер вклада: '))
years = int(input('Введите срок: '))

print(bank(money, years))