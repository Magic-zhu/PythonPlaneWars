# -*- coding:utf-8 -*-
import Scene
import pygame
import time

global clock
clock = 0


def main():
    scene = Scene.Scene()
    while True:
        scene.update()
        scene.player.update()
        pygame.display.flip()
        key_control(scene.player)
        time.sleep(0.02)


def key_control(player):
    global clock
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
                if time.time() - clock > 0.5:
                    player.fire()
                    clock = time.time()


main()
