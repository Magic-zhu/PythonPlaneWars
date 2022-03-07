import pygame
import sys

pygame.init()
# 窗口设置
pygame.display.set_caption('plane wars')
screen = pygame.display.set_mode((480, 852))


class Player:
    def __init__(self):
        self.x = 210
        self.y = 110

    def move_left(self):
        if self.x >= 2:
            self.x -= 2
        else:
            self.x = 0


def main():
    while True:
        # 循环获取事件，监听事件
        for event in pygame.event.get():
            # 判断用户是否点了关闭按钮
            if event.type == pygame.QUIT:
                # 卸载所有模块
                pygame.quit()
                # 终止程序
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('left')
                if event.key == pygame.K_d or event.key == pygame.K_LEFT:
                    print('right')
                if event.key == pygame.K_s or event.key == pygame.K_LEFT:
                    print('up')
                if event.key == pygame.K_w or event.key == pygame.K_LEFT:
                    print('down')
        # 更新屏幕内容
        pygame.display.flip()


if __name__ == '__main__':
    main()
