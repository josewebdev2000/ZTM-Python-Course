"""
Question:

    Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints:

    Use def methodName(self) to define a method.
"""
from Rectangle import Rectangle

def main():
    
    some_rect = Rectangle(4, 7)
    
    print(f"Rectangle Area: {some_rect.area}")

if __name__ == "__main__":
    main()