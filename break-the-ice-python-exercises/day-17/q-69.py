"""
Question:

    Please generate a random float where the value is between 5 and 95 using Python module.

Hints:

    Use random.random() to generate a random float in [0,1].

"""

from random import uniform

def main():
    
    print(f"A random number between 5 and 95: {uniform(5, 95)}")

if __name__ == "__main__":
    main()