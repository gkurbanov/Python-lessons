# Введите число
a = int(input('Введите число - '))
max_value = a % 10
a = a // 10

while a > 0:
    if a % 10 > max_value:
        max_value = a % 10
    a = a // 10

print(max_value)
