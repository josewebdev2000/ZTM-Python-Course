"""
Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

Hints:

Use int() to convert a string to integer.
"""

def main():
    
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    
    print(f"The sum of {a} and {b} is {add_from_str(a, b)}")

def add_from_str(ns1, ns2):
    
    return int(ns1) + int(ns2)

if __name__ == "__main__":
    main()