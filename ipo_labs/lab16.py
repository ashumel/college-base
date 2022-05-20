def even_or_odd(function):
    def wrapper():
        a = 'четное' if (function()[0] % 2 == 0) else 'нечетное'
        b = 'четное' if (function()[1] % 2 == 0) else 'нечетное'
        return f'A - {a}\nB - {b}'
    return wrapper



def number(function):
    def wrapper():
        return [i*i for i in function()]
    return wrapper


def num_to_integer(function):
    def wrapper():
        return [int(x) for x in function()]
    return wrapper


@even_or_odd
@number
@num_to_integer
def get_number():
    a = input('Введите число A: ')
    b = input('Введите число B: ')
    return [a, b]


print(get_number())