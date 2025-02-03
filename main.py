import pyautogui
import time
import psutil
import keyboard
import sys
import os
import win32gui
import win32con

def est_fivem_lance():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'FiveM.exe':
            return True
    return False

def mettre_fivem_premier_plan():
    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            if "FiveM" in win32gui.GetWindowText(hwnd):
                win32gui.SetForegroundWindow(hwnd)
                win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    win32gui.EnumWindows(callback, None)

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

def on_f11_press(event):
    if event.name == 'f11':
        print("Touche F11 détectée. Arrêt du script...")
        keyboard.unhook_all()  
        os._exit(0)

def main():
    keyboard.on_press(on_f11_press)

    while True:
        if est_fivem_lance():
            mettre_fivem_premier_plan()
            automatiser_actions()
            time.sleep(5)
        else:
            time.sleep(10)

if __name__ == "__main__":
    main()