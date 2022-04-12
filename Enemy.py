import random
import pygame


class Enemy(object):
    x = 0
    y = 0
    # 生命值
    hp = 3
    bullets = []

    def __init__(self, enemy_type, screen):
        self.x = random.randint(0, 480)
        self.y = 0
        self.type = enemy_type
        self.screen = screen
        if enemy_type == 0:
            self.image = pygame.image.load('./assets/enemy0.png')
        elif enemy_type == 1:
            self.image = pygame.image.load('./assets/enemy1.png')
            self.hp = 5
        elif enemy_type == 2:
            self.image = pygame.image.load('./assets/enemy2.png')
            self.hp = 8

    def move(self):
        self.y -= 5

    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
