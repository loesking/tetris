from Tetromino import Tetromino


class Tetris:
    height = 0
    width = 0
    score = 0
    state = 'start'
    tetromino = None

    def __init__(self, _height: int, _width: int):
        self.height = _height
        self.width = _width
        self.field = []
        self.score = 0
        self.state = 'start'

        for i in range(_height):
            new_line = []
            for j in range(_width):
                new_line.append(0)
            self.field.append(new_line)

        self.new_tetromino()

    def new_tetromino(self):
        self.tetromino = Tetromino(3, 0)

    def tetromino_fall(self):
        self.tetromino.y += 1
        if self.collide():
            self.tetromino.y -= 1
            self.stop()

    def stop(self):
        for i in range(4):
            for j in range(4):
                possible_tetromino_area = i * 4 + j
                if possible_tetromino_area in self.tetromino.image():
                    self.field[i + self.tetromino.y][j + self.tetromino.x] = self.tetromino.type + 1
        self.remove_lines()
        self.new_tetromino()
        if self.collide():
            self.state = 'gameover'

    def left(self):
        self.__side_movement(-1)

    def right(self):
        self.__side_movement(1)

    def __side_movement(self, step: int):
        old_x = self.tetromino.x
        edge = False
        for i in range(4):
            for j in range(4):
                possible_tetromino_area = i * 4 + j
                if possible_tetromino_area in self.tetromino.image():
                    if j + self.tetromino.x + step > self.width - 1 or j + self.tetromino.x + step < 0:
                        edge = True

        if not edge:
            self.tetromino.x += step
            if self.collide():
                self.tetromino.x = old_x

    def down(self):
        while not self.collide():
            self.tetromino.y += 1
        self.tetromino.y -= 1
        self.stop()

    def rotate(self):
        old_rotation = self.tetromino.rotation
        self.tetromino.rotate()
        if self.collide():
            self.tetromino.rotation = old_rotation

    def collide(self) -> bool:
        collision = False
        for i in range(4):
            for j in range(4):
                possible_tetromino_area = i * 4 + j
                if possible_tetromino_area in self.tetromino.image():
                    if i + self.tetromino.y > self.height - 1 or i + self.tetromino.y < 0 or \
                            self.field[i + self.tetromino.y][j + self.tetromino.x] > 0:
                        collision = True
        return collision

    def remove_lines(self):
        lines = 0
        for i in range(1, self.height):
            number_of_empty_fields = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    number_of_empty_fields += 1

            if number_of_empty_fields == 0:
                lines += 1
                for i2 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i2][j] = self.field[i2 - 1][j]

        self.score += lines ** 2
