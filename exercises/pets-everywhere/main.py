from Pets import Pets
from Cat import Cat

def main() -> None:
    
    # Add another cat
    simon = Cat("Simon", 3, "Meow")
    sally = Cat("Sally", 2, "gghrr")
    simba = Cat("Simba", 4, "Hakunna Matata")
    
    # Make a list of all pets
    my_pets = Pets([simon, sally, simba])
    
    # Output all cats walking
    my_pets.walk()

if __name__ == "__main__":
    main()