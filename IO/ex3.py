# Example IO 3
import io
# IO Error Handling

def main() -> None:
    
    try:
        with open("sad.txt", mode="r") as f:
            print(f.read())
    
    except FileNotFoundError:
        print("File does not exist")
    
    except IOError:
        print("IO Error from the OS")

if __name__ == "__main__":
    pass