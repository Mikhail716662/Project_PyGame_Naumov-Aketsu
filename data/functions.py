import random

import pygame

from data.classes import Player


def main():
    pygame.init()
    size = 1280, 1024
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    player = Player(random.randint(1, size[0]))
    all_sprites.add(player)
    running = True
    fps = 60

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("gray")
        screen.blit(player.image, player.rect)
        pygame.display.update()
        pygame.display.flip()
        dt = clock.tick(fps) / 1000
        player.update()

    pygame.quit()