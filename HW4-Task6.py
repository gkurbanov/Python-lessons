from sys import argv
from itertools import cycle, count

script_name, number = argv

number = 2
last_number = number + 20
for el in count(number):
    if el == last_number:
        break
    else:
        print("Число", el)

# data = [1, 2, 5, 6, 'data', True, 9.6, 32, 52, '42', 3, 2, 43, 53, 'qew', '5']
# new_data = []
# for el in cycle(data):
#     new_data.append(el)
