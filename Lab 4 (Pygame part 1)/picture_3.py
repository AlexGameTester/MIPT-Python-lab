from picture_3_2 import man, woman, ice_cream, balloons, COLOR
from pygame.draw import *
import pygame as pyg
import math


def main():
    pyg.init()

    width, height = 1032, 768
    screen = pyg.display.set_mode((width, height))
    screen.fill(COLOR['GREEN'])
    # sky
    rect(screen, COLOR['BLUE'], (0, 0, width, height // 2))

    man(screen, 260, 250, 150, 300, draw_face=False)

    # ice cream
    angle = 0
    size = 110
    ice_cream(screen, 200, 450, angle, size)

    woman(screen, 690, 220, 240, 330, draw_face=False, draw_hair=False)

    # balloons
    line(screen, COLOR['BLACK'], (830, 315), (885, 170), 2)
    angle = math.degrees(math.pi / 2 - 0.527)
    size = 110
    balloons(screen, 885, 170, angle, size)

    # display and quit event handling
    pyg.display.update()
    finished = False
    while not finished:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                finished = True
    pyg.quit()


if __name__ == '__main__':
    main()

