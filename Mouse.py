background_image_filename = './background/01.jpg'
mouse_img = './Picture/D_U_U.png'
# 指定图像文件名称

import pygame
from pygame.locals import *
from sys import exit

class Mouse():
    def __init__(self, picture = './Picture/D_U_U.png',visible = True):
        self.img = picture
        pygame.mouse.set_visible(visible)
        self.Picture(picture)

    def Picture(self,picture):
        self.img = picture
        self.cursor = pygame.image.load(self.img).convert_alpha()

    def draw(self):
        self.x, self.y = pygame.mouse.get_pos()
        # 获得鼠标位置
        self.x -= mouse_cursor.get_width() / 2
        self.y -= mouse_cursor.get_height() / 2
        screen.blit(self.cursor, (self.x, self.y))

    def set_visibal(self,visible):
        pygame.mouse.set_visible(visible)

pygame.init()
# 初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((1024, 768), 0, 32)
# 创建了一个窗口
pygame.display.set_caption("Hello, World!")
# 设置窗口标题

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_img).convert_alpha()
# 加载并转换图像

mouse = Mouse(visible=False)
while True:
    # 游戏主循环
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse.Picture('./Picture/D_U_A.png')
        if event.type == MOUSEBUTTONUP:
            mouse.Picture('./Picture/D_U_U.png')

    screen.blit(background, (0,0))
    mouse.draw()
    # 把光标画上去

    pygame.display.update()
