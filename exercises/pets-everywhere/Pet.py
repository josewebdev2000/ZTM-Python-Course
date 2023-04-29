class Pet:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        return f"{self.name} is just walking around."