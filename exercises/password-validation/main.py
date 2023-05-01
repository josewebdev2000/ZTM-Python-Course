# Use regex for password validator to check for a password that needs to be
# 8 characters long

import re

def main() -> None:
    
    user_p = input("Enter a password: ")
    
    print("Valid password") if is_valid(user_p) is not None else print("Invalid password")

def is_valid(password):
    
    valid_regex = r"^(?=.*[0-9])[A-Za-z0-9@$!%*#?&^_-]{8,}\d$"
    
    pattern = re.compile(valid_regex)
    
    possible_match = pattern.search(password)
    
    return possible_match
    

if __name__ == "__main__":
    main()