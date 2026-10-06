from pico2d import *

open_canvas(1200, 800)

sprite_sheet = load_image('sonic-sprite.png')

clear_canvas()
sprite_sheet.draw(600, 400)
update_canvas()
delay(2)

close_canvas()
