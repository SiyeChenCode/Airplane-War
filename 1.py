import pygame

def main():

    # 创建一个窗口
    screen = pygame.display.set_mode((377,580), 0, 32)
    
    # 创建一个图片，当作背景
    background = pygame.image.louad("./img/background.png")

    # 将背景图片贴到窗口
    screen.blit(background, (0, 0))

    # 显示窗口中的内容
    pygame.display.update()

if __name__ == '__main__':
    main()