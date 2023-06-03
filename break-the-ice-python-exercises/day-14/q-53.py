"""
Question:

    Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. 
    
    Both user names and company names are composed of letters only.

    Example: If the following email address is given as input to the program:
    
    john@google.com
    
    Then, the output of the program should be:
    
    john

    In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

    Use \w to match letters.

"""

import re

def main():
    
    user_email = input("Enter your email: ")
    
    if is_valid_email(user_email):
        print(f"Your username is: {get_user_from_email(user_email)}")
    
    else:
        print(f"{user_email} is an invalid email.")

def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

def get_user_from_email(email):
    
    user = email.split("@")[0]
    return user

if __name__ == "__main__":
    main()