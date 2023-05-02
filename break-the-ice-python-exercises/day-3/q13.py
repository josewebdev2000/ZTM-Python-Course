"""
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""
from functools import reduce

def main() -> None:
    
    # Get input from the user
    user_str = input("Enter some text with letters and numbers: ")
    user_str_ls = [char for char in user_str]
    
    # Get the number of letters
    num_letters = reduce(increment_letter, user_str_ls, 0)
    
    # Get the number of digits
    num_digits = reduce(increment_digit, user_str_ls, 0)
    
    print(f"letters: {num_letters}".upper())
    print(f"digits: {num_digits}".upper())

def increment_letter(acc, item) -> int:
 
    return acc + 1 if item.isalpha() else acc
    
def increment_digit(acc, item) -> int:
    
    return acc + 1 if item.isdigit() else acc

if __name__ == "__main__":
    main()