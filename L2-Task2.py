# Запроситьу пользователя строку
words = [0, 1, 2, 3, 4, 5, 6, 7]

i = 0
x = 2

result_list = []

for el in words:
    new_list = words[i:x]
    if len(new_list):
        # print(new_list[::-1])
        result_list.extend(new_list[::-1])
        i += 2
        x += 2

print(result_list)
