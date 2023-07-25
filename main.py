import pygame
import neat
import os
import random
import time

from Bird import Bird

WIN_WIDTH = 400
WIN_HEIGHT = 600

BASE_IMG = pygame.transform.scale_by(surface=pygame.image.load(os.path.join("images", "base.png")), factor=1.5)
BG_IMG = pygame.transform.scale_by(surface=pygame.image.load(os.path.join("images", "bg.png")), factor=1.5)


def draw_window(win, bird):
    win.blit(BG_IMG, (0, 0))
    bird.draw(win)
    pygame.display.update()


def main():
    bird = Bird(133, 133)
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # bird.move()
        draw_window(win, bird)

    pygame.quit()
    quit()


main()
