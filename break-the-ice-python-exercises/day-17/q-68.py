"""
Question:

    Please generate a random float where the value is between 10 and 100 using Python module.


Hints:

    Use random.random() to generate a random float in [0,1].

"""

from random import uniform

def main():
    
    random_float = uniform(10, 100)
    print(f"A random number between 10 and 100: {random_float}")

if __name__ == "__main__":
    main()