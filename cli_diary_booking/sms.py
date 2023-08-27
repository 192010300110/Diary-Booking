"""
This file contains the implementation of the SMS class, which is responsible for sending SMS notifications using the Twilio package.
"""

from twilio.rest import Client


class SMS:
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        """
        Initialize an SMS object with the given Twilio credentials and sender number.
        """
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number

    def send_sms(self, to_number: str, message: str):
        """
        Send an SMS to the specified number with the given message.
        """
        client = Client(self.account_sid, self.auth_token)
        client.messages.create(
            body=message,
            from_=self.from_number,
            to=to_number
        )
