from PIL import Image
import os
import sys

def main() -> None:
    
    # Get directories for JPG and PNG files
    jpg_dir, png_dir = grab_clargs()
    
    # Create png directory
    create_new_folder(png_dir)
    
    # Convert and transfer images
    convert_n_transfer(jpg_dir, png_dir)

# Grab command line arguments
def grab_clargs():
    """Grab and check command line arguments are appropiate."""
    
    try:
        old, new = sys.argv[1], sys.argv[2]
        
        # If old is not an existing directory, raise a FileNotFoundError
        if not os.path.exists(old):
            raise FileNotFoundError(f"The specified JPG directory {old} does not exist")
        
        # Delete backlash character from both old and new
        if "\\" in old:
            old = old.rstrip("\\")
        
        if "\\" in new:
            new = new.rstrip("\\")
        
    except IndexError:
        print("Enter two command line arguments")
    
    except FileNotFoundError as e:
        print(e)
        
    else:
        return old, new

# Check new folder does not exist, in that case create it
def create_new_folder(foldername) -> None:
    if not os.path.exists(foldername):
        os.mkdir(foldername)

# Check a file is a jpg file
def is_jpg(filename):
    _, extension = os.path.splitext(filename)
    return extension.lower() in ('.jpg', '.jpeg')

# Loop through all images in the old folder, convert them to PNG and save them in the new folder
def convert_n_transfer(old, new):
    """Convert all images in the old folder to PNG and transfer them to the PNG folder."""
    
    # Get all files in the old folder
    for file in os.listdir(old):
        
        # If the file is JPG image, convert it to PNG and save it to the new folder
        if is_jpg(file):
            
            # Open the JPG image
            img = Image.open(os.path.join(old, file))
            
            # Change color mode to RGBA to preserve alpha channel
            img = img.convert("RGBA")
            
            # Create new transparent background for the new image
            new_png = Image.new("RGBA", img.size, (255, 255, 255, 0))
            
            # Paste the old image into the new image
            new_png.paste(img, img)
            
            # Save the new image in the new folder
            purefilename, _ = os.path.splitext(file)
            new_png.save(os.path.join(new, f"{purefilename}.png"),"png")
            
            # Close file streams for both images
            img.close()
            new_png.close()
            
    # Print success message
    print(f"PNG images from {old} folder have been successfully generated in {new}")


if __name__ == "__main__":
    main()