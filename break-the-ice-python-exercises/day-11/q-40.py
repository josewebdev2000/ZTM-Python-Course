"""
Question:

    Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:

    Use if statement to judge condition.
"""

def main():
    
    ACCEPTABLE = ("yes", "YES", "Yes")
    
    word = input("Please enter a word: ")
    
    print("Yes") if word in ACCEPTABLE else print("No")

if __name__ == "__main__":
    main()