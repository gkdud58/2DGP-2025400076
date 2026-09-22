from pico2d import *
import math
import os

WIDTH, HEIGHT = 800, 600
SPEED = 5          # 직선 이동 시 프레임당 이동 픽셀
FRAME_DELAY = 0.01

# 원운동
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 200

# 사각운동 (좌우/위아래 끝)
LEFT, RIGHT = 50, WIDTH - 50
BOTTOM, TOP = 50, HEIGHT - 50

# 삼각운동 (꼭짓점: 위, 오른쪽 아래, 왼쪽 아래)
TRIANGLE = [(WIDTH // 2, TOP), (RIGHT, BOTTOM), (LEFT, BOTTOM)]


def handle_events():
    # ESC 키 또는 창 닫기 버튼을 누르면 종료
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            close_canvas()
            exit()


def draw_character(x, y):
    handle_events()
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_line(x1, y1, x2, y2):
    # (x1, y1)에서 (x2, y2)까지 직선 이동
    steps = max(1, int(math.hypot(x2 - x1, y2 - y1) / SPEED))
    for i in range(steps):
        t = i / steps
        draw_character(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)


def move_polygon(points):
    # 꼭짓점을 차례로 이어 한 바퀴 이동
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        move_line(x1, y1, x2, y2)


def move_circle():
    # 원의 맨 아래(270도)에서 시작해 반시계 방향으로 한 바퀴
    for degree in range(270, 270 + 360, 2):
        theta = math.radians(degree)
        draw_character(CENTER_X + RADIUS * math.cos(theta),
                       CENTER_Y + RADIUS * math.sin(theta))


def move_rectangle():
    move_polygon([(LEFT, TOP), (RIGHT, TOP), (RIGHT, BOTTOM), (LEFT, BOTTOM)])


def move_triangle():
    move_polygon(TRIANGLE)


open_canvas(WIDTH, HEIGHT)
character = load_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'character.png'))

while True:
    move_circle()
    move_rectangle()
    move_triangle()
