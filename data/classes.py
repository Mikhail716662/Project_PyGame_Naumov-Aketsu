import time

import pygame


class Main_Menu:
    pass


class Player(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load('images/image.png')
        self.rect = self.image.get_rect(center=(x, 0))
        self.rect.center = (1280 / 2, 1024 / 2)

    def update(self):
        self.speedx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx = -3
        if key[pygame.K_RIGHT]:
            self.speedx = 3
        self.rect.x += self.speedx


class Spike:
    pass


class Lava:
    pass


class End_Level_Menu:
    pass


class Records_Menu:
    pass


class Settings_Menu:
    pass


class Platform:
    pass


class Finish_Point:
    pass
