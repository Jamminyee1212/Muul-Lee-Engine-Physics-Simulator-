import pygame as pg
import time
import math

#초기설정
pg.font.init()
font = pg.font.SysFont("arial",30,True,True)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

GRAY = (128,128,128)
WHITE = (255,255,255)
BLACK = (0,0,0)

pg.init()
pg.display.set_caption("Acceleration (2d)")
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#변수 설정
block_pos = [SCREEN_WIDTH/2,SCREEN_HEIGHT/2] #[0]: X axis, [1]: Y axis
block_speed = [0,0] #[0]: X axis, [1]: Y axis
block_acceleration = [0.07,0.07] #[0]: X axis, [1]: Y axis
resist_val = [0.01,0.01] #[0]: X axis, [1]: Y axis
resist = [resist_val[0],resist_val[1]] #[0]: X axis, [1]: Y axis
'''pressed_0 = False
pressed_1 = False
pressed_2 = False
pressed_3 = False
pressed_4 = False
pressed_5 = False
pressed_6 = False
pressed_7 = False
pressed_8 = False'''

#본 코드
clock = pg.time.Clock()
runcode = True
while runcode:
    clock.tick(100)
    for event in pg.event.get():
        #종료 코드
        if event.type == pg.QUIT:
            runcode = False

    #입력 받기
    key_event = pg.key.get_pressed()

    #가속 및 급정지 기능
    if key_event[pg.K_LEFT]:
        block_speed[0]-=block_acceleration[0]
    if key_event[pg.K_RIGHT]:
        block_speed[0]+=block_acceleration[0]
    if key_event[pg.K_UP]:
        block_speed[1]-=block_acceleration[1]
    if key_event[pg.K_DOWN]:
        block_speed[1]+=block_acceleration[1]
    if key_event[pg.K_SPACE]:
        block_speed[0]=0
        block_speed[1]=0

    #마찰력 제거 기능(0)
    if key_event[pg.K_0] and not pressed_0:
        if resist[0] == 0:
            resist[0] = resist_val[0]
            resist[1] = resist_val[1]
        else:
            resist[0] = 0
            resist[1] = 0
        pressed_0=True
    elif not key_event[pg.K_0]:
        pressed_0=False

    #마찰 적용
    if block_speed[0] > 0:
        block_speed[0] -= resist[0]
        if block_speed[0] < 0: block_speed[0] = 0
    elif block_speed[0] < 0:
        block_speed[0] += resist[0]
        if block_speed[0] > 0: block_speed[0] = 0

    if block_speed[1] > 0:
        block_speed[1] -= resist[1]
        if block_speed[1] < 0: block_speed[1] = 0
    elif block_speed[1] < 0:
        block_speed[1] += resist[1]
        if block_speed[1] > 0: block_speed[1] = 0

    #튕기기(X축)
    if block_pos[0]+block_speed[0] <= SCREEN_WIDTH-15 and block_pos[0]+block_speed[0] >= 15:
        block_pos[0]+=block_speed[0]
    else :
        block_speed[0]*=((-1)/2)

    #튕기기(Y축)
    if block_pos[1]+block_speed[1] <= SCREEN_HEIGHT-15 and block_pos[1]+block_speed[1] >= 15:
        block_pos[1]+=block_speed[1]
    else :
        block_speed[1]*=((-1)/2)

    #표시
    time.sleep(0.01)
    screen.fill(WHITE)
    pg.draw.circle(screen, GRAY, [block_pos[0],block_pos[1]], 15)
   
    speed_text = font.render("Speed : " + str(int(math.sqrt((block_speed[0]*100)**2+int(block_speed[1]*100)**2)*100)/100) + "cm/s", True, BLACK)
    screen.blit(speed_text,(30,20))
    a_text = font.render("Acceleration : " + str(int(block_acceleration[0]*1000)/1000) + "m/s^2", True, BLACK)
    screen.blit(a_text,(30,50))
    r_text = font.render("Resist : " + str(int(resist[0]*1000)/1000) + "N", True, BLACK)
    screen.blit(r_text,(30,80))
    info_text = font.render("(Mass: 1.0kg, Size: " + str(SCREEN_WIDTH/100) + "x" + str(SCREEN_HEIGHT/100) + "(m^2))", True, BLACK)
    screen.blit(info_text,(30,110))
    
    pg.display.flip()
pg.quit()
