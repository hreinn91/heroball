#!/usr/bin/python

import pygame
from pygame.locals import KEYDOWN

if __name__ == '__main__':

    width = 500
    height = 500
    size = [width, height]
    ydir = 1
    xdir = 1
    xpos = 0
    ypos = 0
    pygame.init()
    screen = pygame.display.set_mode(size)
    background = pygame.Surface(screen.get_size())

    b = pygame.sprite.Sprite()  # create sprite
    b.image = pygame.image.load("planet.png").convert()  # load image
    b.image = pygame.transform.scale(b.image, (50, 50)).convert()

    b.rect = b.image.get_rect()  # use image extent values
    b.rect.topleft = [xpos, ypos]  # put the ball in the top left corner
    screen.blit(b.image, b.rect)
    slow = 0


    def gravity(y):
        global height
        return 0


    pygame.display.update()
    while pygame.event.poll().type != KEYDOWN:
        pygame.time.delay(gravity(ypos))
        # If we're at the top or bottom of the screen,
        # switch directions.

        if b.rect.bottom >= height:
            ydir = -1
        elif ypos == 0:
            ydir = 1
        if xpos == 0:
            xdir = 1
        elif b.rect.right >= width:
            xdir = -1

        if slow:
            screen.fill([0, 0, 0])  # blank the screen
        else:
            rectlist = [screen.blit(background, b.rect)]

        # Move our position up or down by one pixel
        xpos += xdir
        ypos += ydir
        b.rect.topleft = [xpos, ypos]

        if slow:
            screen.blit(b.image, b.rect)
            pygame.display.update()
        else:
            rectlist += [screen.blit(b.image, b.rect)]
            pygame.display.update(rectlist)
