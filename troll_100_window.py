import cv2
import pyautogui
import numpy as np
# Kích thước màn hình
screen_width, screen_height = pyautogui.size()

# Kéo màn hình xuống
def scroll_down():
    pyautogui.scroll(-100)  # Số âm để kéo xuống

while True:
# Chụp màn hình
    img = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
# Hiển thị màn hình
    cv2.imshow("Screen", frame)

# Bắt phím nhấn
    key = cv2.waitKey(1)
    
# Khi nhấn phím 'q', thoát khỏi vòng lặp
    if key == ord('q'):
        break

# Đóng cửa sổ
cv2.destroyAllWindows()