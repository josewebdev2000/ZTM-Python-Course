# How to handle images in Python

from PIL import Image, ImageFilter
import os

POKEMON_PICS_DIR = "pokemon_pics"

# PNG images support filters so when you apply filters remember to always use PNG as format

def main() -> None:
    
    image = Image.open(os.path.join(POKEMON_PICS_DIR, "pikachu.jpg"))
    
    save_blurred_img(image)
    save_smoothed_img(image)
    save_sharpen_img(image)
    black_n_white(image)
    
    image.close()

def show_img_props(image):
    """Show some common properties of an image."""
    print(f"Image Format: {image.format}")
    print(f"Image Size: {image.size}")
    print(f"Image Color Mode: {image.mode}")

def save_blurred_img(image):
    """Apply blurry filter to an image."""
    
    filtered_pic = image.filter(ImageFilter.BLUR)
    filtered_pic.save(os.path.join(POKEMON_PICS_DIR, "blurry_pikachu.png"), "png")
    filtered_pic.close()

def save_smoothed_img(image):
    """Apply smooth filter to an image."""
    
    filtered_pic = image.filter(ImageFilter.SMOOTH)
    filtered_pic.save(os.path.join(POKEMON_PICS_DIR, "smooth_pikachu.png"), "png")
    filtered_pic.close()

def save_sharpen_img(image):
    """Apply sharp filter to an image."""
    
    filtered_pic = image.filter(ImageFilter.SHARPEN)
    filtered_pic.save(os.path.join(POKEMON_PICS_DIR, "sharp_pikachu.png"), "png")
    filtered_pic.close()

def black_n_white(image):
    """Make an image black and white."""
    
    filtered_pic = image.convert("L") # Converts image to black and white
    filtered_pic.save(os.path.join(POKEMON_PICS_DIR, "monochromatic_pikachu.png"), "png")
    filtered_pic.close()

if __name__ == "__main__":
    main()