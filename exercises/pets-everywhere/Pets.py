class Pets:
    
    animals = []
    
    def __init__(self, animals):
        self.animals = animals
    
    def walk(self):
        for animal in self.animals:
            print(animal.walk())