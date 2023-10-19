import sys
from grid import Grid
from blocks import *
import pygame
gray = (37,37,37)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((440,880))
    pygame.display.set_caption("Python Tetris")

    clock = pygame.time.Clock()
    game_grid = Grid()
    block = TBlock()

    while True:
        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #Drawing
        screen.fill(gray)
        game_grid.draw(screen)
        block.draw(screen)



        pygame.display.update()
        clock.tick(60)


