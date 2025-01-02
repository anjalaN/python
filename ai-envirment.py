#!/usr/bin/env python3
import sys
import random
import math
import time

def simulate_temperature(season):
    """
    Simulate daily temperature variations based on the given season.
    """
    # Define temperature ranges for each season
    seasons = {
        "spring": (7, 16),
        "summer": (20, 35),
        "autumn": (5, 15),
        "winter": (-5, 5)
    }

    if season not in seasons:
        print("Invalid season. Please choose from: spring, summer, autumn, winter.")
        return

    min_temp, max_temp = seasons[season]
    cycle_duration = 48  # Full day in 48 seconds
    step = 2 * math.pi / cycle_duration  # Step size for sine function

    print(f"Simulating temperatures for {season.capitalize()}...\n")

    for i in range(cycle_duration):
        # Sine wave-based temperature variation
        base_temp = (max_temp - min_temp) / 2 * math.sin(step * i) + (max_temp + min_temp) / 2
        # Add random variation
        variation = random.uniform(-0.5, 0.5)
        current_temp = round(base_temp + variation, 1)

        # Print temperatures in a compact format
        print(f"{current_temp}", end=" ", flush=True)
        if (i + 1) % 5 == 0:  # New line after every 5 values
            print()
        time.sleep(1)  # Simulate real-time delay for one second

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 environment.py <season>")
        print("Season can be: spring, summer, autumn, or winter.")
        sys.exit(1)

    season = sys.argv[1].lower()
    simulate_temperature(season)

if __name__ == "__main__":
    main()
