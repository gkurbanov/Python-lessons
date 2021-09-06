# Выручка

gain = int(input('Введите выручку - '))

# Потеря
loss = int(input('Убыток - '))

if loss > gain:
    print('Ваше предприятие убыточное')
else:
    print('Ваше предпрятие преуспевает')
    personal_qty = int(input('Введите количество сотрудников - '))
    salary_per_person = (gain - loss) / personal_qty
    print(f"Зарплата для каждого сотрудника составляет {'%.2f' % salary_per_person}")
