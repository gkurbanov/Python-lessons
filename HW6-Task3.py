class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        Worker.__init__(self, name, surname, position, wage, bonus)
        self.bonus = bonus
        self.wage = wage

    def get_full_name(self):
        print(f'Полное имя сотрудника {self.name} - {self.surname}')

    def get_total_income(self):
        print(f'Общий доход пользователя {self.wage + self.bonus}')


person = Position('Alex', 'Bubnov', 'Director', 3000, 200)
person.get_full_name()
person.get_total_income()
