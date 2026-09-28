from pico2d import *
import os

WIDTH, HEIGHT = 800, 600


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


open_canvas(WIDTH, HEIGHT)
character = load_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'character.png'))

draw_character(WIDTH // 2, HEIGHT // 2)
delay(1)

close_canvas()
