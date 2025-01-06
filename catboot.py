#!/usr/bin/env python3
import re
import requests

def get_weather_details(location):
    """
    Fetch detailed weather information for a given location.
    """
    api_key = "9d8e100fbf99d17abae7be5486ff297f"  # Replace with your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature in °C
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            cloudiness = data['clouds']['all']
            wind_speed = data['wind']['speed']

            cloud_description = "no clouds" if cloudiness == 0 else f"{cloudiness}% cloudiness"
            return (
                f"The current weather in {location} is:\n"
                f"- Temperature: {temp}°C\n"
                f"- Humidity: {humidity}%\n"
                f"- Cloudiness: {cloud_description}\n"
                f"- Wind speed: {wind_speed} km/h."
            )
        else:
            return f"Could not find weather information for {location}. Please try another location."
    except Exception as e:
        return f"An error occurred: {e}"

def chatbot():
    print("Welcome to Weather Bot!")
    print("Ask me about the current weather in any city. Type 'exit' to quit.")
    while True:
        question = input("Ask?: ")
        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        if "weather" in question.lower():
            match = re.search(r"in ([\w\s]+)", question)
            if match:
                location = match.group(1).strip()
                print(get_weather_details(location))
            else:
                print("Please specify a location. For example: 'What is the weather in Paris?'")
        else:
            print("I can only answer weather-related questions. Try asking about the weather.")

if __name__ == "__main__":
    chatbot()
