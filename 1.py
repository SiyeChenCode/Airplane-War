import pygame
import time
# from time import *
from pygame import *
pygame.init()
clock = pygame.time.Clock()

def main():

    # 创建一个窗口
    screen = pygame.display.set_mode((377,580), 0, 32)
    
    # 创建一个图片，当作背景
    background = pygame.image.load(r'D:\code\Airplane-War\img\background.png')

    # 创建一个图片，玩家飞机
    player = pygame.image.load(r'D:\code\Airplane-War\img\plane.jpg')
    
    # 定义飞机的坐标
    x = 140
    y = 453

    # 飞机速度
    speed = 10

    while True:
        # 将背景图片贴到窗口
        screen.blit(background, (0, 0))
        # 将背景图片贴到窗口
        screen.blit(player, (x,y))
        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == pygame.QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序退出
                exit()

            # # 监听按键盘的事件
            # elif event.type == pygame.KEYDOWN:
            #     # 检验按键是否是a或者left
            #     if event.key == K_a or event.key == K_LEFT:
            #         print('left')
            #     # 检查按键是否是d或者right
            #     elif event.key == K_d or event.key == K_RIGHT:
            #         print('right')
            #     # 检查按键是否是空格
            #     elif event.key == K_SPACE:
            #         print('space')

        # 持续监听键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            print('up')
            y -= speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            print('down')
            y += speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print('left')
            x -= speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print('right')
            x += speed
        if key_pressed[K_SPACE]:
            print('space')


        # 显示窗口中的内容
        pygame.display.update()
        # time.sleep(0.01)
        clock.tick(60) # 调整速度，越小越慢

if __name__ == '__main__':
    main()