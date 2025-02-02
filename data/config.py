import pygame

GAME_NAME = "Simple Platformer"
SIZE = WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 40
SPIKE_SIZE = 40
SPIKE_COLOR = (255, 0, 0)
PLATFORM_HEIGHT = 20
PLAYER_COLOR = (0, 128, 255)
PLATFORM_COLOR = (100, 100, 100)
GRAVITY = 1
JUMP_SPEED = -15
MOVE_SPEED = 5
AIR_MOVE_SPEED = 3
TILE_SIZE = 40
FINISH_SIZE = 40
FINISH_COLOR = (255, 255, 0)
DIFFICULTY = 0
FPS = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

