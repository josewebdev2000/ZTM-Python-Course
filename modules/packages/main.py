# Import code from a python file (module)
import utility

# Import code from a folder (package)
from shopping import shopping_cart

def main() -> None:
    utility.useful()
    print(shopping_cart.buy(2))
    

if __name__ == "__main__":
    main()