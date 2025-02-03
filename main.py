import pyautogui
import time
import psutil

def fivem_lance():
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'FiveM.exe':  
            return True
    return False

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

def main():
    while True:
        if fivem_lance():
            print("FiveM est lancé")
            automatiser_actions()
            time.sleep(5)  
        else:
            print("FiveM n'est pas lancé")
            time.sleep(10)

if __name__ == "__main__":
    main()