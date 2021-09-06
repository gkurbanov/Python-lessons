# First day km
a = 2
# Minimum result in km
b = 3
# Day number
day = 1

# Процент
percentage = 0.1

while a <= b:
    a += float(percentage * a)
    day = day + 1
    print(f"День {day} и результат {'%.2f' % a}")
