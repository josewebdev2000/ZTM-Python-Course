from Pet import Pet

class Cat(Pet):
    is_lazy = True
    
    def __init__(self, name, age, sounds):
        super().__init__(name, age)
        self.sounds = sounds
    
    def sing(self):
        return f"{self.sounds}"