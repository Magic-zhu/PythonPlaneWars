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
        if scene.status == 'start':
            scene.player.update()
        if scene.status == 'stop':
            scene.startButton.update()
        pygame.display.flip()
        key_control(scene)
        time.sleep(0.02)


def key_control(scene):
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
                scene.player.move_left()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                scene.player.move_right()
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                scene.player.move_up()
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                scene.player.move_down()
            elif event.key == pygame.K_SPACE:
                if time.time() - clock > 0.5:
                    scene.player.fire()
                    clock = time.time()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (174 <= x <= 306) and (600 <= y <= 648):
                scene.start()


main()
