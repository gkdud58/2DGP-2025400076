from pico2d import *

# 동작(행)별 메타데이터 초안: y = 시트 내 세로 시작좌표, frame_h = 프레임 높이
# (스프라이트 시트를 분석해 행 단위로 먼저 조사. 프레임별 x좌표는 다음 단계에서 채운다)
ACTIONS = [
    {"name": "walk", "y": 39, "frame_h": 39, "frames": []},
    {"name": "walk_fast", "y": 79, "frame_h": 39, "frames": []},
    {"name": "skid_stop", "y": 121, "frame_h": 43, "frames": []},
    {"name": "spin_up", "y": 167, "frame_h": 33, "frames": []},
    {"name": "roll", "y": 206, "frame_h": 27, "frames": []},
    {"name": "dash", "y": 238, "frame_h": 36, "frames": []},
    {"name": "dash_alt", "y": 283, "frame_h": 35, "frames": []},
    {"name": "look_around", "y": 326, "frame_h": 45, "frames": []},
    {"name": "run", "y": 377, "frame_h": 40, "frames": []},
    {"name": "idle_pose", "y": 426, "frame_h": 43, "frames": []},
]

open_canvas(1200, 800)

sprite_sheet = load_image('sonic-sprite.png')

clear_canvas()
sprite_sheet.draw(600, 400)
update_canvas()
delay(2)

close_canvas()
