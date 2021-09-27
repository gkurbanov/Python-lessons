class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Рисуем с помощью {self.title}')


class Pen(Stationery):
    pass


class Pencil(Stationery):
    pass


class Handle(Stationery):
    pass


# Карандаш
pen = Pen('Карандаш')
pen.draw()

# Ручка
pencil = Pencil('Ручки')
pencil.draw()

# Маркер
handle = Handle('Маркер')
handle.draw()
