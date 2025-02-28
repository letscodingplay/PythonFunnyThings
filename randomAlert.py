import tkinter as tk
import random

def create_error_popup():
    # 팝업 창 생성
    popup = tk.Toplevel()
    popup.title("⚠️ Critical Error")
    popup.configure(bg='black')
    
    # 레이블 설정
    label = tk.Label(
        popup, 
        text="SYSTEM FAILURE DETECTED", 
        fg='red', 
        bg='black',
        font=('Arial', 14, 'bold')
    )
    label.pack(padx=50, pady=20)
    
    # 화면 내 무작위 위치 설정
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = random.randint(0, screen_width - 300)
    y = random.randint(0, screen_height - 100)
    popup.geometry(f"+{x}+{y}")
    
    # 1.5초 후 자동 종료
    popup.after(    , popup.destroy)
    # 2초 후 새 팝업 생성
    root.after(    , create_error_popup)

# 메인 창 숨기기
root = tk.Tk()
root.withdraw()

# 초기 팝업 실행
create_error_popup()
root.mainloop()