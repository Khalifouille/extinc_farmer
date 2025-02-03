import pyautogui
import time

def prendre_arme():
    pyautogui.press('1')
    time.sleep(1)

def ranger_arme():
    pyautogui.press('1')
    time.sleep(0.5)
    pyautogui.press('1')
    time.sleep(1)

def viser_et_lancer_molotov():
    pyautogui.mouseDown(button='right')
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(0.5)
    pyautogui.mouseUp(button='left')
    pyautogui.mouseUp(button='right')

def automatiser_actions():
    prendre_arme()
    viser_et_lancer_molotov()
    ranger_arme()

while True:
    automatiser_actions()
    time.sleep(5)