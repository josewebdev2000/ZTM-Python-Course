from Wizard import Wizard
from Archer import Archer

def main() -> None:
    
    # Create a Wizard and Archer Object
    my_wiz = Wizard("Merlin", 50)
    my_arc = Archer("Robbin", 1000)
    
    # Sign them in
    my_wiz.sign_in()
    my_arc.sign_in()
    
    my_wiz.attack()
    my_arc.attack()

if __name__ == "__main__":
    main()