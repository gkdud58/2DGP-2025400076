# 실습 과제 진행
from pico2d import *
import math

CENTER_X, CENTER_Y = 400, 300  # 원운동 중심
RADIUS = 200                   # 원운동 반지름
LEFT, RIGHT = 50, 750          # 네모/세모 좌우 끝
BOTTOM, TOP = 50, 550          # 네모/세모 위아래 끝

def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = CENTER_X + RADIUS * math.cos(theta)
        y = CENTER_Y + RADIUS * math.sin(theta)
        draw_boy(x, y)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_triangle():
    move_tri_left()
    move_tri_bottom()
    move_tri_right()



# ******사각형관련함수******
def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01) # 0에 가까워질수록 빠르게 움직임


def move_top():
    move_line(LEFT, TOP, RIGHT, TOP)
def move_right():
    move_line(RIGHT, TOP, RIGHT, BOTTOM)
def move_bottom():
    move_line(RIGHT, BOTTOM, LEFT, BOTTOM)
def move_left():
    move_line(LEFT, BOTTOM, LEFT, TOP)


## ******삼각형관련함수******
def move_line(x1, y1, x2, y2, speed=5):
    # 점 (x1, y1)에서 점 (x2, y2)까지 직선으로 이동 (speed: 프레임당 이동 픽셀)
    distance = math.hypot(x2 - x1, y2 - y1)
    steps = max(1, int(distance / speed))
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_boy(x, y)

def move_tri_left():
    move_line(CENTER_X, TOP, LEFT, BOTTOM)
def move_tri_bottom():
    move_line(LEFT, BOTTOM, RIGHT, BOTTOM)
def move_tri_right():
    move_line(RIGHT, BOTTOM, CENTER_X, TOP)




open_canvas(800, 600)
boy = load_image('character.png')

while True:
    move_circle()
    move_line(CENTER_X + RADIUS, CENTER_Y, LEFT, TOP, speed=20)  # 원 끝점 → 네모 시작점 (빠르게)
    move_rectangle()
    move_line(LEFT, TOP, CENTER_X, TOP, speed=20)  # 네모 끝점 → 세모 시작점 (빠르게)
    move_triangle()

close_canvas()