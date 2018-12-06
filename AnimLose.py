import sys
import pygame
import random
import time
from pygame import *
from pygame.locals import *

def partLose2():
    timer = 500
    fpsClock = pygame.time.Clock()
    # pygame.init()
    pygame.mixer.init()
    musique = pygame.mixer.Sound("win_lose/crashanim.ogg")
    musique.play()

    pygame.display.set_caption('You lose :(')
    font.init()
    police = font.Font(None,48)
    WHITE = (255,255,255)
    BLUE = (0,0,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    BLACK = (0,0,0)
    PURPLE=(255,0,255)
    YELLOW=(255,255,0)
    ORANGE=(255,100,0)
    GREY=(140,150,160)

    screen = pygame.display.set_mode((620,670))
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen,BLACK,(60,100,500,510))
    pygame.draw.rect(screen,RED,(560,100,60,510))
    pygame.draw.rect(screen,RED,(0,100,60,510))
    pygame.draw.rect(screen,RED,(60,610,500,60))
    pygame.draw.rect(screen,RED,(60,40,500,60))

    for i in range(0,7):
        pygame.draw.line(screen,WHITE,(0,160+(65*i)),(620,160+(65*i)),3)

    for j in range(0,8):
        pygame.draw.line(screen,WHITE,(60+(62*j),40),(60+(62*j),690),3)

    pluie = []
    for t in range(50):
        pluie_x = random.randrange(0, 700)
        pluie_y = random.randrange(0, 700)
        pluie.append([pluie_x, pluie_y])

    laser1x=90
    laser1y=130

    laser2x=90
    laser2y=580

    laser3x=540
    laser3y=130

    laser4x=540
    laser4y=580

    while timer > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        color = (0, 255, 0)

        laser1x+=1
        laser1y+=1

        laser2x+=1
        laser2y-=1

        laser3x-=1
        laser3y+=1

        laser4x-=1
        laser4y-=1

        print(laser1x,laser1y)

        pygame.draw.circle(screen, color, (laser1x, laser1y),10)
        pygame.draw.circle(screen, color, (laser2x, laser2y),10)

        pygame.draw.circle(screen, color, (laser3x, laser3y),10)
        pygame.draw.circle(screen, color, (laser4x, laser4y),10)

        if laser1x > 340:
            laser1x = 350
            laser1y = 350
            LOOSE = pygame.image.load('win_lose/imgplateaujeu.png')
            LOOSEx = 0
            LOOSEy = 0
            LOOSE2 = pygame.image.load('win_lose/youlose.png')
            LOOSE2x = 75
            LOOSE2y = 180
            screen.blit(LOOSE,(LOOSEx,LOOSEy))
            screen.blit(LOOSE2,(LOOSE2x,LOOSE2y))

            for i in range(len(pluie)):
                pygame.draw.circle(screen, WHITE, pluie[i], 3)
                pluie[i][1] += 1
                if pluie[i][1] > 700:
                    pluie_x = random.randrange(0, 700)
                    pluie[i][0] = pluie_x
                    pluie_y = random.randrange(-40, -15)
                    pluie[i][1] = pluie_y

        
        pygame.display.update()
        fpsClock.tick(110)
        timer-=1
