from pyautogui import *
import pyautogui
import pynput
import time
import keyboard
import random
import win32api
import win32con
#
iml = pyautogui.screenshot(region=(300,300,700,520))
iml.save(r"C:\Users\mnmn\Desktop\exsercise\python\aim_booster\target1.png")
# time.sleep(2)
# #
# #
# def click(x, y):
#     win32api.SetCursorPos((x, y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
