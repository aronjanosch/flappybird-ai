import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Player:
    """
    Player playing like a maniac
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.flap = False

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.5 * self.tick_count ** 2

        if d >= 16:
            d = 16

        print(d)
        if d < 0:
            d -= 20

        self.y = self.y + d

    def draw(self, win):
        """
        draw the player
        :param win: pygame window
        :return: None
        """

        pygame.draw.circle(win, BLACK, (self.x, self.y), 50)


