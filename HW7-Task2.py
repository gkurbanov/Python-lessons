class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def calc_coat_square(self):
        sq = self.width / 6.5 + 0.5
        return round(sq)

    @property
    def calc_jacket_square(self):
        sq = 2 * self.height + 0.3
        return round(sq)


class Coat(Clothes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Требуемая площадь для пальто {self.square}'


class Jacket(Clothes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = round(2 * self.height + 0.3)

    def __str__(self):
        return f'Требуемая площадь для костюма {self.square}'


coat = Coat(2, 2)
jacket = Jacket(3, 2)

print(coat)
print(jacket)

# Подсчет общей площади ткани
overall_sum = coat.calc_coat_square + jacket.calc_jacket_square
print(f'Общая площадь ткани: {overall_sum}')
