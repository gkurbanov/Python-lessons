num_1 = int(input('Введите первое положительное число - '))
num_2 = int(input('Введите второе отрицательно число - '))


def my_func(x, y):
    # first solution
    # print(1 / x ** abs(y))

    # second solution
    i = 0
    result = 0
    while i != abs(y):
        result = x * x
        i += 1
    print(1 / result)


my_func(num_1, num_2)
