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
    print('triangle')







def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)





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




open_canvas(800, 600)
boy = load_image('character.png')


while True:
    #move_circle()
    move_rectangle()
    #move_triangle()

close_canvas()