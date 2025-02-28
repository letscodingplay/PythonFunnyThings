import random
import sys
import time

def generate_fake_hacking():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    
    print("해킹 시뮬레이션 시작... (Ctrl + C로 종료)")
    try:
        while True:
            selected_li = random.choices(chars, k=random.randint(50, 100))
            random_text = "".join(selected_li)
            sys.stdout.write(random_text + "\n")
            sys.stdout.flush()
            time.sleep(0.05)  # 출력 속도 조절
    except KeyboardInterrupt:
        print("\n해킹 완료! 시스템 접근 성공! (물론 가짜입니다 😆)")

# 실행
generate_fake_hacking()