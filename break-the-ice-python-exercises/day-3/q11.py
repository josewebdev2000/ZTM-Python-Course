"""
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001

Then the output should be:

1010

Notes: Assume the data is input by console.
"""

def main() -> None:
    
    # Get sequence of comma separated binary numbers
    bin_nums = input("Enter sequence of 4 digit binary numbers separated by a comma: ").split(",")
    
    # Convert all binary numbers to decimal numbers divisible by 5
    bin_nums = [str(bin(int(num, 2)))[2:] for num in bin_nums if int(num, 2) % 5 == 0]
    
    # print comma separated list of resultant nums
    print(",".join(bin_nums))

if __name__ == "__main__":
    main()