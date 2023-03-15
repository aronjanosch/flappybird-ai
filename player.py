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
        self.flap = True
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self, user_input):
        self.tick_count += 1

        self.vel += 0.5

        if self.vel >= 16:
            self.vel = 16
        if self.y < 1000:
            self.y += int(self.vel)
            if self.vel == -2:
                self.flap = False

        if user_input[pygame.K_SPACE] and not self.flap and self.y > 0:
            self.jump()



    def draw(self, win):
        """
        draw the player
        :param win: pygame window
        :return: None
        """

        pygame.draw.circle(win, BLACK, (self.x, self.y), 25)


