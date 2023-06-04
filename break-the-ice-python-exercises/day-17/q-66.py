"""
Question:

    Please write a program which accepts basic mathematic expression from console and print the evaluation result.

    Example: If the following n is given as input to the program:

        35 + 3

    Then, the output of the program should be:

        38

Hints:

    Use eval() to evaluate an expression.

"""

def main():
    
    math_ex = input("Please enter an arithmetic operation: ")
    
    print(eval(math_ex))

if __name__ == "__main__":
    main()