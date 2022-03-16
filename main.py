# -*- coding:utf-8 -*-

import pygame
import time

class Plane():{

}

class Player(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./assets/hero1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        if self.x - 5 <= 0:
            self.x = 0
            return
        self.x -= 5

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
        if self.y + 5 >= (852-124):
            self.y = 852-124
            return
        self.y += 5


def key_control(player):
    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == pygame.QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.move_down()
            elif event.key == pygame.K_SPACE:
                print('space')


def main():
    # 1. 创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    pygame.display.set_caption('飞机大战')

    # 2. 键盘持续响应
    pygame.key.set_repeat(10, 15)

    # 3. 创建一个背景图片
    background = pygame.image.load("./assets/background.png")

    # 4. 创建一个飞机对象
    player = Player(screen)

    while True:
        screen.blit(background, (0, 0))
        player.display()
        pygame.display.update()
        key_control(player)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
