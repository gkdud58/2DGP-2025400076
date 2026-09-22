# 실습 과제 진행
from pico2d import *
import math

def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        boy.draw(x, y)
        update_canvas()
        delay(0.01)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_triangle():
    three_point(400, 550, 50, 50, 750, 50)






# ******사각형관련함수******
def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01) # 0에 가까워질수록 빠르게 움직임


def move_top():
    for x in range(50, 751, 5):
        draw_boy(x, 550)
def move_right():
    for y in range(550, 50, -5):
        draw_boy(750, y)
def move_bottom():
    for x in range(750, 49, -5):
        draw_boy(x, 50)
def move_left():
    for y in range(50, 551, 5):
        draw_boy(50, y)


## ******삼각형관련함수******
def three_point(x1, y1, x2, y2, x3, y3):
    clear_canvas()
    boy.draw(x1, y1)
    boy.draw(x2, y2)
    boy.draw(x3, y3)
    update_canvas()
    delay(0.01)



open_canvas(800, 600)
boy = load_image('character.png')

while True:
    #move_circle()
    #move_rectangle()
    move_triangle()

close_canvas()