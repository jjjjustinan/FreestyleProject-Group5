import os

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv() # go look in the .env file for any env vars

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")

def send_email(recipient_address=SENDER_ADDRESS, subject="YOUR REQUESTED RECIPE", html_content="YOUR REQUESTED RECIPE"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=SENDER_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)
        return response.status_code

    except Exception as err:
        return None