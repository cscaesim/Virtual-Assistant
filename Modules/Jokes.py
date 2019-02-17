import requests


class Joke():

    def get_Joke(self):
        response = requests.get("https://geek-jokes.sameerkumar.website/api")
        joke = response.json()

        return joke

    def tell_Joke(self):
        joke = self.get_Joke()
        print(joke)

joke = Joke()
joke.tell_Joke()
