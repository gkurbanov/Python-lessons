sum = 0
b = True

while b == True:
    ask_numbers = input('Введите числа через пробел - ')
    numbers = ask_numbers.split()

    for el in numbers:
        try:
            el = float(el)
            if el > 0:
                sum += el
        except:
            print("Программа завершена")
            b = False
            break
    print(sum)

