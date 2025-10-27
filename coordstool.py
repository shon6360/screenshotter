import time
import pyautogui
while True:
    x, y = pyautogui.position()
    print(f"Mouse: ({x}, {y})", end="\r")
    time.sleep(0.05)
