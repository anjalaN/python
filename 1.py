
import time
import random

def get_season_temp(season, time_slice):
  """
  Calculates the base temperature for a given season and time slice.

  Args:
    season: The season (e.g., "spring", "summer", "autumn", "winter").
    time_slice: The current time slice (0-47 for 48 slices per day).

  Returns:
    The base temperature for the given season and time slice.
  """
  base_temp = 0.0

  if season == "spring":
    base_temp = 10 + 5 * (time_slice / 47)  # Gradually increases
  elif season == "summer":
    base_temp = 25 - 5 * abs((time_slice - 24) / 24)  # Peaks around noon
  elif season == "autumn":
    base_temp = 15 - 5 * (time_slice / 47)  # Gradually decreases
  elif season == "winter":
    base_temp = 0 + 2 * (time_slice / 47) if time_slice < 24 else 2 - 2 * ((time_slice - 24) / 24)  # Low and gradual increase

  return base_temp

def simulate_daily_temperature(season):
  """
  Simulates daily temperature variations for a given season.

  Args:
    season: The season (e.g., "spring", "summer", "autumn", "winter").
  """
  while True:
    for time_slice in range(48): 
      base_temp = get_season_temp(season, time_slice)
      random_variation = random.uniform(-0.5, 0.5)  # Introduce small random variations
      temperature = base_temp + random_variation
    print(f" {temperature:.2f} ")
    time.sleep(1)  # Simulate 1 second per time slice

if __name__ == "__main__":
  season = input("Enter the season (spring, summer, autumn, winter): ")
  simulate_daily_temperature(season)

































