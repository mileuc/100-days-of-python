import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("./.env")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER_NUM = os.getenv("SENDER_NUM")
RECIPIENT_NUM = os.getenv("RECIPIENT_NUM")

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)  # set up Twilio client using sid and token

    def send_notification(self, message):
        # create message that will be sent to us

        message = self.client.messages.create(
            body=message,
            from_=SENDER_NUM,
            to=RECIPIENT_NUM
        )

        print(message.status)  # just to make sure it was sent successfully
