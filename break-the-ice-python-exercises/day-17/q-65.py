"""
Question:

    Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:

    Use "assert expression" to make assertion.
"""

def main():
    
    nums = [2,4,6,8]
    
    map(assert_is_even, nums)

def assert_is_even(n):
    assert n % 2 == 0

if __name__ == "__main__":
    main()