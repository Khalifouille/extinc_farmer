import time
import json
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
import requests
import re
import threading
import tkinter as tk
from tkinter import messagebox

def est_fivem_lance():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'FiveM.exe':
            return True
    return False

def mettre_fivem_premier_plan():
    def callback(hwnd, extra):
        titre = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowVisible(hwnd):
            if "FiveM® by Cfx.re - EU [NOT-RP] GLife: Extinction & Freeroam || PvP || Zombie || World leaderboard || discord.gg/gtalife" in win32gui.GetWindowText(hwnd):
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
    time.sleep(0.1)
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

def charger_prix_manuels():
    fichier_prix = "prix_manuels.json"
    if os.path.exists(fichier_prix):
        with open(fichier_prix, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def obtenir_prix(item, prix_detecte):   
    prix_manuels = charger_prix_manuels()
    if prix_detecte:
        return prix_manuels.get(item, prix_detecte)
    return prix_manuels.get(item, 999999)

def detecter_texte(zone, dossier_images="captures_texte"):
    if not os.path.exists(dossier_images):
        os.makedirs(dossier_images)
    screenshot = np.array(ImageGrab.grab(bbox=zone))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    chemin_image = os.path.join(dossier_images, f"capture_kg.png")
    cv2.imwrite(chemin_image, screenshot)
    texte = pytesseract.image_to_string(screenshot, config='--psm 6')
    return texte.strip()

def detecter_texte2(zone, dossier_images="captures_texte"):
    if not os.path.exists(dossier_images):
        os.makedirs(dossier_images)
    
    screenshot = np.array(ImageGrab.grab(bbox=zone))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    chemin_image2 = os.path.join(dossier_images, f"capture_prix.png")
    cv2.imwrite(chemin_image2, screenshot)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY) 
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    if np.mean(binary) > 127:
        binary = cv2.bitwise_not(binary)
    blur = cv2.GaussianBlur(binary, (3, 3), 0)
    kernel = np.ones((1,1), np.uint8)
    dilated = cv2.erode(blur, kernel, iterations=1)
    chemin_image_pretraitee = os.path.join(dossier_images, f"capture_prix_pretraitee.png")
    cv2.imwrite(chemin_image_pretraitee, dilated)
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789.,$'
    texte = pytesseract.image_to_string(dilated, config=custom_config)
    texte = texte.replace("9$", "$").strip()
    return texte.strip()

def detecter_texte3(zone, dossier_images="captures_texte"):
    if not os.path.exists(dossier_images):
        os.makedirs(dossier_images)
    screenshot = np.array(ImageGrab.grab(bbox=zone))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    if np.mean(binary) > 127:
        binary = cv2.bitwise_not(binary)
    chemin_image3 = os.path.join(dossier_images, f"debug_capture.png")
    chemin_image4 = os.path.join(dossier_images, f"debug_capture_processed.png")
    cv2.imwrite(chemin_image3, screenshot) 
    cv2.imwrite(chemin_image4, binary) 
    texte = pytesseract.image_to_string(binary, config='--psm 6')
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
    time.sleep(0.1)

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

BASE_API_URL = "https://api.gtaliferp.fr:8443/v1/extinction/marketplace/sell/"

ITEMS_API = {
    "loot_crate_medium": "caisse",
    "kevlar": "kevlar",
    "drug_antizin": "antizin_shot",
    "drug_zombie": "flesh_dot",
    "drug_berserker": "berserker_shot",
    "weapon_carbinerifle_mk2": "carabine_mk2",
    "weapon_mg": "mitralleuse",
    "weapon_specialcarbine": "carabine_spe",
    "weapon_carbinerifle": "carabine"
}

prix_cache = {}

def obtenir_prix_api(nom_objet):
    if nom_objet in prix_cache:
        return prix_cache[nom_objet]

    item_api_name = None
    for api_id, nom_fichier in ITEMS_API.items():
        if nom_fichier == nom_objet:
            item_api_name = api_id
            break

    if not item_api_name:
        print(f"Aucun ID API trouvé ! ")
        return None

    url = f"{BASE_API_URL}{item_api_name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                dernier_objet = data[-1]
                prix = dernier_objet.get("price", 0)
                prix_ajuste = max(0, prix - 1)  
                prix_cache[nom_objet] = prix_ajuste  
                return prix_ajuste
            else:
                print(f"Aucune vente trouvée pour {nom_objet}.")
        else:
            print(f"Erreur API ({response.status_code}) pour {nom_objet}")
    except Exception as e:
        print(f"Erreur lors de la récupération du prix de {nom_objet}: {e}")

    return None

def vente_inv_plein():
    time.sleep(0.1)
    ouvrir_tab()
    time.sleep(0.1)
    clique_marcher()
    time.sleep(0.1)
    pydirectinput.click(1012, 139)
    time.sleep(0.1)

    images_a_detecter = [
        "images_loot/caisse.png",
        "images_loot/kevlar.png",
        "images_loot/antizin_shot.png",
        "images_loot/flesh_dot.png",
        "images_loot/berserker_shot.png",
        "images_loot/carabine_mk2.png",
        "images_loot/mitralleuse.png",
        "images_loot/carabine_spe.png",
        "images_loot/carabine.png",
    ]

    zone_ecran3 = (31, 172, 1185, 433)
    zone_texte_arret = (1519, 945, 1901, 1024)

    for image_path in images_a_detecter:
        nom_objet = image_path.split("/")[-1].replace(".png", "")

        while True:
            texte_detecte_arret = detecter_texte3(zone_texte_arret)
            print(texte_detecte_arret)
            if "20 offres de" in texte_detecte_arret:
                print("Vente arrêtée.")
                return  

            position = detecter_image(image_path, zone_ecran3)
            if position:
                x, y = position
                cliquer_sur_position(x, y)
                time.sleep(1)

                prix_vente = obtenir_prix_api(nom_objet)
                if prix_vente is None:
                    print(f"Impossible de récupérer le prix de {nom_objet}.")
                    continue

                print(f"Vente de {nom_objet} au prix de {prix_vente}")

                cliquer_sur_position(1528, 344)
                pydirectinput.keyDown("ctrl")
                pydirectinput.press("a") 
                pydirectinput.keyUp("ctrl")
                time.sleep(0.1)
                pydirectinput.write(str(prix_vente))
                cliquer_sur_position(1809, 403)
            else:
                print(f"Aucune image détectée pour {nom_objet}.")
                break

def on_f11_press(event):
    if event.name == 'f11':
        keyboard.unhook_all() 
        os._exit(0)  

class FiveMBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FiveM Bot")
        self.root.geometry("400x200")

        self.running = False
        self.thread = None

        self.start_button = tk.Button(root, text="Démarrer", command=self.start_bot)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Arrêter", command=self.stop_bot, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(root, text="Statut: Arrêté", fg="red")
        self.status_label.pack(pady=10)

    def start_bot(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="Statut: En cours", fg="green")

            self.thread = threading.Thread(target=self.run_bot)
            self.thread.start()

    def stop_bot(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_label.config(text="Statut: Arrêté", fg="red")

    def run_bot(self):
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
            ]

            images_a_return = [
                "images_loot/molotov.png",
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
            ]

            start_time = time.time()

            while self.running:
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

                for image_path in images_a_detecter:
                    while self.running:
                        position = detecter_image(image_path, zone_ecran)
                        if position:
                            x, y = position
                            cliquer_sur_position(x, y) 
                            time.sleep(1)
                        else:
                            break

                supprimer_item()

                for image_path in images_a_return:
                    while self.running:
                        position = detecter_image(image_path, zone_ecran2)
                        if position:
                            x, y = position
                            cliquer_sur_position(x, y) 
                            time.sleep(1)
                        else:
                            break       

                zone_texte = (1665, 115, 1719, 133)  
                texte_detecte = detecter_texte(zone_texte)
                if texte_detecte:
                    match = re.search(r'\b(\d+)(?:[.,]\d+)?kg\b', texte_detecte)
                    if match:
                        poids = int(match.group(1))
                        if poids >= 1:
                            print(poids)
                            vente_inv_plein()
                else:
                    print("Aucun texte détecté.")

                time.sleep(1)
                fermer_tab()
                time.sleep(1)
                prendre_arme()
                time.sleep(120)  
        else:
            messagebox.showerror("Erreur", "FiveM n'est pas lancé.")
            self.stop_bot()

if __name__ == "__main__":
    root = tk.Tk()
    app = FiveMBotApp(root)
    root.mainloop()