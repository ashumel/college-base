import math

def square(side_square = int):
    result = []
    perimeter_square = 0
    for i in range(4):
        perimeter_square = perimeter_square + side_square
    square_area = side_square * side_square
    square_diagonal = perimeter_square / (2*math.sqrt(2))
    result.append(perimeter_square)
    result.append(square_area)
    result.append(square_diagonal)
    return tuple(result)


number = input('Введите сторону квадрата: ')
print(square)