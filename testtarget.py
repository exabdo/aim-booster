from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
#
# while 1:
#     if pyautogui.locateOnScreen('target.png',region=(0,0,200,200), grayscale=True, confidence=0.6) != None:
#         print("i can see it")
#         time.sleep(1)
#     else:
#         print("i cant")
#         time.sleep(1)
time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(300,300,700,520))
    while 1:
        if pyautogui.locateOnScreen('target.png', confidence=0.8) != None:
            x=pyautogui.locateOnScreen('target.png', confidence=0.8)
            click(x)
            print(x)
            time.sleep(1)

    # width, height = pic.size
    #
    # for x in range(0,width,5):
    #     for y in range(0,height,5):
    #
    #         r,g,b = pic.getpixel((x,y))
    #
    #         if b == 195:
    #             # time.sleep(.2)
    #             click(x+300,y+300)
    #             time.sleep(0.2)
    #             break