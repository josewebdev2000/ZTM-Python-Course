# @classmethod and @staticmethod

class PlayerCharacter:
    
    membership = True
    
    # Make a method that belongs to the class but not the instance "object"
    # cls stands for class
    @classmethod
    def add_stuff(cls, num1, num2):
        # Return a object of class PlayerCharacter
        return cls("Teddy", num1 + num2)
    
    # No access to class state
    @staticmethod
    def sub_stuff(num1, num2):
        return num1 - num2
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def shout(self):
        print(f"My name is {self.name}")

# May use class method without initializing object
pl = PlayerCharacter.add_stuff(7, 10)

# Initialize object
player1 = PlayerCharacter("Tom", 20)

# Object has instance to class method
player2 = player1.add_stuff(5, 7)

# Object has no access to static methods
print(PlayerCharacter.sub_stuff(5, 3))

