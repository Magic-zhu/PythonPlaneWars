import pygame
import Player


class StartButton:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface((132, 48))
        self.bg = pygame.image.load('./assets/button_nor.png')
        self.text = pygame.image.load('./assets/restart_sel.png')
        self.surface.blit(self.bg, (0, 0))
        self.surface.blit(self.text, (10, 10))

    def update(self):
        self.screen.blit(self.surface, ((480 - 132) / 2, 600))


class Scene(object):
    score = 0
    player = ''
    status = 'stop'

    def __init__(self):
        # 创建窗口
        self.screen = pygame.display.set_mode((480, 852), 0, 32)
        pygame.display.set_caption('飞机大战')
        # 键盘持续响应
        pygame.key.set_repeat(10, 30)
        # 创建一个背景图片并加载
        self.background = pygame.image.load("./assets/background.png")
        # 初始化游戏
        self.startButton = StartButton(self.screen)

    def update(self):
        self.screen.blit(self.background, (0, 0))

    def start(self):
        # 创建一个飞机对象
        self.player = Player.Player(self.screen)
        self.status = 'start'

