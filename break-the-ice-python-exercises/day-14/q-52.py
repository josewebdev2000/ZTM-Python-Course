"""
Question:

    Define a custom exception class which takes a string message as attribute.

Hints:

    To define a custom exception, we need to define a class inherited from Exception.

"""

from SomeError import SomeError

def main():
    
    raise SomeError("Some error took place")

if __name__ == "__main__":
    main()