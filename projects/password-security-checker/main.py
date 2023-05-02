import requests
from constants import PASSWORD_API_ENDPOINT

def main() -> None:
    
    url = PASSWORD_API_ENDPOINT + "password123"
    res = requests.get(url)
    print(res)

if __name__ == "__main__":
    main()