from gtts import gTTS
import os
import pygame
import pyttsx3
import time


class TextToSpeech():

    def __init__(self, language="en-au"):
        super(self.__class__, self).__init__()
        self.language = language

    def speak(self, text):
        self.save(text)
        self.play("voice.mp3")

    def save(self, text):
        tts = gTTS(text=text, lang='en-au', slow=False)
        tts.save("voice.mp3")

    def play(self, file):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(10)
        pygame.quit()
        pygame.mixer.quit()
