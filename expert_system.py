
#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: arajapak <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/16 15:27:30 by arajapak          #+#    #+#              #
#    Updated: 2024/12/16 15:27:34 by arajapak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



import sys
import time

def control_temperature(outside_temp, in_house_temp, heating_auto, cooling_auto):
    """
    This function controls heating or cooling based on the outside and inside temperatures.
    It returns the updated in-house temperature and the action taken.
    """
    if in_house_temp < heating_auto:
        action = "heating"
        in_house_temp += 0.5  # Increase temperature by 0.5 degrees due to heating
    elif in_house_temp > cooling_auto:
        action = "cooling"
        in_house_temp -= 0.5  # Decrease temperature by 0.5 degrees due to cooling
    else:
        action = "nothing"
        # Move the in-house temperature towards the outside temperature by 0.25 degrees
        if in_house_temp < outside_temp:
            in_house_temp += 0.25
        elif in_house_temp > outside_temp:
            in_house_temp -= 0.25

    # Ensure in-house temperature doesn't go beyond a realistic range
    in_house_temp = max(min(in_house_temp, 50), -10)  # Adjust to avoid extreme temps
    return in_house_temp, action

def main():
    if len(sys.argv) != 5:
        print("Usage: python3 environment.py <outside_temp> <heating_auto> <cooling_auto> <in_house_temp>")
        sys.exit(1)

    # Read parameters from command line
    outside_temp = float(sys.argv[1])  # Outside temperature
    heating_auto = float(sys.argv[2])  # Threshold to turn on heating
    cooling_auto = float(sys.argv[3])  # Threshold to turn on cooling
    in_house_temp = float(sys.argv[4])  # Initial in-house temperature

    print(f"Initial Outside Temp: {outside_temp}°C, Heating Threshold: {heating_auto}°C, Cooling Threshold: {cooling_auto}°C")

    # Run the simulation for a day (simulate over 48 steps for a full day)
    for cycle in range(48):
        in_house_temp, action = control_temperature(outside_temp, in_house_temp, heating_auto, cooling_auto)

        # Output the current status in the desired format
        print(f"{in_house_temp:.1f} - {action} - {in_house_temp + 1.0:.1f}")

        # Simulate a time delay (30 minutes)
        time.sleep(1)  # Adjust to simulate real-time delay

if __name__ == "__main__":
    main()
#for tester python3 expert_system.py 5.0 18.0 25.0 10.0(you can change parametre)









