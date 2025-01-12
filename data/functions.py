import random

import pygame

from data.classes import Player, Background


def main():
    pygame.init()
    size = 1280, 720
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Приключение зеленухи')
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    background = Background(size)
    all_sprites.add(background)
    player = Player(random.randint(1, size[0]))
    all_sprites.add(player)
    running = True
    fps = 60

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background.image, background.rect)
        screen.blit(player.image, player.rect)
        pygame.display.update()
        pygame.display.flip()
        dt = clock.tick(fps) / 1000
        player.update()

    pygame.quit()