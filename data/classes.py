import time

import pygame
from data.config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.image = pygame.image.load('images/slimee.png')
        self.rect = self.image.get_rect().move(x, y)
        self.speedx = 0
        self.speedy = 0
        self.gravity = 2

    def update(self, collides):
        self.speedx = 0
        key = pygame.key.get_pressed()
        if collides:
            self.speedy = 0
        else:
            self.speedy = self.gravity
        if key[pygame.K_LEFT]:
            self.speedx = -3
        elif key[pygame.K_RIGHT]:
            self.speedx = 3
        elif key[pygame.K_SPACE]:
            if collides:
                self.speedy = -10
            else:
                self.speedy = self.gravity
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/platforma.png')
        self.rect = self.image.get_rect().move(x, y)


class Finish_Point:
    pass
