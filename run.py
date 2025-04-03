import threading
import schedule
import time
from weather_app import app
from weather_app.scrapper import fetch_weather, fetch_today_data

def run_scheduler():
    """Runs the scraper every hour in the background."""
    schedule.every().hour.do(fetch_weather)
    schedule.every().hour.do(fetch_today_data)
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check the schedule every minute

if __name__ == "__main__":
    # Start the scheduler in a background thread
    scraper_thread = threading.Thread(target=run_scheduler, daemon=True)
    scraper_thread.start()

    # Start the Flask server
    app.run(debug=True)
