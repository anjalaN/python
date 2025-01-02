#!/usr/bin/env python3
import sys
import math
import random

def get_season_temperature(season):
    """
    Get a base temperature range for a given season.
    Each season will have a different temperature range.
    """
    season_temperatures = {
        'spring': (10, 20),
        'summer': (25, 35),
        'fall': (15, 25),
        'winter': (-5, 5)
    }
    
    return season_temperatures.get(season.lower())

def simulate_daily_temperature(season):
    base_temp_range = get_season_temperature(season)
    if not base_temp_range:
        print("Invalid season or no season provided. Please specify one of: spring, summer, fall, winter.")
        return

    min_temp, max_temp = base_temp_range
    total_slices = 48  # 30-minute slices for 24 hours
    scale_factor = 0.5  # Adjust to speed up the simulation

    for i in range(total_slices):
        # Calculate time within the day (0 to 24 hours)
        time_of_day = (i / total_slices) * 24
        # Calculate the sine wave for temperature fluctuation
        temperature = min_temp + (max_temp - min_temp) / 2 * (math.sin(math.pi * time_of_day / 12) + 1)
        # Add small random fluctuation
        temperature += random.uniform(-1, 1)
        print(f"Time: {i * scale_factor:.1f} seconds - Temperature: {temperature:.2f}°C")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python environment.py <season>")
        sys.exit(1)

    season = sys.argv[1]
    simulate_daily_temperature(season)
