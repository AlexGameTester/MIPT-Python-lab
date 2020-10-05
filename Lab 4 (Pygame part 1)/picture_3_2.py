import pygame as pyg
from pygame.draw import *
import math


def main():
    pyg.init()
    FPS = 60

    screen_width, screen_height = 1032, 768

    screen = pyg.display.set_mode((screen_width, screen_height))
    screen.fill(COLOR['GREEN'])

    draw_scene(screen, screen_width, screen_height)

    # display and quit event handling
    pyg.display.update()
    clock = pyg.time.Clock()
    finished = False

    while not finished:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                finished = True
    pyg.quit()


def draw_scene(screen, screen_width, screen_height):
    '''
    Draws scene on screen with resolution screen_width*screen_height
    screen - screen to draw
    screen_width - it's width
    screen_height - it's height
    '''
    # sky
    rect(screen, COLOR['BLUE'], (0, 0, screen_width, screen_height // 2))

    # right couple
    man(screen, 130, 380, 100, 170)
    woman(screen, 420, 360, 160, 200)
    new = pyg.transform.flip(screen, True, False)
    screen.blit(new, (0, 0))
    # left couple
    man(screen, 130, 380, 100, 170)
    woman(screen, 420, 360, 160, 200)

    line(screen, COLOR['BLACK'], (80, 510), (65, 300), 2)
    balloons(screen, 65, 300, 50)

    line(screen, COLOR['BLACK'], (screen_width//2, 30 +
                                  screen_height//2), (20+screen_width//2, screen_height//4), 2)
    balloons(screen, 20+screen_width//2, screen_height//4, 60, size=120)

    ice_cream(screen, 940, 500, 90, size=80)


def man(surface, x, y, width, height):
    '''
    Draws a man
    x, y - coordinates of the center of man's torso(without legs, arms and head)
    width, height - width and height of man's torso
    '''

    # torso
    torso_rect = (x, y, width, height)
    ellipse(surface, COLOR['PURPLE'], torso_rect)

    # face
    face_center = (x + width//2, y - height//6)
    face_height = height // 5
    circle(surface, COLOR['FACE_COLOR'], face_center, face_height)
    # eyes
    eyes_height = y - int(0.22*height)
    circle(surface, COLOR['WHITE'], (x+width//3, eyes_height), height//20)
    circle(surface, COLOR['BLACK'],
           (x + int(0.32*width), eyes_height), height//45)
    circle(surface, COLOR['WHITE'],
           (x + int(0.65*width), eyes_height), height//20)
    circle(surface, COLOR['BLACK'],
           (x + int(0.66*width), eyes_height), height//45)
    # nose
    line(surface, COLOR['BLACK'],
         (x + width//2, y - int(0.2*height)),
         (x + width//2, y - int(0.1*height)), 1)
    # mouth
    arc(surface, COLOR['BLACK'],
        (x + int(0.35*width), y - int(0.18*height), int(0.3*width), height//6),
        1.1 * math.pi, 1.9 * math.pi, 2)
    # hands
    line(surface, COLOR['BLACK'],
         (x + width//5, y + height//10),
         (x - width//2, y + int(0.65*height)), 2)
    line(surface, COLOR['BLACK'],
         (x + int(.8*width), y + height//10),
         (x + int(1.6*width), y + height//2), 2)
    # legs
    leg1_hip = (x + width//3, y + int(0.95*height))
    leg1_heel = (x + width//20, y + int(1.5*height))
    leg1_toe = (x - width//4, y + int(1.5*height) + 2)
    line(surface, COLOR['BLACK'],
         leg1_hip,
         leg1_heel, 2)
    line(surface, COLOR['BLACK'],
         leg1_heel,
         leg1_toe, 2)

    leg2_hip = (x + 2*width//3, y + int(0.95*height))
    leg2_heel = (x + 3*width//4, y + int(1.49*height))
    leg2_toe = (x + width, y + int(1.5*height))
    line(surface, COLOR['BLACK'],
         leg2_hip,
         leg2_heel, 2)
    line(surface, COLOR['BLACK'],
         leg2_heel,
         leg2_toe, 2)


def woman(plot, x, y, width, height):
    # hairs
    circle(plot, COLOR['BROWN'], (x, y-height//8), height//4)
    rect(plot, COLOR['BROWN'], (x-height//4,
                                y-height//8, height//2, height//2))
    polygon(plot, COLOR['PINK'],
            [(x, y), (x-width//2, y+height), (x+width//2, y+height)])
    circle(plot, COLOR['FACE_COLOR'], (x, y-height//16), 2*height//11)
    # eyes
    circle(plot, COLOR['WHITE'],
           (x-int(0.1*width), y-int(0.1*height)), height//25)
    circle(plot, COLOR['BLACK'],
           (x-int(0.1*width), y-int(0.1*height)), height//50)
    circle(plot, COLOR['WHITE'],
           (x+int(0.1*width), y-int(0.1*height)), height//25)
    circle(plot, COLOR['BLACK'],
           (x+int(0.1*width), y-int(0.1*height)), height//50)
    # nose
    line(plot, COLOR['BLACK'],
         (x, y - int(0.1*height)),
         (x, y), 1)
    # mouth
    arc(plot, COLOR['BLACK'],
        (x-int(0.1*width), y-int(0.08*height), int(0.2*width), height//6),
        1.1 * math.pi, 1.9 * math.pi, 2)
    # hands
    line(plot, COLOR['BLACK'],
         (x - width//12, y + height//6),
         (x - int(0.8*width), y + int(0.55*height)), 2)
    line(plot, COLOR['BLACK'],
         (x + width//12, y + height//6),
         (x + int(0.4*width), y + int(0.4*height)), 2)
    line(plot, COLOR['BLACK'],
         (x + int(0.4*width), y + int(0.4*height)),
         (x + int(0.6*width), y + height//4), 2)
    # legs
    line(plot, COLOR['BLACK'],
         (x - width//10, y + height),
         (x - width//10, y + int(1.45*height)), 2)
    line(plot, COLOR['BLACK'],
         (x - width//10, y + int(1.45*height)),
         (x - int(0.3*width), y + int(1.45*height)), 2)
    line(plot, COLOR['BLACK'],
         (x + width//10, y + height),
         (x + width//10, y + int(1.45*height)), 2)
    line(plot, COLOR['BLACK'],
         (x + width//10, y + int(1.45*height)),
         (x + int(0.3*width), y + int(1.45*height) + 3), 2)


def balloons(plot, x, y, angle, size=80):
    x2 = int(x - size * math.cos(math.radians(angle)))
    y2 = int(y - size * math.sin(math.radians(angle)))
    x3 = int(x + size * math.cos(math.radians(180 - angle - 60)))
    y3 = int(y - size * math.sin(math.radians(180 - angle - 60)))
    polygon(plot, COLOR['RED'],
            [(x, y), (x2, y2), (x3, y3)])
    circle(plot, COLOR['RED'], (int(0.25*x2 + 0.75*x3),
                                int(0.25*y2 + 0.75*y3)), size//4)
    circle(plot, COLOR['RED'], (int(0.75*x2 + 0.25*x3),
                                int(0.75*y2 + 0.25*y3)), size//4)


def ice_cream(plot, x, y, angle, size):
    x2 = int(x - size * math.cos(math.radians(angle)))
    y2 = int(y - size * math.sin(math.radians(angle)))
    x3 = int(x + size * math.cos(math.radians(180 - angle - 60)))
    y3 = int(y - size * math.sin(math.radians(180 - angle - 60)))
    polygon(plot, COLOR['YELLOW'],
            [(x, y), (x2, y2), (x3, y3)])
    circle(plot, COLOR['BROWN'], (int(0.25 * x2 + 0.75 * x3),
                                  int(0.25 * y2 + 0.75 * y3)), size//4)
    circle(plot, COLOR['RED'], (int(0.75 * x2 + 0.25 * x3),
                                int(0.75 * y2 + 0.25 * y3)), size//4)
    x_white = (x2 + x3)/2 - size//4 * math.cos(math.radians(30+angle))
    y_white = (y2 + y3)/2 - size//4 * math.sin(math.radians(30+angle))
    circle(plot, COLOR['WHITE'], (int(x_white), int(y_white)), size//4)


COLOR = {
    'GREEN': (55, 200, 113),
    'BLUE': (170, 238, 255),
    'FACE_COLOR': (244, 227, 215),
    'PINK': (255, 85, 221),
    'PURPLE': (167, 147, 172),
    'RED': (255, 0, 0),
    'WHITE': (255, 255, 255),
    'BROWN': (85, 0, 0),
    'YELLOW': (255, 204, 0),
    'BLACK': (0, 0, 0),
}

if __name__ == "__main__":
    main()
