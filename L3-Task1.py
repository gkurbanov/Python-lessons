# Запросить 2 числа
num_1 = int(input('Введите первое число - '))
num_2 = int(input('Введите второе число - '))


def func(num_1, num_2):
    try:
        print(f'Деление числа {num_1} и {num_2} = {num_1 / num_2}')
    except ZeroDivisionError:
        print('Деление на ноль запрещено')


func(num_1, num_2)
