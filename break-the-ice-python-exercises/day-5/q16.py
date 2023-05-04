"""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
    1,2,3,4,5,6,7,8,9

Then, the output should be:

    1,9,25,49,81
"""

def main() -> None:
    
    nums = input("Enter a comma separated sequence of numbers: ").split(",")
    nums = [int(num) for num in nums if int(num) % 2 != 0]
    
    squared_nums = list(map(get_square, nums))
    squared_nums = [str(num) for num in squared_nums]
    print(",".join(squared_nums))

def get_square(num):
    return num ** 2

if __name__ == "__main__":
    main()