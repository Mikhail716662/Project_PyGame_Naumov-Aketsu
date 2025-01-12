import time

import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.image.load("images/image1.png")
        # self.image = pygame.transform.rotozoom(self.image, 0, 1.94)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = size[1]


class Player(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load('images/image.png')
        self.rect = self.image.get_rect(center=(x, 0))
        self.rect.center = (1280 / 2, 720 / 2)

    def update(self):
        self.speedx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx = -15
        if key[pygame.K_RIGHT]:
            self.speedx = 15
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
