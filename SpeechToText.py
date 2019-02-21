import speech_recognition as sr


class SpeechToText:

    def __init__(self):
        self.sr = sr

    def listen(self):
        r = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text
        except UnkownValueError:
            print("Your speech was not able to be recognized")
            return ""


test = SpeechToText()

test.listen()
