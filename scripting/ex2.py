# Image Example 2
from PIL import Image
from ex1 import POKEMON_PICS_DIR
import os

def main() -> None:
    
    img = Image.open(os.path.join(POKEMON_PICS_DIR, "charmander.jpg"))
    
    # Convert to black and white and show to the world
    img.convert("L").show()
    
    # Rotate image 90 and save it
    img.rotate(90).show()
    
    # Resize and show image
    img.resize((300,300)).show()
    
    # Crop image to rectangle area and show it
    img.crop((100,100,400,400)).show()

if __name__ == "__main__":
    main()


