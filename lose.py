import sys
import pygame
import os


def get_image(path):
        _image_library = {}
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def partLose1():
    fps = pygame.time.Clock()
    timer = 150
    mode = ("one", "two")
    state = "..."
    bliter,bliter2 = False, True
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.music.load("win_lose/gameover.ogg")
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((524, 378))
    clock = pygame.time.Clock()
    screen.fill((255, 255, 255))
    screen.blit(get_image('win_lose/lose.jpg'),(0,0))
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption('You lose :(')

    while timer > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        fps.tick(30)
        timer -= 1