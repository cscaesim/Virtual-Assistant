import datetime as dt
import smtplib
import bs4
import nltk
import pickle
import os.path

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from nltk import word_tokenize
from nltk.corpus import stopwords
from gtts import gTTS

# Google Calendar
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Modules
from Modules.Events import main as events
from Modules.Weather import Weather
from TextToSpeech import TextToSpeech
from SpeechToText import SpeechToText
from Modules.News import get_news
from Modules.Email import Email
from Modules.Jokes import Joke


def main():
    sr = SpeechToText()

    while True:
        # command = input("Please give a command: ")
        command = sr.listen()
        sentence = command
        tokens = word_tokenize(sentence)
        name = []

        stop_words = set(stopwords.words('english'))
        clean_tokens = [w for w in tokens if w not in stop_words]
        tagged = nltk.pos_tag(clean_tokens)
        chunk_sentence = nltk.ne_chunk(tagged)

        for chunk in chunk_sentence:
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    name.append(' '.join(c[0] for c in chunk))

        print(name)
        print(clean_tokens)
        print(tagged)
        # print(name)
        print("Your command was: " + command)
        interpretCommand(command)


def interpretCommand(command):

    if "time" in command:
        now = dt.datetime.now()
        hour = now.hour - 12
        if (now == 0):
            hour = 12
        print("It is currently " + str(now.hour - 12) + ":" + str(now.minute))

    elif "email" in command:
        email = Email()
        email.createMessage()
    elif 'Who' in command:
        pass
    elif "news" in command:
        get_news()

    elif "events" in command:
        checkCalendar()

    elif "test" in command:
        tts = TextToSpeech()
        tts.speak("Test")

    elif "joke" in command:
        joke = Joke()
        joke.tell_Joke()

    elif "weather" in command:
        weather = Weather()
        weather.checkWeather()

    elif "quit" in command:
        print("Quitting the program")
        quit()
    else:
        print("Command not recognized, please try again.")

main()
