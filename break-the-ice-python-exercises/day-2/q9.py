"""
    Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

    Suppose the following input is supplied to the program:
    
    Hello world
    Practice makes perfect
    
    HELLO WORLD
    PRACTICE MAKES PERFECT

"""
from typing import Callable

def main() -> None:
    
    # Get the number of lines desired by the user
    num_lines = get_int()
    
    # Let the user write those lines
    line_seq = get_line_seq(num_lines)
    
    # Uppercase all lines 
    up = upper_lines(line_seq)
    
    print("\n\n")
    
    # print lines to the console
    print("\n".join(up))

def stdin_checker(stdin_fn) -> Callable:
    """Function that handles errors for functions that require data from STDIN."""
    
    def wrapper(*args, **kwargs) -> object:
        
        got_error = True
        
        while got_error:
            
            try:
                result = stdin_fn(*args)
            
            except Exception as e:
                print(f"\nAn error occured: {e}")
                print("Please, try again\n")
                break
            
            else:
                got_error = False
                return result
    
    return wrapper     
        
@stdin_checker
def get_int() -> int:
    """Get an integer from STDIN."""
    
    return int(input("Please enter the number of lines to type: "))

@stdin_checker
def get_line_seq(num_lines) -> list:
    """Get a sequence of lines from STDIN"""
    
    return [input("Enter a sentence: ") for _ in range(num_lines)]

def upper_lines(line_seq) -> list:
    """Uppercase all letters in a list of strings"""
    
    return [line.upper() for line in line_seq]
    

if __name__ == "__main__":
    main()