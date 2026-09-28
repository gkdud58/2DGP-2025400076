from pico2d import *
import os

WIDTH, HEIGHT = 800, 600

open_canvas(WIDTH, HEIGHT)
character = load_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'character.png'))

clear_canvas()
character.draw(WIDTH // 2, HEIGHT // 2)
update_canvas()
delay(1)

close_canvas()
