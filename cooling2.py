#!/usr/bin/env python3
import sys

def control_temperature(outside_temp, in_house_temp, heating_threshold, cooling_threshold):
    """
    Controls the heating and cooling system based on the external and in-house temperatures.
    """
    if in_house_temp < heating_threshold:
        action = "heating"
        in_house_temp += 0.5  # Heating increases the temperature
    elif in_house_temp > cooling_threshold:
        action = "cooling"
        in_house_temp -= 0.5  # Cooling decreases the temperature
    else:
        action = "nothing"
        # Move the in-house temperature toward the outside temperature
        if in_house_temp < outside_temp:
            in_house_temp += 0.25
        elif in_house_temp > outside_temp:
            in_house_temp -= 0.25
    
    return in_house_temp, action

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 expert_system.py <heating_threshold> <cooling_threshold>")
        sys.exit(1)
    
    heating_threshold = float(sys.argv[1])
    cooling_threshold = float(sys.argv[2])
    in_house_temp = heating_threshold  # Assume initial in-house temperature equals the heating threshold

    for outside_temp in sys.stdin:
        outside_temp = float(outside_temp.strip())  # Read outside temperature from standard input

        # Control the temperature based on the outside and in-house temperatures
        in_house_temp, action = control_temperature(outside_temp, in_house_temp, heating_threshold, cooling_threshold)

        # Output the result
        print(f"{outside_temp:.1f} - {action} - {in_house_temp:.1f}")

if __name__ == "__main__":
    main()



































