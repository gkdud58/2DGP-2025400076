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
    print('rectangle')


def move_triangle():
    print('triangle')

open_canvas(800, 600)
boy = load_image('character.png')


while True:
    move_circle()
    # move_rectangle()
    # move_triangle()

close_canvas()