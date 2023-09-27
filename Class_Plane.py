import pygame
import time
# from time import *
from pygame import *

pygame.init()
clock = pygame.time.Clock()

class Plane(object):
    def __init__(self, screen):
        # 创建一个图片，玩家飞机
        self.player = pygame.image.load(r'D:\code\Airplane-War\img\plane.jpg')
        
        # 定义飞机的坐标
        self.x = 140
        self.y = 453

        # 飞机速度
        self.speed = 10

        # 记录当前窗口对象
        self.screen = screen

        # 装子弹的列表
        self.bullets = []

    def key_control(self):
        # 持续监听键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            # print('up')
            self.y -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            # print('down')
            self.y += self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            # print('left')
            self.x -= self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            # print('right')
            self.x += self.speed
        if key_pressed[K_SPACE]:
            # 按下空格键发射子弹
            bullet = Bullet(self.screen, self.x, self.y)
            # 把子弹放到列表里
            self.bullets.append(bullet)
            # pass
            # print('space')

    def display(self):
        # 将背景图片贴到窗口
        self.screen.blit(self.player, (self.x,self.y))
        # 遍历所有子弹
        for bullet in self.bullets:
            # 子弹显示在窗口
            bullet.display()

# 子弹类
# 属性
class Bullet(object):
    def __init__(self, screen, x, y):
        # 坐标
        self.x = 150
        self.y = 150
        # 图片
        self.image = pygame.image.load(r'D:\code\Airplane-War\img\plane.jpg')
        # 窗口
        self.screen = screen
        # 速度
        self.speed = 10

    def display(self):
        # 显示子弹到窗口
        self.screen.blit(self.image, (self.x, self.y))

def main():

    # 创建一个窗口
    screen = pygame.display.set_mode((377,580), 0, 32)
    
    # 创建一个图片，当作背景
    background = pygame.image.load(r'D:\code\Airplane-War\img\background.png')

    player = Plane(screen)

    while True:
        # 将背景图片贴到窗口
        screen.blit(background, (0, 0))

        # 获取事件
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == pygame.QUIT:
                # 执行pygame退出
                pygame.quit()
                # python程序退出
                exit()

        # 执行飞机的按键监听
        player.key_control()
        # 飞机的显示
        player.display()

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




        # 显示窗口中的内容
        pygame.display.update()
        # time.sleep(0.01)
        clock.tick(60) # 调整速度，越小越慢

if __name__ == '__main__':
    main()