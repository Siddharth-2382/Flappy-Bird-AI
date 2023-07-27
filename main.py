import pygame
import os

from Bird import Bird
from Pipe import Pipe
from Base import Base

pygame.font.init()
pygame.display.set_caption("Flappy Bird")

WIN_WIDTH = 400
WIN_HEIGHT = 700

BASE_IMG = pygame.transform.scale_by(surface=pygame.image.load(os.path.join("images", "base.png")), factor=1.5)
BG_IMG = pygame.transform.scale_by(surface=pygame.image.load(os.path.join("images", "bg.png")), factor=1.5)

STAT_FONT = pygame.font.SysFont("comicsans", 25)
GAMEOVER_FONT = pygame.font.SysFont("comicsans", 50)


def draw_window(win, bird, pipes, base, score, gameover):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    base.draw(win)
    bird.draw(win)

    if gameover:
        text = GAMEOVER_FONT.render("GAMEOVER", 1, (0, 0, 0))
        win.blit(text, (WIN_WIDTH - (WIN_WIDTH/8) - text.get_width(), WIN_HEIGHT / 2 - 50))
        text = STAT_FONT.render("PRESS 'R' to Restart", 1, (0, 0, 0))
        win.blit(text, (WIN_WIDTH - (WIN_WIDTH / 6) - text.get_width(), WIN_HEIGHT / 4 - 50))
    pygame.display.update()


def main():
    score = 0
    gameover = False
    bird = Bird(150, 300)
    base = Base(600)
    pipes = [Pipe(500)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True
    paused = False

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                if paused:
                    if event.key == pygame.K_r:
                        main()

        if not paused:
            bird.move()
            add_pipe = False
            removed_pipes = []
            for pipe in pipes:
                if pipe.collide(bird):
                    gameover = True
                    paused = True
                if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                    removed_pipes.append(pipe)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

                pipe.move()

            if add_pipe:
                score += 1
                pipes.append(Pipe(450))

            for rp in removed_pipes:
                pipes.remove(rp)

            if bird.y + bird.img.get_height() >= 600 or bird.y < 0:
                gameover = True
                paused = True

            base.move()
            draw_window(win, bird, pipes, base, score, gameover)

        if paused:
            pass

    pygame.quit()
    quit()


main()
