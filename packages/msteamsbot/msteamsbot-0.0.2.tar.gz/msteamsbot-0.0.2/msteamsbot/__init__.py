from pyautogui import *
import pyautogui
import keyboard
import time
import os
import getpass

user = getpass.getuser()

def send(message, delay, x, y):
    if message == None:
       message = 'Hello, World' 
    if delay == None:
        delay = 2
    if x == None:
        x = 525
    if y == None:
        y = 665

    time.sleep(delay)
    pyautogui.click(x, y)
    pyautogui.typewrite(message)
    time.sleep(0.1)
    pyautogui.typewrite(['enter'])
    print('Sent')

def spam(message, delay, quit_button, x, y):
    if message == None:
       message = 'Hello, World' 
    if delay == None:
        delay = 0.5
    if quit_button == None:
        quit_button = 'q'
    if x == None:
        x = 525
    if y == None:
        y = 665

    time.sleep(2)
    while keyboard.is_pressed(quit_button) == False:
        time.sleep(delay)
        pyautogui.click(x, y)
        pyautogui.typewrite(message)
        time.sleep(0.1)
        pyautogui.typewrite(['enter'])
        print('Spammed')

def profile(delay, x, y):
    time.sleep(delay)
    pyautogui.click(x, y)
    print('Profile Opened')

def set_status(message, delay, x, y):
    time.sleep(delay)
    pyautogui.click(x, y)
    pyautogui.typewrite(message)
    time.sleep(0.1)
    pyautogui.typewrite(['enter'])
    print('Status Changed')

def get_status(delay, x, y, px, py):
    time.sleep(delay)
    profile(0.1, px, py)
    time.sleep(0.1)
    pyautogui.click(x, y)
    pyautogui.hotkey('ctrl' + 'a')
    status = pyautogui.hotkey('ctrl' + 'c')
    print('Status: \n' + status)

def close():
    os.system('taskkill /F /IM Teams.exe /T')
