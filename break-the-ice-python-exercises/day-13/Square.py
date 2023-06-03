from Shape import Shape

class Square(Shape):
    
    def __init__(self, length):
        
        self.__length = length
    
    @property
    def length(self):
        return self.__length
    
    @property
    def area(self):
        return self.length ** 2