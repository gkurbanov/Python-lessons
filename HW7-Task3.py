class Cell:
    def __init__(self, qty):
        self.qty = qty

    def __add__(self, other):
        return f'Сумма 2 клеток = {self.qty + other.qty}'

    def __sub__(self, other):
        if self.qty < other.qty:
            return f'Вычитание невозможно так как первая клетка меньше второй'
        else:
            return f'Вычитание 2 клеток = {self.qty - other.qty}'

    def __mul__(self, other):
        return f'Умножение 2 клеток = {self.qty * other.qty}'

    def __truediv__(self, other):
        return f'Деление 2 клеток = {round(self.qty / other.qty)}'

    def make_order(self, row_qty):
        str = ''
        rows_qty = round(self.qty / row_qty)

        for i in range(rows_qty):
            str += f'{"*" * rows_qty} \\n'
        str += f'{"*" * (self.qty % row_qty)}'
        return str


cell_1 = Cell(22)
cell_2 = Cell(3)

# Математические сложения
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

# Построение
print(cell_1.make_order(3))
