"""
Question:

    Define a class named American and its subclass NewYorker.

Hints:

    Use class Subclass(ParentClass) to define a subclass.*

"""

from American import American
from NewYorker import NewYorker

def main():
    
    print("American Nationality: ")
    American.printNationality()
    
    print("New Yorker Nationality: ")
    NewYorker.printNationality()
    NewYorker.printState()

if __name__ == "__main__":
    main()