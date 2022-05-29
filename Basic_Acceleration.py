import pygame as pg
import time
import math

pg.font.init()
font = pg.font.SysFont("arial",30,True,True)

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 480

GRAY = (128,128,128)
WHITE = (255,255,255)
BLACK = (0,0,0)

pg.init()
pg.display.set_caption("Acceleration")
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

block_pos = SCREEN_WIDTH/2
block_speed = 0
block_acceleration = 0.05
resist_val = 0.01
resist = resist_val
first_moved = False
pressed_0 = False
pressed_1 = False
pressed_2 = False
pressed_3 = False
pressed_4 = False
pressed_5 = False
pressed_6 = False
pressed_7 = False
pressed_8 = False

clock = pg.time.Clock()
runcode = True
while runcode:
    clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runcode = False

    key_event = pg.key.get_pressed()
    if key_event[pg.K_LEFT]:
        first_moved = True
        block_speed-=block_acceleration
    if key_event[pg.K_RIGHT]:
        first_moved = True
        block_speed+=block_acceleration
    if key_event[pg.K_SPACE]:
        block_speed=0

    
    if key_event[pg.K_0] and not pressed_0:
        if resist == 0: resist = resist_val
        else: resist = 0
        pressed_0=True
    elif not key_event[pg.K_0]:
        pressed_0=False

    if key_event[pg.K_1] and not pressed_1:
        block_acceleration+=0.005
        pressed_1=True
    elif not key_event[pg.K_1]:
        pressed_1=False

    if key_event[pg.K_2] and not pressed_2:
        if block_acceleration>=0.005: block_acceleration-=0.005
        else: block_acceleration=0
        pressed_2=True
    elif not key_event[pg.K_2]:
        pressed_2=False

    if key_event[pg.K_3] and not pressed_3:
        resist+=0.005
        pressed_3=True
    elif not key_event[pg.K_3]:
        pressed_3=False

    if key_event[pg.K_4] and not pressed_4:
        if resist>=0.005: resist-=0.005
        else: resist=0
        pressed_4=True
    elif not key_event[pg.K_4]:
        pressed_4=False


    if key_event[pg.K_5] and not pressed_5:
        block_acceleration+=0.05
        pressed_5=True
    elif not key_event[pg.K_5]:
        pressed_5=False

    if key_event[pg.K_6] and not pressed_6:
        if block_acceleration>=0.05: block_acceleration-=0.05
        else: block_acceleration=0
        pressed_6=True
    elif not key_event[pg.K_6]:
        pressed_6=False

    if key_event[pg.K_7] and not pressed_7:
        resist+=0.05
        pressed_7=True
    elif not key_event[pg.K_7]:
        pressed_7=False

    if key_event[pg.K_8] and not pressed_8:
        if resist>=0.05: resist-=0.05
        else: resist=0
        pressed_8=True
    elif not key_event[pg.K_8]:
        pressed_8=False

    if key_event[pg.K_0] and not pressed_0:
        if resist == 0: resist = resist_val
        else: resist = 0
        pressed_0=True
    elif not key_event[pg.K_0]:
        pressed_0=False

        
    if block_speed > 0:
        block_speed -= resist
        if block_speed < 0: block_speed = 0
    elif block_speed < 0:
        block_speed += resist
        if block_speed > 0: block_speed = 0
    
    if block_pos+block_speed <= SCREEN_WIDTH-15 and block_pos+block_speed >= 15:
        block_pos+=block_speed
    else :
        block_speed*=((-1)/math.sqrt(4))

    if block_speed > (-1)*block_acceleration/2 and block_speed < block_acceleration/2 and first_moved and block_pos >= 1 and block_pos <= SCREEN_WIDTH:
        #print(int(block_pos))
        first_moved = False
    
    time.sleep(0.01)
    screen.fill(WHITE)
    pg.draw.rect(screen, GRAY, [block_pos-15, SCREEN_HEIGHT*5/8-30, 30, 30])
    pg.draw.rect(screen, BLACK, [0, SCREEN_HEIGHT*5/8, SCREEN_WIDTH, SCREEN_HEIGHT*3/8])

    speed_text = font.render("Speed : " + str(int(block_speed*1000)/1000) + "m/s", True, BLACK)
    screen.blit(speed_text,(30,20))
    a_text = font.render("Acceleration : " + str(int(block_acceleration*1000)/1000) + "m/s^2", True, BLACK)
    screen.blit(a_text,(30,50))
    r_text = font.render("Resist : " + str(int(resist*1000)/1000) + "N", True, BLACK)
    screen.blit(r_text,(30,80))
    info_text = font.render("(Mass: 1.0kg, Distance: " + str(SCREEN_WIDTH/100) + "m)", True, BLACK)
    screen.blit(info_text,(30,110))
    
    pg.display.flip()
pg.quit()
