"""
Define a function that can convert a integer into a string and print it in console.

Hints:

    Use str() to convert a number to string.
"""

def main():
    
    whole_num = int(input("Enter a whole number: "))
    
    print("The string version of your number is " + int_to_str(whole_num))

def int_to_str(num_int):
    return str(num_int)

if __name__ == "__main__":
    main()