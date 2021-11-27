import pygame as pg
import random
from Planet import Planet, SolarSystem

BLACK = pg.Color("BLACK")
WHITE = pg.Color("WHITE")

SCREEN_SIZE = (1800, 1300)


def main():
    properties = {'in_play': True,
                  'tick': 1}

    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    background = pg.Surface(screen.get_size())
    fps = pg.time.Clock()

    solar_system = SolarSystem(background)
    solar_system.step()

    try:
        while 1:
            check_input(properties)

            if properties['in_play']:
                solar_system.step()
            screen.blit(background, (0, 0))
            pg.display.update(background.get_rect())
            fps.tick(properties['tick'])

    finally:
        pg.quit()


def check_input(properties):
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                pg.quit()
            if event.key == pg.K_p:
                properties['in_play'] = not properties['in_play']

            if event.key == pg.K_UP:
                properties['tick'] = properties['tick'] + 10
            if event.key == pg.K_DOWN:
                properties['tick'] = properties['tick'] - 10


if __name__ == '__main__':
    main()
