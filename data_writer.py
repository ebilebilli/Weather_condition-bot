import json

def data_writer(weather_data):
    with open('weather_data.json', '+a') as file:
        json.dump(weather_data, file)
        file.write('\n')