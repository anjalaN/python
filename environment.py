#!/usr/bin/env python3
import sys
import time
import random
import math

def generate_external_temperature(season):
    # Température de base selon la saison
    if season == "spring":
        # Simulation d'une température printanière avec des variations
        base_temp = 15.0  # Température moyenne en printemps
    elif season == "summer":
        base_temp = 30.0  # Température moyenne en été
    elif season == "autom":
        base_temp = 10.0  # Température moyenne en automne
    elif season == "winter":
        base_temp = 0.0   # Température moyenne en hiver
    else:
        raise ValueError("Saison non valide")

    # Ajouter de petites variations aléatoires pour chaque cycle
    temperature_variation = random.uniform(-2.0, 2.0)
    external_temp = base_temp + temperature_variation

    return round(external_temp, 2)

def main():
    if len(sys.argv) != 2:
        print("Usage: python environment.py <season>")
        sys.exit(1)

    season = sys.argv[1]

    while True:
        external_temp = generate_external_temperature(season)
        print(f" {external_temp}")
        time.sleep(1)  # Attente de 1 seconde pour simuler le temps

if __name__ == "__main__":
    main()











e




