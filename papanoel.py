#!/usr/bin/env python3c
import time
import os

# Couleurs ANSI
RED = "\033[91m"
RESET = "\033[0m"  # Réinitialise la couleur

# Père Noël en ASCII
papa_noel = f"""
    {RED}*   *
   *o* *o*
     * *
   **   **
  *  JOYEUX *
  *   NOËL   *
   **     **
     *****
    *     *{RESET}
"""

cadeau = f"""
    {RED}🎁{RESET}
"""

def animation_papa_noel():
    for i in range(5):  # Animation en 5 étapes
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Le Père Noël arrive avec des cadeaux ! 🎅🎄")
        print(papa_noel)
        print(" " * i + cadeau)
        time.sleep(1)

# Lancer l'animation
animation_papa_noel()
