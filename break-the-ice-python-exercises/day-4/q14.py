"""
    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

    Suppose the following input is supplied to the program:

    Hello world!

        Then, the output should be:

    UPPER CASE 1
    LOWER CASE 9

"""
from functools import reduce

def main() -> None:
    
    # Take a sentence from STDIN
    sentence = input("Enter a sentence: ")
    
    # Get number of uppercase letters
    num_upper = reduce(increment_if_upper, sentence, 0)
    
    # Get number of lowercase letters
    num_lower = reduce(increment_if_lower, sentence, 0)
    
    # Show result to STDOUT
    print(f"upper case {num_upper}".upper())
    print(f"lower case {num_lower}".upper())

def increment_if_upper(acc: int, char: str) -> int:
    return acc + 1 if char.isupper() else acc

def increment_if_lower(acc: int, char: str) -> int:
    return acc + 1 if char.islower() else acc

if __name__ == "__main__":
    main()