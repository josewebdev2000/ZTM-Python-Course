"""
    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

    Suppose the following input is supplied to the program:

    9

    Then, the output should be:

    11106

"""

def main() -> None:
    
    # Get number from STDIN
    num = input("Enter a number: ")
    
    # Get a total of 0
    total = 0
    
    # Loop 4 times to get repeated versions of the number
    for i in range(1, 4 + 1):
        
        curr_num = num * i
        total += int(curr_num)
    
    # Show result to STDOUT
    print(total)

if __name__ == "__main__":
    main()