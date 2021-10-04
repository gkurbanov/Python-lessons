class Store:

    def __init__(self, name, price, qty, *args):
        self.name = name
        self.price = price
        self.qty = qty
        self.my_stores = []
        self.my_store = []

    # @classmethod
    # @staticmethod
    def add_stores(self):
        pass


class Printer(Store):
    def __init__(self, name, price, qty, model, paper_qty):
        Store.__init__(self, name, price, qty)
        self.model = model
        self.paper_qty = paper_qty


class Scaner(Store):
    def __init__(self, name, price, qty, year_created, working_hour_per_day):
        Store.__init__(self, name, price, qty)
        self.year_created = year_created
        self.working_hour_per_day = working_hour_per_day


class Copier(Store):
    def __init__(self, name, price, qty, is_wifi, is_bluetooth):
        Store.__init__(self, name, price, qty)
        self.is_wifi = is_wifi
        self.is_bluetooth = is_bluetooth


good_1 = Printer('принтер', 2500000, 3, 'JX-B', 1200)
good_2 = Scaner('сканер', 3500000, 1, 1992, 10)
good_3 = Copier('ксерокс', 1750000, 4, True, False)

good_1.add_stores()
