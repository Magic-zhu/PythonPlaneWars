import pygame


class Bullet:
    # 是否需要被销毁
    status = 0

    def __init__(self, x, y, type, screen):
        self.x = x
        self.y = y
        self.type = type
        self.screen = screen
        self.image = pygame.image.load('./assets/bullet.png')

    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
        if self.y < 0:
            self.destroy()

    def move(self):
        self.y -= 5

    def destroy(self):
        self.status = 1
