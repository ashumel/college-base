x1 = []
x2 = []
x3 = []
for i in range(1, 20+1):
    x1.append(i)
for i in range(10, 30+1):
    x2.append(i)
for i in range(1, 21+1, 2):
    x3.append(i)

x1_set = set(x1)
x2_set = set(x2)
x3_set = set(x3)

y = set((x1_set | x2_set) & (x1_set | x3_set) - (x2_set | x3_set))
print (y)

y1 = set()

for element in y:
    if element % 4 == 0:
        y1.add(element)

print(y1)


print(y.issuperset(y1))