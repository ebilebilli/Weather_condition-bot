import requests
from datetime import datetime
from api_key_reader import API_KEY

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

    print(f'Weather condition for {city}:\n'
        f'Temperature: {temperature}\n'
        f'Humidity: {humidity}\n'
        f'Wind Speed: {wind_speed}\n'
        f'Date: {date}')
    
city = input('Write city name for info: ').title()

if __name__ == '__main__':
    main(API_KEY, city)