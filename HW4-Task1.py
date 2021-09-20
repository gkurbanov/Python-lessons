from sys import argv

script_name, work_hours, rate_per_hour, bonus = argv

salary = (int(work_hours) * int(rate_per_hour)) + int(bonus)

print("Имя скрипта: ", script_name)
print("Зарплата сотрудника составляет: ", salary)
