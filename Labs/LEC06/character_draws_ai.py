from pico2d import *
import math
import os

WIDTH, HEIGHT = 800, 600
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
    steps = int(math.hypot(x2 - x1, y2 - y1) / 5)
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
    # 위쪽 변: 왼쪽 → 오른쪽
    for x in range(LEFT, RIGHT, 5):
        draw_character(x, TOP)
    # 오른쪽 변: 위 → 아래
    for y in range(TOP, BOTTOM, -5):
        draw_character(RIGHT, y)
    # 아래쪽 변: 오른쪽 → 왼쪽
    for x in range(RIGHT, LEFT, -5):
        draw_character(x, BOTTOM)
    # 왼쪽 변: 아래 → 위
    for y in range(BOTTOM, TOP, 5):
        draw_character(LEFT, y)


open_canvas(WIDTH, HEIGHT)
character = load_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'character.png'))

while True:
    move_circle()
    move_rectangle()
