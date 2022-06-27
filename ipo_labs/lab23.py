import numpy as np

#1
print("Задание 1")
a = np.array([1,2,3,4,5,6,7,8,9,10],float)
print(f"Массив из 10 чисел: {a}")
#2
print("Задание 2")
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
print(f"Срез 1: {a[:b]}, Срез 2: {a[:c]}")
#3
print("Задание 3")
g = np.array([[1,2,3],[3,2,1],[2,3,1]], float)
print(g)
#4
print("Задание 4")
k = int(input("Введите число 1: "))
l = int(input("Введите число 2: "))

if k in g:
    print("\nЧисло 1 в двумерном массиве")
else:
    print("\nНет число 1 не в массиве")

if l in g:
    print("Число 2 в двумерном массиве")
else:
    print("Нет число 2 не в массиве")
#5
print("Задание 5")
m = np.array(range(30),float)
print('\n',m)
n = m.reshape(3,10)
print(n.transpose())
#6
print("Задание 6")
z = g.flatten()
v = n.flatten()
print("\n4-ый массив: ",np.concatenate((a,z,v)))
#7
print("Задание 7")
j = np.arange(1,101,4)
print("\n",j)
#8
print("Задание 8")
print("\n",np.ones((10,10), dtype = float))
#9
print("Задание 9")
h = np.arange(0,200,2)
print("\n",h)
print(h.reshape(25,4))
#10
print("Задание 10")
a = np.zeros((15,15))
print(np.eye(15,k = 7))