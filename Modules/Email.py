import smtplib

from config import Keys
from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech


class Email():
    message = ""
    recipient = ""

    tts = TextToSpeech()
    stt = SpeechToText()

    def createMessage(self):

        # print("What would you like to send?")
        self.tts.speak("What would you like to send?")
        # message = input(": ")
        message = self.stt.listen()

        if message != "":
            # print("Who would you like to send it to?")
            tts.speak("Okay, who would you like to send the message to?")
            # recipient = input(": ")
            recipient = self.stt.listen()
            tts.speak("Okay, you are sending the message " + message + " to " +
                      recipient + ", would you like to send the message?")

            answer = stt.listen()

            if "Yes" in answer:
                tts.speak("Seinding message now.")
                self.sendEmail(recipient, message)
            else:
                tts.speak("Okay, I won't send the message.")

    def sendEmail(self, recipient, message):

        print("Okay, sending message to " + recipient)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()

        server.starttls()
        server.login(Keys.email, Keys.password)

        server.sendmail('<'+Keys.email+'>', '<'+recipient+'>',
                        message)

        print("Okay, message has been sent.")
