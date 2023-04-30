"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""
def main() -> None:
    
    # Get factorials of numbers 1 to 10 with 10 included
    factorials = [str(factorial(num)) for num in range(1, 10 + 1)]
    print(",".join(factorials))

def factorial(num: int) -> int:
    
    if num == 1:
        return 1
    
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":
    main()