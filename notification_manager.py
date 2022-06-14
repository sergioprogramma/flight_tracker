account_sid = "AC25aad92a99c628e1cc28a5e23947de08"
auth_token = "b1838e19bbad4c8262f44ea066b279eb"

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_text(self, dep_city, dep_airport, ar_city, ar_airport, price, tomorrow, last_day):
        proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Important message! The flight from {dep_city}-{dep_airport} to {ar_city}-{ar_airport} has a new lowest price of {price}. From {tomorrow} to {last_day}",
            from_="+16812525644",
            to="+16473940639"
        )
        print(message.status)

