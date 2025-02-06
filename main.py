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
import pytesseract
import re

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
    for _ in range(60):
        pydirectinput.press('e')  
    time.sleep(0.1)

def ouvrir_tab():
    pydirectinput.press('tab')  
    time.sleep(1)

def fermer_tab():
    pydirectinput.press('tab')  
    time.sleep(1)

def supprimer_item():
    for _ in range(28):
        pydirectinput.moveTo(244, 194) 
        time.sleep(0.1)
        pydirectinput.click(button='right')
        pydirectinput.click(button='right')
        time.sleep(0.1)

def detecter_texte(zone, dossier_images="captures_texte"):
    if not os.path.exists(dossier_images):
        os.makedirs(dossier_images)
    screenshot = np.array(ImageGrab.grab(bbox=zone))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    chemin_image = os.path.join(dossier_images, f"capture_kg.png")
    cv2.imwrite(chemin_image, screenshot)
    ## print(f"Image enregistrée : {chemin_image}")
    ## gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    ## gray = cv2.GaussianBlur(gray, (5, 5), 0)
    ## _, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    texte = pytesseract.image_to_string(screenshot, config='--psm 6')
    return texte.strip()

def detecter_image(image_path, zone, confidence=0.8):
    screenshot = np.array(ImageGrab.grab(bbox=zone))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if template is None:
        return None
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= confidence:
        x, y = max_loc
        x += zone[0]
        y += zone[1]
        return (x, y)
    else:
        return False

def cliquer_sur_position(x, y):
    pydirectinput.moveTo(x, y) 
    time.sleep(0.1)
    pydirectinput.click()
    time.sleep(0.5)

def clique_marcher():
    ouvrir_tab()
    pydirectinput.moveTo(1102, 52) 
    time.sleep(0.1)
    pydirectinput.click()
    time.sleep(1)

def actualier_reclamer():
    time.sleep(0.1)
    clique_marcher()
    time.sleep(0.1)
    pydirectinput.click(1012, 139)
    time.sleep(0.1)
    pydirectinput.click(1073, 475)
    time.sleep(0.1)
    pydirectinput.click(882, 475)
    time.sleep(0.1)
    fermer_tab()
    time.sleep(1)

def on_f11_press(event):
    if event.name == 'f11':
        keyboard.unhook_all() 
        os._exit(0)  

def main():
    keyboard.on_press(on_f11_press)

    if est_fivem_lance():
        mettre_fivem_premier_plan()
        time.sleep(2)
        prendre_arme()

        zone_ecran = (126, 115, 1798, 539)
        zone_ecran2 = (124, 555 , 1805, 869)

        images_a_detecter = [
            "images_loot/caisse.png", 
            "images_loot/kevlar.png",
            "images_loot/antizin_shot.png",
            "images_loot/flesh_dot.png",
            "images_loot/berserker_shot.png",
            "images_loot/molotov.png",
            "images_loot/carabine_mk2.png",
            "images_loot/mitralleuse.png",
            "images_loot/carabine_spe.png",
            "images_loot/carabine.png",
            "images_loot/cog.png"
        ]

        images_a_return = [
            "images_loot/molotov.png"
        ]

        start_time = time.time()

        while True:
            if time.time() - start_time >= 180:
                print("Vente au marché !")
                actualier_reclamer()
                start_time = time.time()

            viser_et_lancer_molotov()
            time.sleep(1)
            ramasser_loot()
            time.sleep(1)
            ouvrir_tab()
            time.sleep(1)

## CHECK SI IMAGE EST SUR ECRAN EN BOUCLE JUSQUA PLUS D'IMAGE A DETECTER ##

            for image_path in images_a_detecter:
                while True:
                    position = detecter_image(image_path, zone_ecran)
                    if position:
                        x, y = position
                        cliquer_sur_position(x, y) 
                        time.sleep(1)
                    else:
                        break

            supprimer_item()

## CHECK SI IMAGE A RETURN EST SUR ECRAN EN BOUCLE JUSQUA PLUS D'IMAGE A DETECTER ##

            for image_path in images_a_return:
                while True:
                    position = detecter_image(image_path, zone_ecran2)
                    if position:
                        x, y = position
                        cliquer_sur_position(x, y) 
                        time.sleep(1)
                    else:
                        break

            zone_texte = (1669, 551, 1719, 581)  
            texte_detecte = detecter_texte(zone_texte)
            if texte_detecte:
                print(f"Texte détecté : {texte_detecte}")
                match = re.search(r'\d+', texte_detecte)
                if match:
                    poids = int(match.group())
                    if poids >= 30:
                        print("+30kg")
            else:
                print("Aucun texte détecté.")
## ---------------------------------------------------------------------------------------------

            time.sleep(1)
            fermer_tab()
            time.sleep(1)
            prendre_arme()
            time.sleep(120)  
    else:
        sys.exit()

if __name__ == "__main__":
    main()