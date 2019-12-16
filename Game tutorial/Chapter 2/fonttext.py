import pygame, sys
from pygame.locals import *
import time

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello world!')

WHITE = (255,255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0,128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurficeObj = fontObj.render('Hello world!', True, GREEN, BLUE)
textRectObj = textSurficeObj.get_rect()
textRectObj.center = (200, 150)

pygame.mixer.music.load('example.wav')
pygame.mixer.music.play(-1, 0.0)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurficeObj, textRectObj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()