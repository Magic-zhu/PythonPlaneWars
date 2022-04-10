import pygame
import Player


class Scene(object):
    def __init__(self):
        # 创建窗口
        self.screen = pygame.display.set_mode((480, 852), 0, 32)
        pygame.display.set_caption('飞机大战')
        # 键盘持续响应
        pygame.key.set_repeat(10, 30)
        # 创建一个背景图片并加载
        self.background = pygame.image.load("./assets/background.png")
        # 创建一个飞机对象
        self.player = Player.Player(self.screen)

    def update(self):
        self.screen.blit(self.background, (0, 0))
