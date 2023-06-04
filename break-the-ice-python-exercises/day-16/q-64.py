"""
Question:

    Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

    Example: If the following n is given as input to the program:

    100

    Then, the output of the program should be:

    0,35,70

    In case of input data being supplied to the question, it should be assumed to be a console input.


Hints:

    Use yield to produce the next value in generator.

"""
def main():
    
    num = int(input("Enter a number: "))
    
    num_range = range(0, num + 1)
    
    divisible_range = tuple(str(n) for n in num_range if n % 35 == 0)
    
    print(",".join(divisible_range))

if __name__ == "__main__":
    main()