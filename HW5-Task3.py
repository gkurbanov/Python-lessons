f = open('data-task3.txt', mode="r", encoding="utf-8")

overall_sum = 0
workers_qty = 0

for line in f:
    single_worker = line.split()
    if int(single_worker[1]) < 20000:
        print(line, end='')
    workers_qty += 1
    overall_sum += int(single_worker[1])

f.close()
print("----------")
print(f"Сотрудников {workers_qty}")
print(f"Средняя зп {overall_sum / workers_qty}")


