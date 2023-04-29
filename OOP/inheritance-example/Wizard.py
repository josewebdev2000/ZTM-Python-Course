from User import User

class Wizard(User):
    
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"Attacking with the power of {self.power}")