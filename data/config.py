import pygame

# Константы:
GAME_NAME = "Slime Platformer"
FPS = 60
SIZE = WIDTH, HEIGHT = 1920, 1080
DIFFICULTY = 0  # Сложность игры (и/или выбор уровня)

# Конфигурации PyGame:
pygame.init()

# Игровое поле
# Шрифт
font = pygame.font.Font(None, 30)

# Задержка для зажатой клавиши. Например, при движении игрока.
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()