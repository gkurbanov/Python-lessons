number1 = int(input('Введите 1 число - '))
number2 = int(input('Введите 2 число - '))


class DivisionError(Exception):
    def __init__(self, text):
        self.text = text

    def divide_numbers(num1, num2):
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print('На ноль делить нельзя')


DivisionError.divide_numbers(number1, number2)
