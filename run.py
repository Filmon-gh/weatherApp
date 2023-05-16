# Import the required modules
import requests  # Import the requests module for making HTTP requests
import json  # Import the json module for working with JSON data
import time
from tkinter import *  # Import the tkinter module for GUI
from datetime import datetime  # Import the datetime module for working with dates and times



API_key="6112a97c554eb760c42d9012cfc32ad6"

# Function to retrieve weather data from the OpenWeatherMap API for a given city name
def get_weather_data(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
    response = requests.get(url)
    return response.json()

def display_weather_data(weather_data):
    if 'cod' in weather_data and weather_data['cod'] != 200:
        print(f"Error: {weather_data['message']}")
    else:
        try:
            # Accessing specific weather data
            temperature_kelvin = weather_data['main']['temp']
            temperature_celsius = temperature_kelvin - 273.15
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            wind_speed = weather_data['wind']['speed']
        
            # Get the current date
            current_date = datetime.now().strftime('%Y-%m-%d')

            # Printing weather data using f-strings
            print(f"City: {city_name}")
            print(f"Date: {current_date}")
            print(f"Temperature: {temperature_celsius:.2f} °C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description}")
            print(f"Wind Speed: {wind_speed} m/s")

            # Additional if-else statements for diverse weather conditions
            if 'rain' in description.lower():
                print("\nRemember to bring an umbrella!\n")
            elif 'cloud' in description.lower():
                print("\nIt's a cloudy day.\n")
            elif temperature_celsius > 25:
                print("\nIt's hot outside. Stay hydrated!\n")
            elif temperature_celsius < 5:
                print("\nIt's cold outside. Bundle up!\n")
            else:
                print("\nEnjoy the weather!\n")
        except KeyError:
            print("Invalid weather data. Unable to display.")
            


city_name = input("Enter your city: ") # Prompt the user to enter their desired city name
weather_data = get_weather_data(city_name) # Retrieve the weather data for the specified city
display_weather_data(weather_data) # Display the weather data on the console

# Continuously prompts the user to enter a new city name and retrieves and displays the weather data for the entered city.
# The loop continues until the user enters 'q' to quit.q

while True:
    option = input("Enter a new city (or 'q' to quit): ")
    if option.lower() == 'q':
        break
    city_name = option
    weather_data = get_weather_data(city_name)
    display_weather_data(weather_data)

