# Send a SMS message to myself with Python
# CAN ONLY SEND TEXT TO VERIFIED NUMBERS

# Let the user send text over clargs
import os
import sys
from twilio.rest import Client

def main(clargs) -> None:
    
    # Get required info from environment variables
    sender = os.environ["SENDER"]
    receiver = os.environ["RECEIVER"]
    account_sid = os.environ["SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    
    # Make a Client object
    client = Client(account_sid, auth_token)
    
    # Build an SMS message
    message = client.messages.create(
        body=clargs,
        from_=sender,
        to=receiver
        )

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))