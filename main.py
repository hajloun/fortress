import pyautogui
import time

time.sleep(4)

while True:
    pyautogui.press('enter')
    time.sleep(0.5)
    try:
        zero = pyautogui.locateOnScreen('zero.png',confidence=0.9)
        if zero is not None:
            print("Image found")
            pyautogui.press('enter')
            recruit_button = pyautogui.locateOnScreen('rec.png',confidence=0.8)
            recruit_button = pyautogui.center(recruit_button)
            pyautogui.moveTo(recruit_button)
            pyautogui.click()

            add_soldiers = pyautogui.locateOnScreen('add_soldiers.png',confidence=0.8)
            add_soldiers = pyautogui.center(add_soldiers)
            pyautogui.moveTo(add_soldiers)
            pyautogui.click()
            break

    except pyautogui.ImageNotFoundException:
        print("Image not found")
        pyautogui.press('right')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(0.3)
        pyautogui.press('enter')
        time.sleep(1)
        continue
