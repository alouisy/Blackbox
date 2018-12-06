import pygame
from pygame.locals import *
import sys
import pyganim
import os

def partWin2():
    timer = 200

    windowSurface = pygame.display.set_mode((670, 780))
    pygame.display.set_caption('You win :)')
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.music.load("win_lose/trap.ogg")
    pygame.mixer.music.play()
    Anim = pyganim.PygAnimation([('win_lose/0.gif', 0.1),
                                     ('win_lose/1.gif', 0.1),
                                     ('win_lose/2.gif', 0.1)])
    Anim.play()

    mainClock = pygame.time.Clock()
    BGCOLOR = (100, 50, 50)
    while timer > 0:
        windowSurface.fill(BGCOLOR)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        Anim.blit(windowSurface, (10, 30))

        pygame.display.update()
        mainClock.tick(60)
        timer-=1
