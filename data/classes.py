from data.config import *


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.y_vel = 0
        self.on_ground = False
        self.is_jumping = False

    def update(self, platforms, finish_point, spikes):
        if not self.on_ground:
            self.y_vel += GRAVITY
            self.rect.y += self.y_vel
            if self.y_vel > 20:
                self.y_vel = 20

        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.y_vel >= 0:
                self.rect.bottom = platform.rect.top
                self.y_vel = 0
                self.on_ground = True
                self.is_jumping = False
                break

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.y_vel = 0
            self.on_ground = True
            self.is_jumping = False

    def draw(self):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)

    def jump(self):
        if self.on_ground and not self.is_jumping:
            self.y_vel = JUMP_SPEED
            self.is_jumping = True

    def move_x(self, direction, platforms):
        if self.on_ground:
            self.rect.x += direction * MOVE_SPEED
        else:
            self.rect.x += direction * AIR_MOVE_SPEED

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Platform:
    def __init__(self, x, y, width):
        self.rect = pygame.Rect(x, y, width, PLATFORM_HEIGHT)

    def draw(self):
        pygame.draw.rect(screen, PLATFORM_COLOR, self.rect)


class FinishPoint:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, FINISH_SIZE, FINISH_SIZE)

    def draw(self):
        pygame.draw.rect(screen, FINISH_COLOR, self.rect)


class Spike:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, SPIKE_SIZE, SPIKE_SIZE)
        self.points = [
            (self.rect.centerx, self.rect.top),
            (self.rect.left, self.rect.bottom),
            (self.rect.right, self.rect.bottom)
        ]

    def draw(self):
        pygame.draw.polygon(screen, SPIKE_COLOR, self.points)
