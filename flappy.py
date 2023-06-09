import os.path
import random
import pygame
import sys
from pygame.locals import *
from player import Player
from pipe import Pipe

pygame.font.init()

FPS = 60

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

STAT_FONT = pygame.font.SysFont("comicsansms", 50)

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))


def init():

    pygame.display.set_caption('Flappy Bird Game')
    clock = pygame.time.Clock()
    clock.tick(FPS)


def draw_window(win: pygame.Surface, player, pipes, score):
    win.fill(WHITE)
    for pipe in pipes:
        pipe.draw(win)

    text = STAT_FONT.render("Score: " + str(score), True, BLACK)
    win.blit(text, (500 - 10 - text.get_width(), 10))

    player.draw(win)
    pygame.display.update()


def spawn_pipes(pipes, score, player):
    rem = []
    add_pipe = False
    for pipe in pipes:
        if pipe.x + pipe.width < 0:
            rem.append(pipe)

        if not pipe.passed and pipe.x < 350:
            pipe.passed = True
            add_pipe = True

        if not pipe.scored and pipe.x < player.x and player.alive:
            pipe.scored = True
            score += 1

        pipe.move()

    if add_pipe:
        pipes.append(Pipe(600))

    for r in rem:
        pipes.remove(r)

    return pipes, score, player


def main():
    player = Player(150, 200)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((500, 800))
    clock = pygame.time.Clock()
    run = True
    score = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        user_input = pygame.key.get_pressed()
        player.move(user_input)

        pipes, score, player = spawn_pipes(pipes, score, player)

        draw_window(win, player, pipes, score)
    pygame.quit()
    quit()


if __name__ == "__main__":
    while True:
        main()
