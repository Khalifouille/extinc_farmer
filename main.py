import time
import psutil
import keyboard
import sys
import os
import win32gui
import win32con
import pydirectinput
import cv2
import numpy as np
from PIL import ImageGrab

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
    for _ in range(30):
        pydirectinput.press('e')  
        time.sleep(0.1)
    time.sleep(0.1)

def ouvrir_tab():
    pydirectinput.press('tab')  
    time.sleep(1)

def fermer_tab():
    pydirectinput.press('tab')  
    time.sleep(1)

def detecter_image(image_path, zone, confidence=0.8):

    screenshot = np.array(ImageGrab.grab(bbox=zone))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if template is None:
        print(f"Erreur : Impossible de charger l'image {image_path}.")
        return None
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        x, y = max_loc
        x += zone[0]
        y += zone[1]
        print(f"Score de confiance de {max_val:.2f}.")
        return (x, y)
    else:
        print(f"Image non détectée (meilleur score de confiance : {max_val:.2f}).")
        return False

def cliquer_sur_position(x, y):
    pydirectinput.moveTo(x, y) 
    time.sleep(0.2)
    pydirectinput.click()
    time.sleep(0.5)

def clique_marcher():
    pydirectinput.moveTo(1102, 52) 
    time.sleep(0.1)
    pydirectinput.click()
    time.sleep(0.1)

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
        zone_ecran = (126, 115, 1798, 539)

        while True:
            viser_et_lancer_molotov()
            time.sleep(1)
            ramasser_loot()
            time.sleep(1)
            ouvrir_tab()
            time.sleep(1)


            
            image_path = "bandage.png"  
            position = detecter_image(image_path, zone_ecran)
            if position:
                x, y = position
                print(f"Je clique ici : ({x}, {y})")
                cliquer_sur_position(x, y)
            else:
                print("L'image n'a pas été détectée dans la zone spécifiée.")
            time.sleep(1)


            ## clique_marcher() -- Utilisation plus tard tkt


            fermer_tab()
            time.sleep(1)
            ranger_arme()
            print("Attends 5 minutes maintenant !")
            time.sleep(10)  
    else:
        sys.exit()

if __name__ == "__main__":
    main()