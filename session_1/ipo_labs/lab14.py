class Vector():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def __str__(self):
        return f'Вы создали вектор {self.name}: {self.x}, {self.y}'
    def __add__(self, vector):
        x = self.x + vector.x
        y = self.y + vector.y
        return x, y
    def __sub__(self, vector):
        x = self.x - vector.x
        y = self.y - vector.y
        return x, y
    def __mul__(self, num):
        x = self.x * num
        y = self.y * num
        return Vector('вектор Mul: ', x, y)
    def __eq__(self, vector):
        return 'равны' if self.x == vector.x and self.y == vector.y else 'не равны'

def create_vector():
    name = input('Введите название вектора: ')
    a = int(input('Введите первую координату: '))
    b = int(input('Введите вторую координату: '))
    v = Vector(name, a, b)
    print('Вы создали', v)
    return v

vector_1 = create_vector()
vector_2 = create_vector()
vector_3 = vector_1 + vector_2
print('Сумма = ', vector_3)
vector_3 = vector_1 - vector_2
print('Разность = ', vector_3)
num = int(input('Введите число: '))
vector_4 = vector_1 * num
print('Вектора на число = ', vector_4)
print('Вектора', vector_1 == vector_2)