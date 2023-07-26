import pygame
import neat
import os
import pickle

from Bird import Bird
from Pipe import Pipe
from Base import Base

pygame.font.init()
pygame.display.set_caption("Flappy Bird")

WIN_WIDTH = 400
WIN_HEIGHT = 700

BG_IMG = pygame.transform.scale_by(surface=pygame.image.load(os.path.join("images", "bg.png")), factor=1.5)

STAT_FONT = pygame.font.SysFont("comicsans", 25)
GAMEOVER_FONT = pygame.font.SysFont("comicsans", 50)
GEN = 0


def draw_window(win, birds, pipes, base, score, gameover, gen, alive):
    win.blit(BG_IMG, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render("Gen: " + str(gen), 1, (255, 255, 255))
    win.blit(text, (10, 10))

    text = STAT_FONT.render("Alive: " + str(alive), 1, (255, 255, 255))
    win.blit(text, (10, 50))

    base.draw(win)

    for bird in birds:
        bird.draw(win)

    if gameover:
        text = GAMEOVER_FONT.render("GAMEOVER ", 1, (0, 0, 0))
        win.blit(text, (WIN_WIDTH - (WIN_WIDTH / 8) - text.get_width(), WIN_HEIGHT / 2 - 50))
    pygame.display.update()


def genome_evaluation(genomes, config):
    global GEN
    GEN += 1
    score = 0
    gameover = False
    network_list = []
    genome_list = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        network_list.append(net)
        birds.append(Bird(150, 300))
        g.fitness = 0
        genome_list.append(g)

    base = Base(600)
    pipes = [Pipe(500)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            break

        for x, bird in enumerate(birds):
            bird.move()
            genome_list[x].fitness += 0.1

            output = network_list[x].activate((bird.y,
                                               abs(bird.y - pipes[pipe_ind].height),
                                               abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:
                bird.jump()

        add_pipe = False
        removed_pipes = []
        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    genome_list[x].fitness -= 1
                    birds.pop(x)
                    network_list.pop(x)
                    genome_list.pop(x)

                if bird.y + bird.img.get_height() >= 600 or bird.y < 0:
                    birds.pop(x)
                    network_list.pop(x)
                    genome_list.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                removed_pipes.append(pipe)

            pipe.move()

        if add_pipe:
            score += 1
            for g in genome_list:
                g.fitness += 5
            pipes.append(Pipe(450))

        for rp in removed_pipes:
            pipes.remove(rp)

        if score > 100:
            break
        base.move()
        draw_window(win, birds, pipes, base, score, gameover, GEN, len(birds))


def run_config(configuration_file_path, save_file_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                neat.DefaultStagnation, configuration_file_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(genome_evaluation, 50)

    # Save the winning genome to a pickle file
    with open(save_file_path, 'wb') as f:
        pickle.dump(winner, f)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    save_path = os.path.join(local_dir, "winner_genome.pkl")  # Replace 'winner_genome.pkl' with your desired filename
    run_config(config_path, save_path)
