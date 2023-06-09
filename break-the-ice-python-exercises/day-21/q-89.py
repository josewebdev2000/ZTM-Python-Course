"""
Question:
    Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
    Use Subclass(Parentclass) to define a child class.
"""
from Male import Male
from Female import Female

def main():
    
    a_man = Male()
    a_woman = Female()
    
    print(f"Masculine Gender: {a_man.getGender()}")
    print(f"Femenine Gender: {a_woman.getGender()}")

if __name__ == "__main__":
    main()