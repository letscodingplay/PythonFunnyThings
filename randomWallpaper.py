import os
import random
import ctypes  # Windows 배경화면 변경을 위한 라이브러리
from pathlib import Path
import time

def change_wallpaper(folder_path):
    # 폴더 내의 모든 이미지 파일 가져오기
    image_files = [f for f in Path(folder_path).iterdir() ]
    
    if not image_files:
        print("이미지 파일을 찾을 수 없습니다!")
        return
    
    # 랜덤으로 하나 선택
    selected_image = random.choice(image_files)
    print(f"설정된 배경화면: {selected_image}")
    
    # Windows 배경화면 변경
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(          ), 3)

# 실행 예제
wallpaper_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")

try:
    while True:
        change_wallpaper(wallpaper_folder)
        time.sleep(3)  # 10초마다 변경    
except KeyboardInterrupt:
    print("배경화면 변경 종료!")

