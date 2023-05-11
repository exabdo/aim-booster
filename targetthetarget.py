from pyautogui import *
import time
import keyboard
import pyautogui
import random
import win32api, win32con
# import cv2
while 1:
    if pyautogui.locateOnScreen('target.png', confidence=0.8) != None:
        print("i can see it")
        time.sleep(1)
    else:
        print("i cant")
        time.sleep(1)
