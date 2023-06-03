"""
Question:

    Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
    
    
Hints:

    Use unicode()/encode() function to convert.

"""
def main():
    
    ascii_str = input("Enter some ASCII text: ")
    
    utf_8_version = ascii_str.encode("utf-8")
    
    print(utf_8_version)

if __name__ == "__main__":
    main()