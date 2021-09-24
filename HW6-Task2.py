class Road:
    def __init__(self, length, width, weight, thickness):
        self.length = length
        self.width = width
        self.weight = weight
        self.thickness = thickness

    def calculate(self, length, width, weight, thickness):
        print(f'Требуемая масса асфальта: {length * width * weight * thickness}')


road = Road(20, 5000, 25, 5)
road.calculate(road.length, road.width, road.weight, road.thickness)
