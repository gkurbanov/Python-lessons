# Создание файла
overall_sum = 0
with open('data-task5.txt', 'w+') as f:
    f.write("3 2 1 23 4 5 32 12 2 42 2 1 23 54")
    f.seek(0)
    data = f.read().split()
    for number in data:
        overall_sum += int(number)

print(overall_sum)
