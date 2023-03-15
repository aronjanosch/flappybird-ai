import os.path
import random
import pygame
import sys
from pygame.locals import *
from player import Player
from pipe import Pipe


FPS = 45

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bg.png")))

def init():

    pygame.display.set_caption('Flappy Bird Game')
    clock = pygame.time.Clock()
    clock.tick(FPS)


def draw_window(win: pygame.Surface, player, pipes):
    win.fill(WHITE)
    for pipe in pipes:
        pipe.draw(win)

    player.draw(win)
    pygame.display.update()


def main():
    player = Player(150, 200)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((500, 800))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        user_input = pygame.key.get_pressed()
        player.move(user_input)

        rem = []
        add_pipe = False
        for pipe in pipes:
            if pipe.x + pipe.width < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < 300:
                pipe.passed = True
                add_pipe = True
            pipe.move()

        if add_pipe:
            pipes.append(Pipe(600))

        for r in rem:
            pipes.remove(r)
        draw_window(win, player, pipes)
    pygame.quit()
    quit()


if __name__ == "__main__":
    while True:
        main()
