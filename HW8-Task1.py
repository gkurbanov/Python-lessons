class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @staticmethod
    def valid(day, month, year):
        if day >= 1 and day <= 31:
            if month >= 1 and month <= 12:
                if year >= 0 and year <= 2025:
                    print('Данные введены правильно!')
                else:
                    print('Год указан неверно')
            else:
                print("Месяц введен неправильно")
        else:
            print("Дата введене неправильная")

    @classmethod
    def get_numbers(cls, day_month_year):
        dates = []
        for i in day_month_year.split('.'):
            dates.append(int(i))
        print(dates)


date = Data('1-12-2021')

date.get_numbers('22.03.2020')
date.valid(2, 11, 2020)
