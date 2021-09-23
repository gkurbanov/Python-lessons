# Создание файла
f = open('data-task1.txt', 'w')

# Запросить данные у пользователя
data = input('Введите данные через пробел - ')
new_data = data.split()
for el in new_data:
    f.write(el + '\n')
f.close()