"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

def main() -> None:
    
    nums_l, nums_t = get_num_seq()
    
    print(nums_l)
    print(nums_t)
    

def get_num_seq() -> "tuple[list, tuple]":
    """Return a string of comma separated numbers from the user"""
    
    got_error = True
    
    while got_error:
    
        try:
            num_seq = input("Enter a comma separated sequence of integers: ")
            nums = [num for num in num_seq.split(",")]
        
        except ValueError:
            print("\nRemember to enter a comma separated sequence of numbers")
            print("Example: 2,4,6,8,10")
            print("Try again\n")
        
        else:
            got_error = False
            
    return nums, tuple(nums)
        

if __name__ == "__main__":
    main()