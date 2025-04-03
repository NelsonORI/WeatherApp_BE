from weather_app import db

class WeatherForecast(db.Model):
    __tablename__ = 'weather_forecast'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    day = db.Column(db.String(50))
    high_temp = db.Column(db.String(10))
    low_temp = db.Column(db.String(10))
    condition = db.Column(db.String(100))
    rain_percentage = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, day, high_temp, low_temp, condition, rain_percentage):
        self.day = day
        self.high_temp = high_temp
        self.low_temp = low_temp
        self.condition = condition
        self.rain_percentage = rain_percentage

class TodayWeather(db.Model):
    __tablename__ = 'today_weather'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    day = db.Column(db.String(50))
    sunrise = db.Column(db.String(50))
    sunset = db.Column(db.String(50))
    highest_temp = db.Column(db.String(10))
    lowest_temp = db.Column(db.String(10))
    wind_speed = db.Column(db.String(50))
    humidity = db.Column(db.String(10))
    dew_point = db.Column(db.String(10))
    pressure = db.Column(db.String(10))
    uv_index = db.Column(db.String(10))
    visibility = db.Column(db.String(10))
    moon_phase = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, day, sunrise, sunset, highest_temp, lowest_temp, wind_speed, humidity, dew_point, pressure, uv_index, visibility, moon_phase):
        self.day = day
        self.sunrise = sunrise
        self.sunset = sunset
        self.highest_temp = highest_temp
        self.lowest_temp = lowest_temp
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.dew_point = dew_point
        self.pressure = pressure
        self.uv_index = uv_index
        self.visibility = visibility
        self.moon_phase = moon_phase