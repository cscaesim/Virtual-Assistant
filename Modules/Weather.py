import requests
import json
import geocoder

from gtts import gTTS
from config import Keys


class Weather():

    def checkWeather(self):
        location = self.getLocation('me')
        self.getWeather(location[0], location[1])

    def getLocation(self, location):
        current_location = geocoder.ip(location).latlng
        # print(current_location

        lat = current_location[0]
        lon = current_location[1]
        self.getWeather(lat, lon)

        return current_location

    def getWeather(self, latitude, longitude):

        url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = Keys.weather_key

        api_call_url = (url + "lat=" + str(latitude) + "&lon=" +
                        str(longitude) + "&appid=" + api_key)

        print(api_call_url)

        response = requests.get(api_call_url)
        json = response.json()
        # print(json)

        data = json["main"]
        current_temperature = data["temp"]
        fahrenheight_temp = (current_temperature - 273.15) * (9/5) + 32
        y = json["weather"]
        current_description = y[0]["description"]
        # current_description = [data]["description"]

        print("-----------------------------------")
        # print(fahrenheight_temp)
        # print(current_description)
        print("The current weather in your area is " +
              str(format(fahrenheight_temp, '.1f')) +
              " degrees, and the forecast is " +
              current_description + " today.")


test = Weather()
test.checkWeather()
