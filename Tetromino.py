import random

colors = [
    (0, 0, 0),
    (0, 240, 240),
    (0, 0, 240),
    (240, 160, 0),
    (240, 240, 0),
    (0, 240, 0),
    (160, 0, 240),
    (240, 0, 0)
]


class Tetromino:
    x = 0
    y = 0

    tetrominos = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],  # Gerade
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # Rev L
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # L
        [[1, 2, 5, 6]],  # BLOCK
        [[6, 7, 9, 10], [1, 5, 6, 10]],  # S
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # T
        [[4, 5, 9, 10], [2, 6, 5, 9]],  # Z
    ]

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.type = random.randint(0, len(self.tetrominos) - 1)
        self.color = colors[self.type + 1]
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.tetrominos[self.type])

    def image(self) -> list:
        return self.tetrominos[self.type][self.rotation]
