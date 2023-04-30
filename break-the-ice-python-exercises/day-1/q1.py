"""
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def main() -> None:
    
    # List of all numbers divisible by 7 and not by 5 from 2000 to 3200
    nums = [str(num) for num in range(2000, 3200 + 1) if num % 7 == 0 and num % 5 != 0]
    
    # Print numbers as a string of comma separated values
    nums_str = ",".join(nums)
    
    print(nums_str)

if __name__ == "__main__":
    main()