new_values = []

ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': "Три", 'Four': 'Четрые'}

with open('data-task4.txt', mode="r+", encoding="utf-8") as f:
    for line in f:
        line = line.split()
        new_values.append(ru_dict[line[0]] + ' - ' + line[2])

# Создание нового файла
f = open('new-data-task4.txt', mode="w", encoding="utf-8")
for value in new_values:
    f.write(value + '\n')

print('Новый файл создан')
