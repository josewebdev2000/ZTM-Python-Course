

class Rectangle(object):
    
    def __init__(self, width, length):
        
        self.__width = width
        self.__length = length
    
    @property
    def width(self):
        return self.__width
    
    @property
    def length(self):
        return self.__length
    
    @property
    def area(self):
        return self.width * self.length
    