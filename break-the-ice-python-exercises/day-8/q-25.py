"""
Question:

    Define a class, which have a class parameter and have a same instance parameter.
    
Hints:

Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later
"""

class SomeClass:
    """Class to solve this challenge."""
    
    def __init__(self, some_data = None):
        
        self.some_data = some_data

def main():
    
    # Give the value as a parameter
    some_class = SomeClass("some value")
    
    print(some_class.some_data)
    
    # Give value later
    some_other_class = SomeClass()
    some_other_class.some_data = "some other value"
    print(some_other_class.some_data)

if __name__ == "__main__":
    main()