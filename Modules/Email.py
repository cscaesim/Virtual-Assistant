import smtplib

from config import Keys


class Email():

    message = ""
    recipient = ""

    def createMessage(self):

        print("What would you like to send?")
        message = input(": ")
        print("Who would you like to send it to?")
        recipient = input(": ")

        self.sendEmail(recipient, message)

    def sendEmail(self, recipient, message):

        print("Okay, sending message to " + recipient)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()

        server.starttls()
        server.login(Keys.email, Keys.password)

        server.sendmail('<'+Keys.email+'>', '<'+recipient+'>',
                        message)

        print("Okay, message has been sent.")
