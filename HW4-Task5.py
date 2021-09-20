from functools import reduce

data = [i for i in range(100, 1000 + 1) if i % 2 == 0]
result = reduce(lambda x, y: x * y, data)

print(result)
