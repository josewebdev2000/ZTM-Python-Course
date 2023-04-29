from User import User

class Archer(User):
    def __init__(self, name, arrows_num):
        self.name = name
        self.arrows_num = arrows_num
    
    def attack(self):
        print(f"Attacking with {self.arrows_num} arrows")