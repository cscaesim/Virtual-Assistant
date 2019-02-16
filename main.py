import datetime as dt
import smtplib
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

from gtts import gTTS

# Google Calendar
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from Modules.Events import main as events
from Modules.Weather import Weather
from TextToSpeech import TextToSpeech
from Modules.News import get_news
from Modules.Email import Email


def main():
    while True:
        command = input("Please give a command: ")
        print("Your command was: " + command)
        interpretCommand(command)


def interpretCommand(command):
    if "time" in command:
        print("The time is: " + str(dt.datetime.now()))

    elif "email" in command:
        email = Email()

        email.createMessage()

    elif "news" in command:
        get_news()

    elif "events" in command:
        checkCalendar()

    elif "test" in command:
        tts = TextToSpeech()
        tts.speak("Test")

    elif "weather" in command:
        weather = Weather()
        weather.checkWeather()

    elif "quit" in command:
        print("Quitting the program")
        quit()

main()
