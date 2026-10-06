from pico2d import *

# 동작(행)별 메타데이터: y = 시트 내 세로 시작좌표, frame_h = 프레임 높이,
# frames = 프레임별 (x, width) 목록 (스프라이트 시트를 분석해 수동으로 조사한 좌표)
ACTIONS = [
    {
        "name": "walk",
        "y": 39,
        "frame_h": 39,
        "moves": True,
        "frames": [(1, 29), (31, 26), (58, 28), (86, 30), (118, 30), (150, 30),
                   (182, 29), (211, 29), (240, 30), (270, 24), (302, 29)],
    },
    {
        "name": "walk_fast",
        "y": 79,
        "frame_h": 39,
        "moves": True,
        "frames": [(8, 26), (37, 27), (65, 31), (97, 37), (135, 32), (170, 32),
                   (206, 26), (238, 24), (263, 30), (295, 36), (334, 32), (370, 29)],
    },
    {
        "name": "skid_stop",
        "y": 121,
        "frame_h": 43,
        "moves": False,
        "frames": [(1, 33), (39, 35), (89, 35), (130, 34), (181, 34), (228, 33)],
    },
    {
        "name": "spin_up",
        "y": 167,
        "frame_h": 33,
        "moves": False,
        "frames": [(1, 29), (35, 29), (67, 30), (98, 31), (131, 29), (162, 29),
                   (193, 30), (230, 31), (268, 30)],
    },
    {
        "name": "roll",
        "y": 206,
        "frame_h": 27,
        "moves": True,
        "frames": [(1, 30), (36, 29), (70, 29), (105, 29), (139, 29), (174, 29)],
    },
    {
        "name": "dash",
        "y": 238,
        "frame_h": 36,
        "moves": True,
        "frames": [(1, 29), (36, 30), (74, 31), (111, 31), (149, 30), (186, 31)],
    },
    {
        "name": "dash_alt",
        "y": 283,
        "frame_h": 35,
        "moves": True,
        "frames": [(1, 29), (36, 30), (72, 39), (123, 39), (172, 39), (218, 38)],
    },
    {
        "name": "look_around",
        "y": 326,
        "frame_h": 45,
        "moves": False,
        "frames": [(1, 24), (31, 29), (65, 20), (90, 25), (119, 25), (149, 20),
                   (184, 40), (232, 39)],
    },
    {
        "name": "run",
        "y": 377,
        "frame_h": 40,
        "moves": True,
        "frames": [(1, 27), (31, 31), (64, 31), (99, 33), (136, 32), (176, 33),
                   (217, 33), (254, 33)],
    },
    {
        "name": "idle_pose",
        "y": 426,
        "frame_h": 43,
        "moves": False,
        "frames": [(6, 34), (49, 34), (96, 23), (125, 23)],
    },
]

CANVAS_W, CANVAS_H = 1200, 800
CENTER_X, CENTER_Y = CANVAS_W // 2, CANVAS_H // 2  # 캐릭터를 그릴 캔버스 중앙 좌표

open_canvas(CANVAS_W, CANVAS_H)

sprite_sheet = load_image('sonic-sprite.png')

# clip_draw는 bottom(아래쪽 기준) 좌표를 쓰므로, 위에서부터 잰 y(ACTIONS["y"])를
# 이미지 전체 높이 기준 bottom 좌표로 변환한다.
def to_bottom(action):
    return sprite_sheet.h - action["y"] - action["frame_h"]

ZOOM = 6  # 화면 대비 캐릭터가 잘 보이도록 확대할 배율
FRAME_DELAY = 0.1  # 프레임 전환 간격(초)
REPEAT_COUNT = 5  # 동작별 반복 재생 횟수
MOVE_LEFT_X = 150  # 이동하는 동작의 시작 x좌표
MOVE_RIGHT_X = CANVAS_W - 150  # 이동하는 동작의 끝 x좌표


def play_action(action):
    """동작 하나의 프레임 시퀀스를 REPEAT_COUNT번 반복 재생한다.
    moves가 True인 동작(걷기/달리기류)은 한 바퀴 재생될 때마다
    화면 왼쪽에서 오른쪽으로 수평 이동하는 것처럼 보이게 그린다."""
    bottom = to_bottom(action)
    frame_h = action["frame_h"]
    frame_count = len(action["frames"])

    for _ in range(REPEAT_COUNT):
        for i, (frame_x, frame_w) in enumerate(action["frames"]):
            if action["moves"] and frame_count > 1:
                progress = i / (frame_count - 1)
                draw_x = MOVE_LEFT_X + (MOVE_RIGHT_X - MOVE_LEFT_X) * progress
            else:
                draw_x = CENTER_X

            clear_canvas()
            sprite_sheet.clip_draw(frame_x, bottom, frame_w, frame_h,
                                    draw_x, CENTER_Y, frame_w * ZOOM, frame_h * ZOOM)
            update_canvas()
            delay(FRAME_DELAY)

    delay(1)  # 동작 하나의 반복 재생이 끝나면 1초 정지


# 모든 동작을 순서대로 한 바퀴 재생 (F1)
for action in ACTIONS:
    play_action(action)

close_canvas()
