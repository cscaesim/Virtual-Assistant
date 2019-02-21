import requests
from TextToSpeech import TextToSpeech


class Joke():

    def get_Joke(self):
        response = requests.get("https://geek-jokes.sameerkumar.website/api")
        joke = response.json()

        return joke

    def tell_Joke(self):
        tts = TextToSpeech()
        joke = self.get_Joke()
        tts.speak(joke)
        print(joke)
