import re

def main() -> None:
    
    valid_email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    
    pattern = re.compile(valid_email_regex)
    
    some_email = "some@email.com"
    not_email = "Not an email"
    
    a = pattern.search(some_email)
    b = pattern.search(not_email)
    
    print(a)
    print(b)

if __name__ == "__main__":
    main()