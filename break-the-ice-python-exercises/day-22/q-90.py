"""
Question:

    Please write a program which count and print the numbers of each character in a string input by console.

    Example: If the following string is given as input to the program:


Hints:

    Then, the output of the program should be:

"""

def main():
    
    string = input("Enter a string: ")
    
    chars = [char for char in string]
    
    unique_chars = set(chars)
    
    for char in sorted(list(unique_chars)):
        print(f"{char}, {chars.count(char)}")

if __name__ == "__main__":
    main()