"""
Question

    Given a number N.Find Sum of 1 to N Using Recursion

Input

    5

Output

    15

Hints

    Make a recursive function to get the sum
"""
def main():
    
    n = int(input("Enter a number: "))
    print(recursive_sum(n))
    

def recursive_sum(n):
    
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

if __name__ == "__main__":
    main()