#本段代码依赖background文件夹
import sys, random, time, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

#主程序
pygame.init()
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Keyboard Typing Demo")
font1 = pygame.font.Font(None, 48)
font2 = pygame.font.Font(None, 160)
font3 = pygame.font.Font(None, 80)

white = 255,255,255
yellow = 255,255,0
color = 125,100,210
green = 0,255,0

key_flag = False
correct_answer = [97,98,99,100,101,102,103,104,105,106,107,108]
cnt = 0
all_cnt = 0
seconds = 0
score = 0
clock_start = 0
game_over = True
sys_start_time = time.clock()

while True:
    for event in pygame.event.get():        #游戏退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:         #按键按下事件
            key_flag = True
        elif event.type == KEYUP:           #按键抬起事件
            key_flag = False

    keys = pygame.key.get_pressed()         #按键信息获取
    if keys[K_ESCAPE]:                      #如果按下ESC，则退出游戏
        sys.exit()

    if keys[K_RETURN]:                      #如果按下回车，则统计信息，并在11秒之后退出
        if game_over:
            game_over = False
            score = 0
            seconds = 11
            clock_start = time.clock()      #获取当前时间

    current = time.clock() - clock_start
    speed = score * 6                       #计算速度
    time_cnt = int(time.clock() - sys_start_time) + 1
    if keys[correct_answer[cnt]]:            #如果按键与字母匹配，则刷新字母
        cnt += 1
        all_cnt += 1
        if (cnt == 11):
            cnt = 0
            for i in range(0,11):
                correct_answer[i] = random.randint(97,122)
                while(correct_answer[i] == correct_answer[i-1]):
                    correct_answer[i] = random.randint(97, 122)
        if (seconds - current < 0):
            game_over = True
        else:
            score += 1

    #清屏
    if ((all_cnt%288) < 55):                #随着分数变动背景
        bgp = "./background/01.jpg"
    elif((all_cnt%288) < 110):
        bgp = "./background/02.jpg"
    elif ((all_cnt%288) < 165):
        bgp = "./background/03.jpg"
    elif ((all_cnt%288) < 220):
        bgp = "./background/04.jpg"
    elif ((all_cnt%330) < 275):
        bgp = "./background/05.jpg"
    else:
        bgp = "./background/06.jpg"

    background = pygame.image.load(bgp).convert()
    screen.blit(background, (0, 0))

    print_text(font1, 50, 50, "Please start your show during the next 10 seconds")    #打印信息

    if key_flag:                                                    #如果按键按下，则打印如下信息
        print_text(font1, 600, 0, "system detected your key-board is working...")

    if not game_over:                                               #计算时间
        print_text(font1, 50, 120, "time: " + str(int(seconds-current)))
    else:
        print_text(font1, 50, 120, "Press Enter to test your typing speed...")

    print_text(font1, 50, 180, "test record:  " + str(speed) + "  letters/min")  #计算速度

    print_text(font1, 50, 240, "You have typed  " + str(all_cnt) + "  letters")  # 计算总数
    print_text(font1, 50, 300, "Using time  " + str(time_cnt) + "  seconds")  # 计算总数
    print_text(font1, 50, 360, "Means  " + str(int(all_cnt/time_cnt*60)) + "  seconds")  # 计算总数

    for i in range(0,11):
        if(i < cnt):
            print_text(font2, 0+i*90, 480, chr(correct_answer[i] - 32), green)     #已正确打出的字
        else:
            print_text(font2, 0+i*90, 480, chr(correct_answer[i] - 32), yellow)    #未打出的字

    #更新
    pygame.display.update()
