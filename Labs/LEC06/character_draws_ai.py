from pico2d import *
import math
import os

WIDTH, HEIGHT = 800, 600
FRAME_DELAY = 0.01

CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 200


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_circle():
    for degree in range(0, 360, 2):
        theta = math.radians(degree)
        draw_character(CENTER_X + RADIUS * math.cos(theta),
                       CENTER_Y + RADIUS * math.sin(theta))


open_canvas(WIDTH, HEIGHT)
character = load_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'character.png'))

move_circle()

close_canvas()
