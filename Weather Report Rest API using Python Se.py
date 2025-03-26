import requests
import json

def fetch_weather_data():
    urls = [
        "https://api.weatherbit.io/v2.0/current?lat=30&lon=50&key=20",
        "https://api.weatherbit.io/v2.0/current?postal_code=1230&key=20"
    ]
    
    for url in urls:
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
            generate_report(weather_data)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")

def generate_report(data):
    if "data" in data and len(data["data"]) > 0:
        weather_info = data["data"][0]
        report = f"Weather Report:\n"
        report += f"Location: {weather_info.get('city_name', 'Unknown')}, {weather_info.get('country_code', 'Unknown')}\n"
        report += f"Temperature: {weather_info.get('temp', 'N/A')}°C\n"
        report += f"Humidity: {weather_info.get('rh', 'N/A')}%\n"
        report += f"Wind Speed: {weather_info.get('wind_spd', 'N/A')} m/s\n"
        report += f"Weather: {weather_info['weather'].get('description', 'Unknown')}\n"
        print(report)
    else:
        print("No weather data available.")

if __name__ == "__main__":
    fetch_weather_data()