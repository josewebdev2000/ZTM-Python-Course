"""
    Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

    Suppose the following input is supplied to the program:

7

    Then, the output should be:

0
7
14

Hints:

    Consider use class, function and comprehension.
"""

class MultiplesOf7Gen():
    
    def __init__(self, last):
        self.last = last
    
    def generate_nums(self):
        
        for i in range(self.last + 1):
            
            if i % 7 == 0:
                yield i

def main() -> None:
    
    # Grab number from the user
    num = int(input("Enter a number: "))
    
    # Make a range for all multiples of 7 from 0 to 7
    multiples_7_gen = MultiplesOf7Gen(num)
    
    for i in multiples_7_gen.generate_nums():
        print(i)

if __name__ == "__main__":
    main()