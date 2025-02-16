# 🎮 FiveM Bot - Automatisation de tâches dans GLife: Extinction & Freeroam 🧟‍♂️

Ce projet est un **bot automatisé** pour le jeu **FiveM**, spécialement conçu pour le serveur **GLife: Extinction & Freeroam**. Il permet d'automatiser des tâches répétitives comme la gestion de l'inventaire, la vente d'objets sur le marché, et l'interaction avec l'environnement de jeu. Parfait pour optimiser votre gameplay ! 🚀

## 🌟 Fonctionnalités

- **🕹️ Détection de processus FiveM** : Vérifie si FiveM est en cours d'exécution.
- **🖥️ Mise au premier plan** : Met la fenêtre FiveM au premier plan et la maximise.
- **🎒 Gestion de l'inventaire** : Automatise la prise et le rangement d'armes, la collecte de loot, et la suppression d'items.
- **💰 Vente automatique** : Vente d'objets sur le marché en fonction des prix actuels récupérés via une API.
- **🖼️ Détection d'images** : Utilise **OpenCV** pour détecter des images spécifiques à l'écran et interagir avec elles.
- **🖱️ Interface utilisateur** : Une interface graphique simple pour démarrer et arrêter le bot.

  ## 🛠️ Prérequis

- **Python 3.x**
- **Bibliothèques Python** :
  ```bash
  pip install psutil keyboard pywin32 pydirectinput opencv-python numpy Pillow pytesseract requests
  ```
  
---

### Section 4 : Installation

## 🚀 Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/fivem-bot.git
   cd fivem-bot
    ```
---

### Section 5 : Utilisation

## 🎯 Utilisation

1. Lancez **FiveM** et connectez-vous au serveur **GLife: Extinction & Freeroam**.
2. Exécutez le script :
   ```bash
   python fivem_bot.py
    ```
---

### Section 6 : Configuration

## ⚙️ Configuration

- **Prix manuels** : Ajoutez des prix manuels pour les objets dans le fichier `prix_manuels.json`.
- **Images de détection** : Placez les images à détecter dans le dossier `images_loot`.

## 🚨 Arrêt d'urgence

Appuyez sur **`F11`** pour arrêter immédiatement le bot.

## ⚠️ Avertissement

Ce bot est conçu à des fins **éducatives** et pour des serveurs de jeu **privés**. Veuillez respecter les règles du serveur et ne pas utiliser ce bot de manière abusive.

