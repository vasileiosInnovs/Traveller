import os
from mailjet_rest import Client

def send_email(to_email, subject, html_content):
    api_key = os.getenv("MAILJET_API")
    api_secret = os.getenv("MAILJET_SECRET_KEY")

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "tom@traveller.com",
                    "Name": "Traveller"
                },
                "To": [
                    {
                        "Email": to_email,
                        "Name": "User"
                    }
                ],
                "Subject": subject,
                "HTMLPart": html_content
            }
        ]
    }

    result = mailjet.send.create(data=data)
    return result.status_code == 200
