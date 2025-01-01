#!/usr/bin/env python3
import sys
import time

def simulate_day(season):
    # Simulate different temperatures based on the season
    if season == "spring":
        # Spring has moderate temperatures
        temp_range = (10, 20)  # Example range: 10°C to 20°C
    else:
        print("Unknown season")
        return
    
    # Generate temperature slice over a day
    for cycle in range(48):  # Simulate 48 cycles (one per 30 minutes)
        outside_temp = temp_range[0] + (temp_range[1] - temp_range[0]) * (cycle / 47.0)
        # Print each temperature slice
        print(f"{outside_temp:.1f}")

        # Simulate 1 second delay between cycles
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 environment.py <season>")
        sys.exit(1)

    season = sys.argv[1]
    simulate_day(season)





































