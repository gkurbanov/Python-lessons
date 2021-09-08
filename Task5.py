# Список значений
list_number = [7, 5, 4, 3, 2]

insert_number = int(input('Введите число - '))

i = 0
for el in list_number:
    if insert_number >= el:
        list_number.insert(i, insert_number)
        break
    elif insert_number < el and len(list_number) - 1 == i:
        list_number.insert(len(list_number), insert_number)
        break
    i += 1

print(list_number)
