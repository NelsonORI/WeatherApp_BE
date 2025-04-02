import requests
from bs4 import BeautifulSoup
import schedule
import time

weather_data = []
today_data=[]

def fetch_weather():
    global weather_data
    r = requests.get('https://weather.com/en-KE/weather/today/l/KEXX0009:1:KE?Goto=Redirected')
    soup = BeautifulSoup(r.content, 'html.parser')

    weather_days = soup.find_all('li', class_='Column--column--gUiRn')
    new_data = []

    for day in weather_days:
        day_name = day.find('h3', class_='Column--label--tMb5q')
        high_temp = day.find('div', {'data-testid':'SegmentHighTemp'})
        low_temp = day.find('div', {'data-testid':'SegmentLowTemp'})
        condition = day.find('title')
        rain_percentage = day.find('div', {'data-testid':'SegmentPrecipPercentage'})

        if day_name and high_temp and low_temp and condition:
            weather_data.append({
                'Day':day_name.text.strip(),
                'High Temp': high_temp.find('span', {'data-testid':'TemperatureValue'}).text.strip(),
                'Low Temp': low_temp.find('span', {'data-testid':'TemperatureValue'}).text.strip(),
                'Condition': condition.text.strip(),
                'Rain Percentage': rain_percentage.find('span', class_='Column--precip--YkErk').text.strip()
            })
            print(weather_data)
        

    weather_data = new_data

schedule.every().day.at("05:00").do(fetch_weather)



def fetch_today_data():
    global today_data
    print("Starting the process...")
    
    url = 'https://weather.com/en-KE/weather/today/l/KEXX0009:1:KE?Goto=Redirected'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f"Failed to fetch data. HTTP Status Code: {r.status_code}")
        return

    soup = BeautifulSoup(r.content, 'html.parser')

    sun_rise = soup.find('div', {'data-testid':'SunriseValue'})
    sun_set = soup.find('div', {'data-testid':'SunsetValue'})
    temperatures = soup.find('div', {'data-testid':'WeatherDetailsListItem'})
    wind = soup.find('span', {'data-testid':'Wind'})
    humidity = soup.find('span', {'data-testid':'PercentageValue'})
    dew_points = soup.find_all('div', {'data-testid':'WeatherDetailsListItem'})
    pressure = dew_points[4] if dew_points else None
    uv_index = dew_points[5] if dew_points else None
    visibility = dew_points[6] if dew_points else None
    moon_phase = dew_points[7] if dew_points else None

    if temperatures:
        temps = temperatures.find_all('span', {'data-testid':'TemperatureValue'})
        highest_temp = temps[0].text.strip()
        lowest_temp = temps[1].text.strip()
    else:
        highest_temp = "N/A"
        lowest_temp = "N/A"

    wind_speed = None
    if wind:
        wind_values = wind.find_all('span')
        wind_speed = wind_values[-2].text.strip() + " " + wind_values[-1].text.strip()

    dew_point = dew_points[3] if dew_points else "N/A"
  

    if sun_rise and sun_set and temperatures and humidity:
        today_data.append({
            'Sunrise': sun_rise.find('p', class_='TwcSunChart--dateValue--TzXBr').text.strip(),
            'Sunset': sun_set.find('p', class_='TwcSunChart--dateValue--TzXBr').text.strip(),
            'Highest_Temp':highest_temp,
            'Lowest_Temp':lowest_temp,
            'Wind_speed':wind_speed,
            'Humidity':humidity.text.strip(),
            'Dew_point':dew_point.find('span', {'data-testid':'TemperatureValue'}).text.strip(), 
            'Pressure':pressure.find('span', {'data-testid':'PressureValue'}).text.strip(),
            'Uv_index':uv_index.find('span', {'data-testid':'UVIndexValue'}).text.strip(),
            'Visibility':visibility.find('span', {'data-testid':'VisibilityValue'}).text.strip(),
            'Moon_phase':moon_phase.find('div', {'data-testid':'wxData'}).text.strip()
        })
        print(today_data)

schedule.every().day.at("15:52").do(fetch_today_data)

import threading

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for 60 seconds before checking the schedule again

scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

# # Keep the script running
# while True:
#     time.sleep(1)  # Keep the main thread alive
