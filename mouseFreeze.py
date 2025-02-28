import pyautogui
import time

# 고정할 위치 (예: 화면 중앙)
screen_width, screen_height = pyautogui.size()
fixed_x, fixed_y = screen_width // 2, screen_height // 2

print("마우스가 계속 제자리로 돌아오고 있어요! 종료하려면 Ctrl + C 를 누르세요.")

try:
    while True:
        pyautogui.moveTo(    ,   , duration=0)
        time.sleep(    )  # CPU 점유율을 낮추기 위한 짧은 대기 시간
except KeyboardInterrupt:
    print("마우스가 풀렸습니다!")