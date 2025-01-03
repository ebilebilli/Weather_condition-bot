import requests
from datetime import datetime
from api_key_reader import API_KEY
from data_writer import data_writer

def main(api_key: str, city: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    weather_data = response.json()

    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

    data = {'City': city,
        'Temperature': temperature,
        'Humidity': humidity,
        'Wind Speed': wind_speed,
        'Date': date}
    data_writer(data)
    print(data)


city = input('Write city name for info: ').title()

if __name__ == '__main__':
    main(API_KEY, city)