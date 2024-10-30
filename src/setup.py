import requests
def fetch_weather_data(city):
    api_key = "https://api.tomorrow.io/v4/weather/realtime?location=myanmar&apikey=XXX"  # replace your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Could not fetch weather data. Please check the city name."}
    
    return response.json()