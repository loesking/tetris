import pygame
from Tetris import Tetris

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


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption('Tetris')

    done = False
    fps = 2
    clock = pygame.time.Clock()
    counter = 0
    zoom = 30

    game = Tetris(20, 10)
    pressing_down = False
    pressing_left = False
    pressing_right = False

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)

    while not done:
        if game.state == 'start':
            game.tetromino_fall()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    pressing_down = True
                if event.key == pygame.K_LEFT:
                    pressing_left = True
                if event.key == pygame.K_RIGHT:
                    pressing_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    pressing_down = False
                if event.key == pygame.K_LEFT:
                    pressing_left = False
                if event.key == pygame.K_RIGHT:
                    pressing_right = False

            if pressing_down:
                game.down()

            if pressing_left:
                game.left()

            if pressing_right:
                game.right()

        screen.fill(color=WHITE)
        for i in range(game.height):
            for j in range(game.width):
                if game.field[i][j] == 0:
                    color = GREY
                    border = 1
                else:
                    color = colors[game.field[i][j]]
                    border = 0

                pygame.draw.rect(screen, color, [25 + j * zoom, 15 + i * zoom, zoom, zoom], border)
        if game.tetromino is not None:
            for i in range(4):
                for j in range(4):
                    possible_tetromino_area = i * 4 + j
                    if possible_tetromino_area in game.tetromino.image():
                        pygame.draw.rect(screen, game.tetromino.color,
                                         [25 + (j + game.tetromino.x) * zoom, 15 + (i + game.tetromino.y) * zoom, zoom,
                                          zoom])
        gameover_font = pygame.font.SysFont('Calibri', 65, True, False)
        gameover_text = gameover_font.render('Game Over!', True, (0, 0, 0))

        if game.state == 'gameover':
            screen.blit(gameover_text, [30, 180])

        score_font = pygame.font.SysFont('Calibri', 25, True, False)
        score_text = score_font.render('Score: ' + game.score.__str__(), True, (0, 0, 0))
        screen.blit(score_text, [370, 20])

        if game.state == 'gameover':
            screen.blit(gameover_text, [30, 180])

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
