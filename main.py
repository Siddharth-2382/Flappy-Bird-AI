import pygame
import neat
import os
import random
import time

from Bird import Bird
from Pipe import Pipe
from Base import Base

WIN_WIDTH = 400
WIN_HEIGHT = 700

BASE_IMG = pygame.transform.scale_by(surface=pygame.image.load(os.path.join("images", "base.png")), factor=1.5)
BG_IMG = pygame.transform.scale_by(surface=pygame.image.load(os.path.join("images", "bg.png")), factor=1.5)


def draw_window(win, bird, pipes, base):
    win.blit(BG_IMG, (0, 0))
    bird.draw(win)

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    pygame.display.update()


def main():
    bird = Bird(150, 300)
    base = Base(600)
    pipes = [Pipe(500)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # bird.move()
        for pipe in pipes:
            pipe.move()
        base.move()
        draw_window(win, bird, pipes, base)

    pygame.quit()
    quit()


main()
