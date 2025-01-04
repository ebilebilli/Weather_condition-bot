import requests

from datetime import datetime
from settings import API_KEY
from data_writer import data_writer

def main(city: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

    data = {
        'City': city,
        'Temperature': temperature,
        'Humidity': humidity,
        'Wind Speed': wind_speed,
        'Date': date
    }
    
    data_writer(data)
    print(data)

if __name__ == '__main__':
    city = input('Write city name for info: ').strip().title()
    main(city)