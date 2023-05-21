"""
Question:

    Define a function which can compute the sum of two numbers.

Hints:

    Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
"""

def main():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    
    sum_a_b_ = add_up(a, b)
    
    print(f"The sum of {a} and {b} is {sum_a_b_}")

def add_up(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    main()