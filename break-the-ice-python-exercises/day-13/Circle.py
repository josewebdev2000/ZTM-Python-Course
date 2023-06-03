from math import pi

class Circle(object):
    
    def __init__(self, radius):
        
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def area(self):
        return pi * self.radius ** 2