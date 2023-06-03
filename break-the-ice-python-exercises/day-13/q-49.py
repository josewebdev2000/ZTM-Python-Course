"""
Question:

    Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
    Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

    To override a method in super class, we can define a method with the same name in the super class.

"""
from Shape import Shape
from Square import Square

def main():
    
    my_shape = Shape()
    my_square = Square(5)
    
    print(f"Area of my shape: {my_shape.area}")
    print(f"Area of my square: {my_square.area}")

if __name__ == "__main__":
    main()