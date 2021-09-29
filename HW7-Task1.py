class Matrix:
    def __init__(self, maxtrix_1, matrix_2):
        self.maxtrix_1 = maxtrix_1
        self.matrix_2 = matrix_2

    def __add__(self):
        matr = [
            [0, 0, 0], [0, 0, 0], [0, 0, 0]
        ]

        for i in range(len(self.maxtrix_1)):
            for j in range(len(self.matrix_2[i])):
                matr[i][j] = self.maxtrix_1[i][j] + self.matrix_2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix(
    [[35, 432, 53], [42, 63, 65], [41, 53, 86]],
    [[42, 132, 342], [432, 11, 232], [452, 563, 132]]
)

print(my_matrix.__add__())