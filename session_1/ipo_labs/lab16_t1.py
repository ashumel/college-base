def even_or_odd(function):
    def wrapper():
        list = function()
        a = 'четное' if (list[0] % 2 == 0) else 'нечетное'
        b = 'четное' if (list[1] % 2 == 0) else 'нечетное'
        print(f'A - {a}\nB - {b}')
    return wrapper


def number_squaring(function):
    def wrapper():
        task = [i*i for i in function()]
        print(task)
        return task
    return wrapper


def num_to_integer(function):
    def wrapper():
        task = [int(x) for x in function()]
        print(task)
        return task
    return wrapper


@even_or_odd
@number_squaring
@num_to_integer
def get_number():
    a = input('Введите число A: ')
    b = input('Введите число B: ')
    print([a, b])
    return [a, b]


get_number()