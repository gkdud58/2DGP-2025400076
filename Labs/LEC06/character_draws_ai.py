from pico2d import *
import math
import os

WIDTH, HEIGHT = 800, 600
SPEED = 5
FRAME_DELAY = 0.01

CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 200

LEFT, RIGHT = 50, WIDTH - 50
BOTTOM, TOP = 50, HEIGHT - 50


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_line(x1, y1, x2, y2):
    steps = int(math.hypot(x2 - x1, y2 - y1) / SPEED)
    for i in range(steps):
        t = i / steps
        draw_character(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)


def move_circle():
    # 원의 맨 아래(270도)에서 시작해 반시계 방향으로 한 바퀴
    for degree in range(270, 270 + 360, 2):
        theta = math.radians(degree)
        draw_character(CENTER_X + RADIUS * math.cos(theta),
                       CENTER_Y + RADIUS * math.sin(theta))


def move_rectangle():
    move_line(LEFT, TOP, RIGHT, TOP)
    move_line(RIGHT, TOP, RIGHT, BOTTOM)
    move_line(RIGHT, BOTTOM, LEFT, BOTTOM)
    move_line(LEFT, BOTTOM, LEFT, TOP)


def move_triangle():
    move_line(WIDTH // 2, TOP, RIGHT, BOTTOM)
    move_line(RIGHT, BOTTOM, LEFT, BOTTOM)


open_canvas(WIDTH, HEIGHT)
character = load_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'character.png'))

while True:
    move_circle()
    move_rectangle()
    move_triangle()
