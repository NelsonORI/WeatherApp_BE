import requests
from bs4 import BeautifulSoup
import schedule
import time
import threading
from weather_app import app, db 
from weather_app.models import WeatherForecast, TodayWeather

print("Weather scrapping has begun")

def fetch_weather():
    with app.app_context():  # Use the app context
        r = requests.get('https://weather.com/en-KE/weather/today/l/KEXX0009:1:KE?Goto=Redirected')
        soup = BeautifulSoup(r.content, 'html.parser')

        weather_days = soup.find_all('li', class_='Column--column--gUiRn')

        for day in weather_days:
            day_name = day.find('h3', class_='Column--label--tMb5q')
            high_temp = day.find('div', {'data-testid':'SegmentHighTemp'})
            low_temp = day.find('div', {'data-testid':'SegmentLowTemp'})
            condition = day.find('title')
            rain_percentage = day.find('div', {'data-testid':'SegmentPrecipPercentage'})

            if day_name and high_temp and low_temp and condition:
                existing_weather = WeatherForecast.query.filter_by(day=day_name.text.strip()).first()

                if existing_weather:
                    existing_weather.high_temp = high_temp.find('span', {'data-testid':'TemperatureValue'}).text.strip()
                    existing_weather.low_temp = low_temp.find('span', {'data-testid':'TemperatureValue'}).text.strip()
                    existing_weather.condition = condition.text.strip()
                    existing_weather.rain_percentage = rain_percentage.find('span', class_='Column--precip--YkErk').text.strip()
                else:
                    new_weather = WeatherForecast(
                        day=day_name.text.strip(),
                        high_temp=high_temp.find('span', {'data-testid':'TemperatureValue'}).text.strip(),
                        low_temp=low_temp.find('span', {'data-testid':'TemperatureValue'}).text.strip(),
                        condition=condition.text.strip(),
                        rain_percentage=rain_percentage.find('span', class_='Column--precip--YkErk').text.strip()
                    )
                    db.session.add(new_weather)

        db.session.commit()
        print("Weather data updated successfully")

# schedule.every().day.at("14:12").do(fetch_weather)
fetch_weather()

def fetch_today_data():
    with app.app_context():  # Use app context for DB operations
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
            existing_weather = TodayWeather.query.filter_by(day="Today").first()

            if existing_weather:
                existing_weather.sunrise = sun_rise.find('p', class_='TwcSunChart--dateValue--TzXBr').text.strip()
                existing_weather.sunset = sun_set.find('p', class_='TwcSunChart--dateValue--TzXBr').text.strip()
                existing_weather.highest_temp = highest_temp
                existing_weather.lowest_temp = lowest_temp
                existing_weather.wind_speed = wind_speed
                existing_weather.humidity = humidity.text.strip()
                existing_weather.dew_point = dew_point.find('span', {'data-testid':'TemperatureValue'}).text.strip()
                existing_weather.pressure = pressure.find('span', {'data-testid':'PressureValue'}).text.strip()
                existing_weather.uv_index = uv_index.find('span', {'data-testid':'UVIndexValue'}).text.strip()
                existing_weather.visibility = visibility.find('span', {'data-testid':'VisibilityValue'}).text.strip()
                existing_weather.moon_phase = moon_phase.find('div', {'data-testid':'wxData'}).text.strip()
            else:
                new_data = TodayWeather(
                    day="Today",
                    sunrise=sun_rise.find('p', class_='TwcSunChart--dateValue--TzXBr').text.strip(),
                    sunset=sun_set.find('p', class_='TwcSunChart--dateValue--TzXBr').text.strip(),
                    highest_temp=highest_temp,
                    lowest_temp=lowest_temp,
                    wind_speed=wind_speed,
                    humidity=humidity.text.strip(),
                    dew_point=dew_point.find('span', {'data-testid':'TemperatureValue'}).text.strip(),
                    pressure=pressure.find('span', {'data-testid':'PressureValue'}).text.strip(),
                    uv_index=uv_index.find('span', {'data-testid':'UVIndexValue'}).text.strip(),
                    visibility=visibility.find('span', {'data-testid':'VisibilityValue'}).text.strip(),
                    moon_phase=moon_phase.find('div', {'data-testid':'wxData'}).text.strip()
                )

                db.session.add(new_data)

        db.session.commit()
        print("Today's weather data updated successfully")

fetch_today_data()


# def run_scheduler():
#     while True:
#         schedule.run_pending()
#         time.sleep(60)  # Wait for 60 seconds before checking the schedule again

# scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
# scheduler_thread.start()
