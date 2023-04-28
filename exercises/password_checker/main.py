username = input("What's your username? ")
password = input("What's your password? ")

hidden_pass = "*" * len(password)

print(f"{username}, your password {hidden_pass} is {len(password)} long.")