data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# почему то не получается сделать(
new_data = [i for i in data if data[i + 1:i + 2:] > data[i:i + 1:]]
print(new_data)

# 1 рабочий вариант
# i = 0
# for el in data:
#     if data[i + 1:i + 2:] > data[i:i + 1:]:
#         print(data[i + 1:i + 2:], '>', data[i:i + 1:], data[i + 1])
#     i += 1

# 2 рабочий вариант
# i = 1
# for el in data:
#     if data[i] > data[i - 1]:
#         print(data[i])
#     i += 1
