import time

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
        self.screen.blit(self.surface, ((480 - 132) / 2, 520))


class QuitButton:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface((132, 48))
        self.bg = pygame.image.load('./assets/button_nor.png')
        self.text = pygame.image.load('./assets/quit_sel.png')
        self.surface.blit(self.bg, (0, 0))
        self.surface.blit(self.text, (10, 10))

    def update(self):
        self.screen.blit(self.surface, ((480 - 132) / 2, 600))


class Logo:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./assets/name.png')

    def update(self):
        self.screen.blit(self.image, ((480 - 429) / 2, 200))


class Loading:
    def __init__(self, screen):
        self.screen = screen
        self.step = 0
        self.loading1 = pygame.image.load('./assets/game_loading1.png')
        self.loading2 = pygame.image.load('./assets/game_loading2.png')
        self.loading3 = pygame.image.load('./assets/game_loading3.png')
        self.timer = time.time()
        self.now = self.loading1

    def update(self):
        if time.time() - self.timer < 0.2:
            self.screen.blit(self.now, ((480 - 176) / 2, 400))
            return
        else:
            self.timer = time.time()
        if self.step == 0:
            self.now = self.loading1
            self.screen.blit(self.now, ((480 - 176) / 2, 400))
            self.step = 1
            return
        if self.step == 1:
            self.now = self.loading2
            self.screen.blit(self.now, ((480 - 176) / 2, 400))
            self.step = 2
            return
        if self.step == 2:
            self.now = self.loading3
            self.screen.blit(self.now, ((480 - 176) / 2, 400))
            self.step = 0
            return


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
        self.quitButton = QuitButton(self.screen)
        self.logo = Logo(self.screen)
        self.loading = Loading(self.screen)

    def update(self):
        self.screen.blit(self.background, (0, 0))

    def start(self):
        # 创建一个飞机对象
        self.player = Player.Player(self.screen)
        self.status = 'start'
