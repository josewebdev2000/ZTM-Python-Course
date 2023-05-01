"""
    Write a program that calculates and prints the value according to the given formula:

    Q = Square root of [(2CD)/H]

    Following are the fixed values of C and H:

    C is 50. H is 30.

    D is the variable whose values should be input to your program in a comma-separated sequence.
    For example Let us assume the following comma separated input sequence is given to the program:
    
    100,150,180

    The output of the program should be:
    
    18,22,24

"""

import math

C = 50
H = 30

def main() -> None:
    
    d_values = get_num_seq()
    results = list(map(formula_result, d_values))
    results_str = ",".join(results)
    print(results_str)

def formula_result(d_value) -> str:
    """Get value from the formula (2CD)/H"""
    
    ex1 = 2 * C * d_value
    ex2 = ex1 / H
    ex3 = int(math.sqrt(ex2))
    return str(ex3)

def get_num_seq() -> list:
    """Return a string of comma separated numbers from the user"""
    
    got_error = True
    
    while got_error:
    
        try:
            num_seq = input("Enter a comma separated sequence of numbers: ")
            nums = [float(num) for num in num_seq.split(",")]
        
        except ValueError:
            print("\nRemember to enter a comma separated sequence of numbers")
            print("Example: 2,4,6,8,10")
            print("Try again\n")
        
        else:
            got_error = False
            
    return nums  

if __name__ == "__main__":
    main()