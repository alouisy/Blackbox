import pygame
from pygame.locals import *
import sys
import pyganim
import os

def partWin1():
    timer = 250
    windowSurface = pygame.display.set_mode((730, 780))
    pygame.display.set_caption('You win :)')
    Anim = pyganim.PygAnimation([('win_lose/0.png', 0.06),
                                     ('win_lose/1.png', 0.06),
                                     ('win_lose/3.png', 0.06),
                                     ('win_lose/4.png', 0.06),
                                     ('win_lose/5.png', 0.06),
                                     ('win_lose/6.png', 0.06),
                                     ('win_lose/7.png', 0.06),
                                     ('win_lose/8.png', 0.06),
                                     ('win_lose/9.png', 0.06),
                                     ('win_lose/10.png', 0.06),
                                     ('win_lose/11.png', 0.06),
                                     ('win_lose/12.png', 0.06),
                                     ('win_lose/13.png', 0.06),
                                     ('win_lose/14.png', 0.06)])
    Anim.play()

    mainClock = pygame.time.Clock()
    BGCOLOR = (0, 0, 0)
    while timer > 0:
        windowSurface.fill(BGCOLOR)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        Anim.blit(windowSurface, (10, 30))

        pygame.display.update()
        mainClock.tick(60)
        timer -= 1
