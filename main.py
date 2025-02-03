import time
import psutil
import keyboard
import sys
import os
import win32gui
import win32con
import pydirectinput

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
                time.sleep(1)
    win32gui.EnumWindows(callback, None)

def prendre_arme():
    pydirectinput.press('1')  
    time.sleep(1)

def ranger_arme():
    for _ in range(2):
        pydirectinput.press('1')  
        time.sleep(0.5)
    time.sleep(1)

def viser_et_lancer_molotov():
    pydirectinput.mouseDown(button='right')  
    time.sleep(1)
    pydirectinput.mouseDown(button='left')  
    time.sleep(0.5)
    pydirectinput.mouseUp(button='left') 
    pydirectinput.mouseUp(button='right')  

def ramasser_loot():
    for _ in range(15):
        pydirectinput.press('e')  
        time.sleep(0.5)
    time.sleep(1)

def ouvrir_tab():
    pydirectinput.press('tab')  
    time.sleep(1)

def fermer_tab():
    pydirectinput.press('tab')  
    time.sleep(1)

def on_f11_press(event):
    if event.name == 'f11':
        print("STOP STOP")
        keyboard.unhook_all() 
        os._exit(0)  

def main():
    keyboard.on_press(on_f11_press)

    if est_fivem_lance():
        mettre_fivem_premier_plan()
        time.sleep(2)
        prendre_arme()

        while True:
            viser_et_lancer_molotov()
            time.sleep(1)
            ramasser_loot()
            time.sleep(1)
            ouvrir_tab()
            time.sleep(1)



            fermer_tab()
            time.sleep(1)
            ranger_arme()
            print("Attends 5 minutes maintenant !")
            time.sleep(10)  
    else:
        sys.exit()

if __name__ == "__main__":
    main()