# 실습 과제 진행
from pico2d import *
import math

CENTER_X, CENTER_Y = 400, 300  # 원운동 중심
RADIUS = 200                   # 원운동 반지름

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
    move_line(50, 550, 750, 550)
def move_right():
    move_line(750, 550, 750, 50)
def move_bottom():
    move_line(750, 50, 50, 50)
def move_left():
    move_line(50, 50, 50, 550)


## ******삼각형관련함수******
def move_line(x1, y1, x2, y2):
    # 점 (x1, y1)에서 점 (x2, y2)까지 직선으로 이동
    steps = 100
    for i in range(steps + 1):
        t = i / steps
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        draw_boy(x, y)

def move_tri_left():  
    move_line(400, 550, 50, 50)
def move_tri_bottom():
    move_line(50, 50, 750, 50)
def move_tri_right():
    move_line(750, 50, 400, 550)




open_canvas(800, 600)
boy = load_image('character.png')

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()