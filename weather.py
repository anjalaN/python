#!/usr/bin/env python3
import requests

def get_weather(latitude, longitude):
    # Open-Meteo API URL for current weather forecast
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    # Send GET request to the Open-Meteo API
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the response JSON data
        data = response.json()
        
        # Extract current weather details
        current_weather = data['current_weather']
        
        temperature = current_weather['temperature']
        wind_speed = current_weather['windspeed']
        wind_direction = current_weather['winddirection']
        weather_code = current_weather['weathercode']
        
        # Display the weather information
        print(f"Current Weather at Latitude: {latitude}, Longitude: {longitude}:")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Speed: {wind_speed} km/h")
        print(f"Wind Direction: {wind_direction}°")
        
        # Convert weather code to human-readable description
        weather_conditions = {
            0: "Clear sky",
            1: "Partly cloudy",
            2: "Cloudy",
            3: "Light rain",
            4: "Moderate rain",
            5: "Heavy rain"
        }
        
        weather_condition = weather_conditions.get(weather_code, "Unknown")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("Failed to retrieve weather data. Please check the coordinates and try again.")

def main():
    print("Weather Application")
    
    # Ask for user input for latitude and longitude
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))
    
    # Call the function to get and display weather for the given coordinates
    get_weather(latitude, longitude)

if __name__ == "__main__":
    main()
