num_1 = int(input('Введите первое число - '))
num_2 = int(input('Введите второе число - '))
num_3 = int(input('Введите третье число - '))


def my_func(num_1, num_2, num_3):
    numbers = [num_1, num_2, num_3]
    # 1 наибольшее число
    largest = 0
    # 2 наибольшее число
    second_largest = 0
    for item in numbers:
        if item > largest:
            second_largest = largest
            largest = item
        elif largest > item > second_largest:
            second_largest = item
    sum = largest + second_largest
    print(f'Сумма двух наибольших чисел равна {sum}')


my_func(num_1, num_2, num_3)
