"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def main() -> None:
    
    num_range = range(1000, 3000 + 1)
    special_nums = each_digit_even(num_range)
    print(",".join(special_nums))

def each_digit_even(num_range):
    """Return a list of numbers such that each digit is an even number"""
    
    each_digit_even_num = []
    
    for num in num_range:
        num = str(num)
        
        all_digits_even = True
        
        for char in num:
            char = int(char)
            
            if char % 2 != 0:
                all_digits_even = False
            
        
        if all_digits_even:
            each_digit_even_num.append(num)
    
    return each_digit_even_num

if __name__ == "__main__":
    main()