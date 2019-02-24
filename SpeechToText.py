import speech_recognition as sr


class SpeechToText:

    def __init__(self):
        self.sr = sr

    def listen(self):
        r = sr.Recognizer()
        mic = sr.Microphone()

        print("Say something")

        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            print("Parsing audio")
            try:
                # print("You said" + r.recognize_google(audio))
                string = r.recognize_google(audio)
                return string
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("{0}".format(e))


# test = SpeechToText()

# test.listen()
