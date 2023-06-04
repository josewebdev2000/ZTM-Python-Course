"""
Question:

    Write a program to compute:

    f(n)=f(n-1)+100 when n>0
    and f(0)=0

    with a given n input by console (n>0).

    Example: If the following n is given as input to the program:

    5

    Then, the output of the program should be:

    500

    In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

    We can define recursive function in Python.

"""

def main():
    
    num = int(input("Enter a number to start the sequence: "))
    
    print(get_sum_f_minus_1_plus_100(num))

def get_sum_f_minus_1_plus_100(n):
    
    if n == 0:
        return 0
    
    else:
        return get_sum_f_minus_1_plus_100(n - 1) + 100

if __name__ == "__main__":
    main()