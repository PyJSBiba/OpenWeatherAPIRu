import requests
from decouple import config

API_KEY = config('API_KEY')

def get_weather(api_key, city, lang="ru"):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "lang": lang,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    return weather_data

def print_weather_info(weather_data):
    city_name = weather_data["name"]
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    cloudiness = weather_data["clouds"]["all"]
    print(f"Погода в городе: {city_name}")
    print(f"Описание: {weather_description.capitalize()}")
    print(f"Температура: {temperature}°C")
    print(f"Ощущается как: {feels_like}°C")
    print(f"Влажность: {humidity}%")
    print(f"Скорость ветра: {wind_speed} m/s")
    print(f"Облачность: {cloudiness}%")

if __name__ == "__main__":
    city = input("Введите город: ")
    
    weather_data = get_weather(API_KEY, city)
    print_weather_info(weather_data) 