class ExceptionError:
    def __init__(self, *args):
        self.list_numbers = []

    def enter_input(self):
        while True:
            try:
                val = int(input('Введите значение и нажимайте Enter - '))
                self.list_numbers.append(val)
                print(f'Текущий список - {self.list_numbers} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                stop = input(f'Для выхода их программы введите stop ')

                if stop == 'stop':
                    return False


try_add = ExceptionError(1)
print(try_add.enter_input())
