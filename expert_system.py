#!/usr/bin/env python3
import sys
import time

def adjust_temperature(external_temp, in_house_temp, heating_threshold, cooling_threshold):
    """
    Ajuste la température intérieure selon la température extérieure et les seuils.
    """
    action = ""
    
    if in_house_temp < heating_threshold:
        # Activer le chauffage si la température intérieure est en dessous du seuil
        action = "heating"
        in_house_temp += 0.5  # Augmenter la température de 0.5°C
    elif in_house_temp > cooling_threshold:
        # Activer la climatisation si la température intérieure est au-dessus du seuil
        action = "cooling"
        in_house_temp -= 0.5  # Diminuer la température de 0.5°C
    else:
        # Aucune action si la température intérieure est dans la plage confortable
        action = "nothing"
    
    return in_house_temp, action

def main():
    if len(sys.argv) != 3:
        print("Usage: python expert_system.py <external_temp> <heating_threshold>")
        sys.exit(1)

    # Paramètres de la ligne de commande
    external_temp = float(sys.argv[1])
    heating_threshold = float(sys.argv[2])
    cooling_threshold = 7.5  # Un seuil fixe pour la climatisation

    # Initialiser la température intérieure à la même température que l'extérieur
    in_house_temp = external_temp

    # Simuler la régulation de la température
    while True:
        # Ajuster la température intérieure
        in_house_temp, action = adjust_temperature(external_temp, in_house_temp, heating_threshold, cooling_threshold)

        # Afficher les résultats
        print(f"External Temp: {external_temp}°C | Action: {action} | In-house Temp: {in_house_temp:.1f}°C")

        # Attendre une seconde avant la prochaine itération
        time.sleep(1)

if __name__ == "__main__":
    main()



























