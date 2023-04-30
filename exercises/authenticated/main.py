# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True

def main():
    
    user1 = {
    "name": "Sorna",
    "valid": True # changing this will either run or not run the message_friends function
    }
    
    user2 = {
        "name": "Luigi",
        "valid": False
    }

    message_friends(user1) # This one will run
    message_friends(user2) # This one will not run

def authenticated(fn):
    # code here
    def wrapper_func(user):
        if user["valid"]:
            fn(user)
    return wrapper_func

@authenticated
def message_friends(user):
    print(f"message has been sent to {user.get('name')}")

if __name__ == "__main__":
    main()