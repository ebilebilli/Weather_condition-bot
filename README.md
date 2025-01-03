markdown
# Weather Condition Fetcher

This Python script fetches current weather conditions for a specified city using the OpenWeatherMap API.

## Prerequisites

- Python 3.x
- `requests` library
- An API key from [OpenWeatherMap](https://openweathermap.org/api)

## Installation

Install the required dependencies:

```bash
pip install requests

Usage
Get Your API Key:
Sign up or log in to OpenWeatherMap.
Navigate to your account dashboard to get your API key.
Set Up the Script:
Replace api_key in the script with your actual OpenWeatherMap API key.
Run the Script:

bash
python main.py

Example
Here's how to run the script for a specific city:

python
api_key = 'YOUR_API_KEY_HERE'
weather_condition_func(api_key, 'Baku')

This will output:

Weather condition for Baku:
Temperature: X°C
Humidity: Y%
Wind Speed: Z m/s
Date: YYYY-MM-DD HH:MM:SS

Code Structure
Imports:
requests: To make HTTP requests to the API.
datetime: For timestamping the data.
Function weather_condition_func:
Takes api_key and city as parameters.
Makes a GET request to the OpenWeatherMap API with the provided city name.
Parses the JSON response to extract temperature, humidity, and wind speed.
Prints the weather conditions along with the current date and time.

Notes
The API key should be kept secret and not shared in the source code. Consider using environment variables or a configuration file for this purpose.
The weather data is returned in metric units by default (units='metric'). Change this parameter if you need different units.
The bs4 (BeautifulSoup) library is imported but not used in this script. It's likely included for potential future expansion into HTML parsing if needed.

Troubleshooting
Unauthorized Error: If you get a 401 status code, your API key might be incorrect or expired. Double-check your key or generate a new one.
API Limits: Be aware of the request limits imposed by OpenWeatherMap. Consider upgrading to a paid plan for more requests or implement rate limiting.

License
This project is open source and available under the MIT License (LICENSE).

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. 

Acknowledgements
Thanks to OpenWeatherMap for providing a free tier of their weather data API.