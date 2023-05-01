# Image Example 3
from PIL import Image
from ex1 import POKEMON_PICS_DIR
import os

def main() -> None:
    
    img = Image.open(os.path.join(POKEMON_PICS_DIR, "astro.jpg"))
    
    # The thumbnail() method resizes the current image and keeps the aspect ratio
    img.thumbnail((400,400))
    img.save(os.path.join(POKEMON_PICS_DIR, "new_astro.png"), "png")

if __name__ == "__main__":
    main()