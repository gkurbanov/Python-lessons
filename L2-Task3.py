# Список месяцев list
month_list = ["January", "Febuary",
              "March", "April", "May",
              "June", "July", "August",
              "September", "October", "November",
              "December"]

month_number = int(input('Введите номер месяца - '))

print(month_list[month_number - 1])
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
# Список месяцев dic
month_dic = {
    1: 'January',
    2: 'Febuary',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

month_number = int(input('Введите номер месяца - '))
for key in month_dic:
    if key == month_number:
        print(month_dic[month_number])
