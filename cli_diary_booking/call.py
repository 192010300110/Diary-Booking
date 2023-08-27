## call.py
from twilio.rest import Client


class Call:
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        """
        Initialize a Call object with the given Twilio credentials and sender number.
        """
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number

    def make_call(self, to_number: str, message: str):
        """
        Make a phone call to the specified number with the given message.
        """
        client = Client(self.account_sid, self.auth_token)
        client.calls.create(
            twiml=f'<Response><Say>{message}</Say></Response>',
            from_=self.from_number,
            to=to_number
        )
