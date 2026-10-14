from ast import Global

from pico2d import *
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self): # 멤버함수는 항상 첫번째 인자가 self여야 함
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self) :
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Zombie:
    def __init__(self) :
        self.x, self.y = 100,170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')
 
    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height, 
                             self.x, self.y, frame_width//2, frame_height//2)


def reset_world():
    global running
    global grass
    global team
    global world

    #world
    world = []

    # 땅객체
    grass = Grass()
    world.append(grass)
    # 좀비를 생성, world리스트에 추가
    zombie = Zombie()
    world.append(zombie)

    # 팀을 생성, wolrd리스트에 추가
    running = True
    team = [Boy() for i in range(10)]
    world += team

def update_world():
    grass.update()
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for o in world:
        o.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas()


reset_world()





while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


close_canvas()
