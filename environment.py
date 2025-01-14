#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    environment.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/16 15:26:37 by arajapak          #+#    #+#              #
#    Updated: 2024/12/16 15:26:42 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3
import sys
import random
import math
import time

#san arrete program

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
    step = 2 * math.pi / 48  # Step size for sine function

    print(f"Simulating temperatures for {season.capitalize()}...\n")

    slice_counter = 0
    while True:
        # Sine wave-based temperature variation
        base_temp = (max_temp - min_temp) / 2 * math.sin(step * slice_counter) + (max_temp + min_temp) / 2
        # Add random variation
        variation = random.uniform(-0.5, 0.5)
        current_temp = round(base_temp + variation, 1)

        # Print temperature on a new line
        print(f"{current_temp}")
        time.sleep(1)  # Simulate real-time delay for one second
        slice_counter += 1

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 environment.py <season>")
        print("Season can be: spring, summer, autumn, or winter.")
        sys.exit(1)

    season = sys.argv[1].lower()
    simulate_temperature(season)

if __name__ == "__main__":
    main()

#avec arret slic 48 full day

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

        # Print temperature on a new line
        print(f"Temperature at slice {i + 1}: {current_temp}°C")
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
















