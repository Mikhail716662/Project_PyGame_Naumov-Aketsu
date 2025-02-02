import sys
from typing import Tuple, Any

import winsound
from pygame_menu.examples.other.maze import WHITE
import pygame_menu
from pygame_menu.examples import create_example_window
from data.classes import *
from data.config import *
from levels.levels import level_list


def terminate():
    pygame.quit()
    sys.exit()


def game_cycle(difficulty):
    level_string = level_list[difficulty]
    platforms, player_start_x, player_start_y, finish_point, spikes = create_level_from_string(level_string)
    player = Player(player_start_x, player_start_y)

    # Игровой цикл
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.jump()
        if keys[pygame.K_LEFT]:
            player.move_x(-1, platforms)
        if keys[pygame.K_RIGHT]:
            player.move_x(1, platforms)
        if keys[pygame.K_ESCAPE]:
            menu()
            running = False

        player.update(platforms, finish_point, spikes)
        if player.rect.colliderect(finish_point.rect):
            if difficulty == 4:
                winsound.PlaySound('sounds/level_complete.wav', winsound.SND_FILENAME)
                menu()
                running = False
            else:
                winsound.PlaySound('sounds/level_complete.wav', winsound.SND_FILENAME)
                game_cycle(difficulty + 1)
                running = False

        for spike in spikes:
            if player.rect.colliderect(spike.rect):
                winsound.PlaySound('sounds/death.wav', winsound.SND_FILENAME)
                game_cycle(difficulty)
                running = False

        screen.fill((255, 255, 255))
        player.draw()
        for platform in platforms:
            platform.draw()
        finish_point.draw()
        for spike in spikes:
            spike.draw()
        pygame.display.flip()
    terminate()


def rules_screen():
    rules_text = ["ПРАВИЛА",
                  "",
                  "Нельзя врезаться в шипы, иначе - поражение",
                  "Цель - дойти до финиша, отмеченного как желтый квадрат",
                  "Всего есть 5 уровней разной сложности",
                  "",
                  "Управление - стрелочками:",
                  "",
                  "Вправо - стрелка вправо",
                  "Влево - стрелка влево",
                  "Прыжок - стрелка вверх",
                  "",
                  "Для выхода из игры в главное меню нажать ESCAPE",
                  "Для выхода из меню правил - нажмите мышкой в любом месте экрана"]
    screen.fill(WHITE)
    text_coord = 60
    for line in rules_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        rules_rect = string_rendered.get_rect()
        rules_rect.top = text_coord
        rules_rect.x = 50
        screen.blit(string_rendered, rules_rect)
        text_coord += rules_rect.height + 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONUP:
                return
        pygame.display.flip()
        clock.tick(FPS)


def create_level_from_string(level_string):
    platforms = []
    player_start_x = 0
    player_start_y = 0
    finish_x = 0
    finish_y = 0
    spikes = []
    rows = level_string.strip().split('\n')
    for row_index, row in enumerate(rows):
        platform_start = None
        for col_index, cell in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE

            if cell == '-':
                if platform_start is None:
                    platform_start = x
            elif cell == '.' or cell == '@' or cell == 'F' or cell == '^':
                if platform_start is not None:
                    platforms.append(Platform(platform_start, y, x - platform_start))
                    platform_start = None
            if cell == '@':
                player_start_x = x
                player_start_y = y
            if cell == 'F':
                finish_x = x
                finish_y = y
            if cell == '^':
                spikes.append(Spike(x, y))
        if platform_start is not None:
            platforms.append(Platform(platform_start, y, WIDTH - platform_start if len(row) > 0 else 0))

    finish_point = FinishPoint(finish_x, finish_y)
    return platforms, player_start_x, player_start_y, finish_point, spikes


def set_difficulty(selected: Tuple, value: Any) -> None:
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

    menu.add.selector('Сложность: ',
                      [('Уровень 1', 0), ('Уровень 2', 1), ('Уровень 3', 2), ('Уровень 4', 3), ('Уровень 5', 4)],
                      onchange=set_difficulty)
    menu.add.button('Правила', rules_screen)
    menu.add.button('Играть', lambda: game_cycle(DIFFICULTY))
    menu.add.button('Выход', terminate)
    menu.mainloop(surface)
