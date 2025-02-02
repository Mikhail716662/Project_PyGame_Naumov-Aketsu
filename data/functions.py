import random
import sys
from typing import Tuple, Any
from data import *

import pygame

from data.classes import Player, Platform
import pygame_menu
from pygame_menu.examples import create_example_window

# Внутренние зависимости:
from data.classes import *


def terminate():
    """Выход из игры"""
    pygame.quit()
    sys.exit()


def game_cycle(user_name, difficulty):
    collides = False
    background_image = pygame.transform.scale(pygame.image.load('images/fon.png'), SIZE)
    screen.blit(background_image, (0, 0))  # Выводим фон
    player = Player(600, 400)
    player_group.add(player)
    # Перед началом игрового цикла создадим камеру:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        screen.fill(0)
        # screen.blit(background_image, (0, 0))  # Выводим фон
        tiles_group.draw(screen)
        player_group.draw(screen)
        # if player.rect.colliderect(platform.rect):
        #     collides = True
        player.update(collides)
        # Выводим имя игрока:
        pygame.display.flip()
        clock.tick(FPS)
    terminate()


def rules_screen():
    rules_text = ["Правила игры",
                  "",
                  "Перемещаться можно ТОЛЬКО по платформам",
                  "Нельзя врезаться в шипы, иначе - поражение",
                  "Цель - дойти до финиша, отмеченного как портал"]
    background_image = pygame.transform.scale(pygame.image.load('images/fon.png'), SIZE)
    screen.blit(background_image, (0, 0))  # Выводим фон
    text_coord = 60
    for line in rules_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        rules_rect = string_rendered.get_rect()
        rules_rect.top = text_coord + 200  # Записываем новые координаты у
        rules_rect.x = 500  # Отступ текста от левого края
        screen.blit(string_rendered, rules_rect)
        text_coord += rules_rect.height + 10  # Переводим строку текста

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                return  # Закрываем окно правил и возвращаемся обратно в меню
        pygame.display.flip()
        clock.tick(FPS)


def set_difficulty(selected: Tuple, value: Any) -> None:
    """
    Set the difficulty of the game.
    """
    print(f'Set difficulty to {selected[0]} ({value})')
    global DIFFICULTY
    DIFFICULTY = value
    print("DIFFICULTY ", DIFFICULTY)


def menu():
    surface = create_example_window(GAME_NAME, SIZE)
    menu = pygame_menu.Menu(
        height=HEIGHT,
        theme=pygame_menu.themes.THEME_BLUE,
        title=GAME_NAME,
        width=WIDTH
    )

    user_name = menu.add.text_input('Представься: ', default=GAME_NAME, maxchar=10)
    menu.add.selector('Сложность: ', [('Уровень 1', 0)], onchange=set_difficulty)
    menu.add.button('Правила', rules_screen)
    menu.add.button('Играть', lambda: game_cycle(user_name.get_value(), DIFFICULTY))
    menu.add.button('Выход', terminate)
    menu.mainloop(surface)
