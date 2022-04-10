import pygame
import Bullet


class Player(object):
    bullets = []

    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./assets/hero.gif")

    def update(self):
        self.screen.blit(self.image, (self.x, self.y))
        for index, bullet in enumerate(self.bullets):
            if bullet.status == 0:
                bullet.update()
                bullet.move()
            else:
                del self.bullets[index]

    def move_left(self):
        if self.x - 5 <= 0:
            self.x = 0
            return
        self.x -= 5
        self.update()

    def move_right(self):
        # 需要减去飞机本身的大小
        if self.x + 5 >= 380:
            self.x = 380
            return
        self.x += 5

    def move_up(self):
        if self.y - 5 <= 0:
            self.y = 0
            return
        self.y -= 5

    def move_down(self):
        # 需要减去飞机本身的大小
        if self.y + 5 >= (852 - 124):
            self.y = 852 - 124
            return
        self.y += 5

    # 发射子弹
    def fire(self):
        bullet = Bullet.Bullet(self.x + 50 - 11, self.y - 5, 0, self.screen)
        self.bullets.append(bullet)
