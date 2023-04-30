# Create a generator of Fibonacci sequences
def main():
    
    for num in fib(1, 30):
        print(num)

def fib(start_num, end_num):
    """Fibonacci sequence generator that accpets start number and end number."""
    
    a, b = 0, 1
    
    # Cut it when the first number a is not less than the end_number
    while a < end_num:
        # Only yield if a is greater than or equal to the greatest number
        if a >= start_num:
            yield a
        
        # First number becomes the value of the last second number
        # Second number becomes the value of adding the first number to itself
        a, b = b, a + b

if __name__ == "__main__":
    main() 