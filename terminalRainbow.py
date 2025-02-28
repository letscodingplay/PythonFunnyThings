from time import sleep
from colorama import Fore, Style, init
import itertools

# colorama 초기화 (Windows에서도 색상이 제대로 출력되도록 설정)
init()

# 사용할 색상 리스트
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
name = "LETSCODING & PLAY"  # 여기에 원하는 이름 입력

print("내 이름을 무지개처럼 빛나게! (Ctrl + C로 종료)")

try:
    for color in itertools.cycle(     ):  # 색상을 반복해서 순환
        print(color + name + Style.RESET_ALL, end="\r", flush=True)
        sleep(0.3)  # 0.3초마다 색상 변경
except KeyboardInterrupt:
    print("\n무지개 출력 종료!")
