import speech_recognition as sr
from tempfile import TemporaryFile

from gtts import gTTS
import os
import pygame
import pyttsx3
import time


pygame.mixer.init()
TextToSpeak = ("Here is the news for you today,"
               " how about this very long sentence."
               "What about if I did this, isn't that great")

tts = gTTS(text=TextToSpeak, lang='en', slow=False)
tts.save('good.mp3')

pygame.init()
pygame.mixer.music.load("good.mp3")
pygame.mixer.music.play()
time.sleep(10)

print("Sound playing")

# pygame.mixer.music.load('good.mp3')
# pygame.mixer.music.play()
print("Sound played")
