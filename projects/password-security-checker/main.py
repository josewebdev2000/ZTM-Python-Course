import sys
import requests
from hashlib import sha1
from constants import PASSWORD_API_ENDPOINT

def main(clargs):
    
    for password in clargs:
        count = pwned_api_check(password)
        
        if count:
            print(f"\n\"{password}\" was found {count} times.\nYou should change your password.\n")
        
        else:
            print(f"\n\"{password}\" was not found.\nYou may keep using it for now.\n")

    
def request_api_data(query_chars):
    """Provide a hast to password API and get response"""
    
    url = f"{PASSWORD_API_ENDPOINT}{query_chars}"
    res = requests.get(url)
    
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching Password. Returned HTTP Status code is {res.status_code}")
    
    else:
        return res

def read_response(response):
    """Read Received Response"""
    
    return response.text

def get_password_leaks_counts(hashes, hash_to_check):
    """Get how many times our hash was leaked"""
    
    hashes = (line.split(":") for line in hashes.splitlines())
    
    for h, count in hashes:
        
        if h == hash_to_check:
            return count
    
    else: 
        return 0

def pwned_api_check(password):
    """Check if password exists in API Response"""
    
    sha1_pass = sha1(password.encode("UTF-8")).hexdigest().upper()
    first_5_chars, tail = sha1_pass[:5], sha1_pass[5:]
    
    response = request_api_data(first_5_chars)
    
    # Get hashes
    hashes = read_response(response)
    
    return get_password_leaks_counts(hashes, tail)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))