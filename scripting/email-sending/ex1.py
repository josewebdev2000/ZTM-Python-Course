# Python Email Sending Example
import smtplib
from email.message import EmailMessage
import sys

def main() -> None:
    
    # Set up headers of email
    email = EmailMessage()
    email['from'] = 'Jose Brache Garcia'
    email['to'] = 'jabg1234@protonmail.com'
    email['subject'] = 'College Grades Available'
    
    email.set_content("I am a Python Master")
    
    # Get SMPT server to send email
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        
        # ehlo SMTP to start out communication
        smtp.ehlo()
        
        # Encrypt communication
        smtp.starttls()
        
        # Login with Google Creds
        smtp.login(sys.argv[1], sys.argv[2])
        
        # Now send the email message
        smtp.send_message(email)
        
        print("Email was sent successfully")
        

if __name__ == "__main__":
    main()