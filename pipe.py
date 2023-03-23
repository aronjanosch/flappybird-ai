import random

import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Pipe:
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.width = 50
        self.top = 0
        self.bottom = 0
        self.gap = 150

        self.enter, self.exit = False, False
        self.passed = False
        self.scored = False

        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.gap = random.randrange(150, 200)
        self.bottom = self.height+self.gap


    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        pygame.draw.rect(win, GREEN, (self.x, 0, self.width, self.height))
        pygame.draw.rect(win, GREEN, (self.x, self.bottom, self.width, 9999))
