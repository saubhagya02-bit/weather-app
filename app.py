from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None 
    error = ""

    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:

            icon_map = {
                "clear sky": "icons/sun.png",
                "few clouds": "icons/clouds.png",
                "scattered clouds": "icons/clouds.png",
                "broken clouds": "icons/clouds.png",
                "overcast clouds": "icons/overcast.png",
                "shower rain": "icons/rain.png",
                "rain": "icons/rain.png",
                "thunderstorm": "icons/rain.png",
                "snow": "icons/snow.png",
                "mist": "icons/clouds.png"
            }

            weather_description = data["weather"][0]["description"]
            weather_icon = icon_map.get(weather_description, "sun.png") 

            weather = {
                "city": city,
                "timezone": data["timezone"],
                "temp": data["main"]["temp"],
                "description": weather_description,
                "humidity": data["main"]["humidity"],
                "icon": weather_icon
            }
        else:
            error = "City not found!"

    return render_template("index.html", weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)
