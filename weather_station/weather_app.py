# weather_station/weather_app.py
import requests
from config import WEATHER_KEY

url = "http://api.weatherapi.com/v1/current.json"

while True:
    city = input("\nEnter city name (or type 'exit' to quit): ")

    if city.lower() == "exit":
        print("Goodbye!")
        break

    query_params = {
        "key": WEATHER_KEY,
        "q": city
    }

    response = requests.get(url, params=query_params)
    weather_data = response.json()

    if "error" in weather_data:
        print("City not found. Please try again.")
    else:
        print("\n--- Weather Station ---")
        print(
            f"City: {weather_data['location']['name']}, {weather_data['location']['country']}")
        print(f"Condition: {weather_data['current']['condition']['text']}")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Feels like: {weather_data['current']['feelslike_c']}°C")
