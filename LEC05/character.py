from pico2d import *
import math
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas()

character = load_image('character.png')

center_x = 400
center_y = 300

radius = 150
angle = 0

running = True

while running:
    clear_canvas()

    x = center_x + math.cos(angle) * radius
    y = center_y + math.sin(angle) * radius

    character.draw(x, y)

    angle += 0.03

    update_canvas()
    delay(0.01)

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

close_canvas()