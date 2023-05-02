# Send HTML email templates using Python

# Python Email Sending Example
import smtplib
import sys
from email.message import EmailMessage
from string import Template
from pathlib import Path

def main() -> None:
    
    # Get HTML Template Content
    html_content = Template(Path("html", "index.html").read_text())
    
    # Substitute
    html_substituted = html_content.substitute(name = "Tilin")
    
    # Get email object after configuring it
    email_to_send = configure_email(sender = "Dr Heinz Doofenshmirtz",
                                    to = "jabg1234@protonmail.com",
                                    subject="Honor Scholarship",
                                    content=html_substituted,
                                    content_type='html')
    
    # Send the email
    send_email(email_to_send)

def configure_email(sender='', to='', subject='', content='', content_type=''):
    """Configure email object"""
    
    # Set up headers of email
    email = EmailMessage()
    email['from'] = sender
    email['to'] = to
    email['subject'] = subject
    
    email.set_content(content, content_type)
    
    return email

def send_email(email_obj):
    """Send email to desired person"""
    
    # Get SMPT server to send email
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        
        # ehlo SMTP to start out communication
        smtp.ehlo()
        
        # Encrypt communication
        smtp.starttls()
        
        # Login with Google Creds
        smtp.login(sys.argv[1], sys.argv[2])
        
        # Now send the email message
        smtp.send_message(email_obj)
        
        print("Email was sent successfully")
        

if __name__ == "__main__":
    main()