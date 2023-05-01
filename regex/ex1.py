import re

def main() -> None:
    
    sentence = "Search inside of this text please!"

    a = re.search("this", sentence)
    
    print(a.span())

if __name__ == "__main__":
    main()