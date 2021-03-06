import pygame as pyg
from pygame.draw import *
import math


def main():
    """
    Main method that initializes pygame and draws scene
    """
    # set up
    pyg.init()

    screen_width, screen_height = 1032, 768

    screen = pyg.display.set_mode((screen_width, screen_height))
    screen.fill(COLOR['GREEN'])
    # scene drawing
    draw_scene(screen, screen_width, screen_height)

    # display and quit event handling
    pyg.display.update()
    finished = False

    while not finished:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                finished = True
    pyg.quit()


def draw_scene(screen, screen_width, screen_height):
    """
    Draws scene on screen with resolution screen_width*screen_height
    @param screen: screen to draw on
    @param screen_width: screen's width
    @param screen_height: screen's height
    """
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

    line(screen, COLOR['BLACK'], (screen_width // 2, 30 +
                                  screen_height // 2), (20 + screen_width // 2, screen_height // 4), 2)
    balloons(screen, 20 + screen_width // 2, screen_height // 4, 60, size=120)

    ice_cream(screen, 940, 500, 90, size=80)


def man(surface, x, y, width, height, draw_face=True):
    """
    Draws a man
    @param surface: surface to draw on
    @param x: x coordinate of the center of man's torso(without legs, arms and head)
    @param y: y coordinates of the center of man's torso(without legs, arms and head)
    @param width: torso width
    @param height: torso height
    @param draw_face: if man's face should be drawn
    """

    # torso
    torso_rect = (x, y, width, height)
    ellipse(surface, COLOR['PURPLE'], torso_rect)
    # head
    head_center = (x + width // 2, y - height // 6)
    head_height = height // 5
    circle(surface, COLOR['FACE_COLOR'], head_center, head_height)

    if draw_face:
        # eyes
        eyes_height = y - int(0.22 * height)
        circle(surface, COLOR['WHITE'], (x + width // 3, eyes_height), height // 20)
        circle(surface, COLOR['BLACK'],
               (x + int(0.32 * width), eyes_height), height // 45)
        circle(surface, COLOR['WHITE'],
               (x + int(0.65 * width), eyes_height), height // 20)
        circle(surface, COLOR['BLACK'],
               (x + int(0.66 * width), eyes_height), height // 45)
        # nose
        line(surface, COLOR['BLACK'],
             (x + width // 2, y - int(0.2 * height)),
             (x + width // 2, y - int(0.1 * height)), 1)
        # mouth
        arc(surface, COLOR['BLACK'],
            (x + int(0.35 * width), y - int(0.18 * height), int(0.3 * width), height // 6),
            1.1 * math.pi, 1.9 * math.pi, 2)
    # hands
    line(surface, COLOR['BLACK'],
         (x + width // 5, y + height // 10),
         (x - width // 2, y + int(0.65 * height)), 2)
    line(surface, COLOR['BLACK'],
         (x + int(.8 * width), y + height // 10),
         (x + int(1.6 * width), y + height // 2), 2)
    # legs
    leg1_top = (x + width // 3, y + int(0.95 * height))
    leg1_mid = (x + width // 20, y + int(1.5 * height))
    leg1_bot = (x - width // 4, y + int(1.5 * height) + 2)
    line(surface, COLOR['BLACK'],
         leg1_top,
         leg1_mid, 2)
    line(surface, COLOR['BLACK'],
         leg1_mid,
         leg1_bot, 2)

    leg2_top = (x + 2 * width // 3, y + int(0.95 * height))
    leg2_mid = (x + 3 * width // 4, y + int(1.49 * height))
    leg2_bot = (x + width, y + int(1.5 * height))
    line(surface, COLOR['BLACK'],
         leg2_top,
         leg2_mid, 2)
    line(surface, COLOR['BLACK'],
         leg2_mid,
         leg2_bot, 2)


def woman(surface, x, y, width, height, draw_face=True, draw_hair=True):
    """
    Draws woman.
    surface - surface to draw on
    x, y - coordinates of the highest point of a torso triangle aka end of a neck
    width, height - width and height of torso triangle
    @param surface: surface to draw on
    @param x: x coordinate of the highest point of a torso triangle aka end of a neck
    @param y: y coordinate of the highest point of a torso triangle aka end of a neck
    @param width: torso triangle width
    @param height: torso triangle height
    @param draw_face: if woman's face should be drawn
    @param draw_hair: if woman's hair should be drawn
    """
    if draw_hair:
        # hairs
        circle(surface, COLOR['BROWN'], (x, y - height // 8), height // 4)
        rect(surface, COLOR['BROWN'], (x - height // 4,
                                       y - height // 8, height // 2, height // 2))
    # torso
    polygon(surface, COLOR['PINK'],
            [(x, y), (x - width // 2, y + height), (x + width // 2, y + height)])
    # head
    circle(surface, COLOR['FACE_COLOR'], (x, y - height // 16), 2 * height // 11)

    if draw_face:
        # eyes
        eyes_y = y - int(0.1 * height)
        eyes_dx = int(0.1 * width)
        circle(surface, COLOR['WHITE'],
               (x - eyes_dx, eyes_y), height // 25)
        circle(surface, COLOR['BLACK'],
               (x - eyes_dx, eyes_y), height // 50)
        circle(surface, COLOR['WHITE'],
               (x + eyes_dx, eyes_y), height // 25)
        circle(surface, COLOR['BLACK'],
               (x + eyes_dx, eyes_y), height // 50)
        # nose
        line(surface, COLOR['BLACK'],
             (x, y - int(0.1 * height)),
             (x, y), 1)
        # mouth
        arc(surface, COLOR['BLACK'],
            (x - int(0.1 * width), y - int(0.08 * height), int(0.2 * width), height // 6),
            1.1 * math.pi, 1.9 * math.pi, 2)
    # hands
    line(surface, COLOR['BLACK'],
         (x - width // 12, y + height // 6),
         (x - int(0.8 * width), y + int(0.55 * height)), 2)
    line(surface, COLOR['BLACK'],
         (x + width // 12, y + height // 6),
         (x + int(0.4 * width), y + int(0.4 * height)), 2)
    line(surface, COLOR['BLACK'],
         (x + int(0.4 * width), y + int(0.4 * height)),
         (x + int(0.6 * width), y + height // 4), 2)
    # legs
    #  leg 1
    leg1_mid = (x - width // 10, y + int(1.45 * height))
    line(surface, COLOR['BLACK'],
         (x - width // 10, y + height),
         leg1_mid, 2)
    line(surface, COLOR['BLACK'],
         leg1_mid,
         (x - int(0.3 * width), y + int(1.45 * height)), 2)
    #  leg 2
    leg2_mid = (x + width // 10, y + int(1.45 * height))
    line(surface, COLOR['BLACK'],
         (x + width // 10, y + height),
         leg2_mid, 2)
    line(surface, COLOR['BLACK'],
         leg2_mid,
         (x + int(0.3 * width), y + int(1.45 * height) + 3), 2)


def balloons(surface, x, y, angle, size=80):
    """
    Draws heart-shaped balloon
    @param surface: surface to draw on
    @param x: x coordinate of bottom center point
    @param y: y coordinate of bottom center point
    @param angle: rotation angle in degrees
    @param size: triangle side size
    """
    # triangle represents bottom of the heart
    triangle_left_x = int(x - size * math.cos(math.radians(angle)))
    triangle_left_y = int(y - size * math.sin(math.radians(angle)))
    triangle_right_x = int(x + size * math.cos(math.radians(180 - angle - 60)))
    triangle_right_y = int(y - size * math.sin(math.radians(180 - angle - 60)))
    polygon(surface, COLOR['RED'],
            [(x, y), (triangle_left_x, triangle_left_y), (triangle_right_x, triangle_right_y)])
    circle(surface, COLOR['RED'], (int(0.25 * triangle_left_x + 0.75 * triangle_right_x),
                                   int(0.25 * triangle_left_y + 0.75 * triangle_right_y)), size // 4)
    circle(surface, COLOR['RED'], (int(0.75 * triangle_left_x + 0.25 * triangle_right_x),
                                   int(0.75 * triangle_left_y + 0.25 * triangle_right_y)), size // 4)


def ice_cream(surface: pyg.Surface, x, y, angle, size):
    """
    Draws ice-cream
    @param surface: surface to draw on
    @param x: x coordinate of bottom center point
    @param y: y coordinate of bottom center point
    @param angle: rotation angle in degrees
    @param size: size of side of the cone
    """
    # triangle represents a cone
    triangle_left_x = int(x - size * math.cos(math.radians(angle)))
    triangle_left_y = int(y - size * math.sin(math.radians(angle)))
    triangle_right_x = int(x + size * math.cos(math.radians(180 - angle - 60)))
    triangle_right_y = int(y - size * math.sin(math.radians(180 - angle - 60)))
    polygon(surface, COLOR['YELLOW'],
            [(x, y), (triangle_left_x, triangle_left_y), (triangle_right_x, triangle_right_y)])
    circle(surface, COLOR['BROWN'], (int(0.25 * triangle_left_x + 0.75 * triangle_right_x),
                                     int(0.25 * triangle_left_y + 0.75 * triangle_right_y)), size // 4)
    circle(surface, COLOR['RED'], (int(0.75 * triangle_left_x + 0.25 * triangle_right_x),
                                   int(0.75 * triangle_left_y + 0.25 * triangle_right_y)), size // 4)
    x_white = (triangle_left_x + triangle_right_x) / 2 - size // 4 * math.cos(math.radians(30 + angle))
    y_white = (triangle_left_y + triangle_right_y) / 2 - size // 4 * math.sin(math.radians(30 + angle))
    circle(surface, COLOR['WHITE'], (int(x_white), int(y_white)), size // 4)


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
