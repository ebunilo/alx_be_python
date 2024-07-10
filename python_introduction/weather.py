import requests


def get_weather():
    """Using requests.get method, fetch weather data from weatherapi"""

    # Replace 'your_api_key_here' with your actual WeatherAPI key

    api_key = 'your_api_key_here'
    location = 'San Francisco'  # You can change this to any location you want
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

get_weather()
