import requests
from bs4 import BeautifulSoup
import schedule
import time

weather_data = []

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

        

    weather_data = new_data

schedule.every().day.at("20:17").do(fetch_weather)


print("⏳ Weather scraper scheduled. Running in the background...")

import threading
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()