import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Attachment, FileContent, FileName, FileType, Disposition, Mail

SENDGRID_API_KEY = "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"
SENDER_ADDRESS = "jjjjustinan@gmail.com"

def send_email(recipient_address=SENDER_ADDRESS, subject="YOUR REQUESTED RECIPE", html_content="YOUR REQUESTED RECIPE"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)

    print("HTML:", html_content)

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=SENDER_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)
        return response.status_code

    except Exception as err:
        print(type(err))
        print(err)
        return None