# Example IO 2

# Writing to files

def main() -> None:
    
    append_to_file()
    read_n_write()
    create_n_write()

def create_n_write():
    
    with open("sad.txt", "w") as f:
        f.write(":(")
        
def read_n_write():
    
    with open("test.txt", mode="r+") as f:
        text = f.write("Hey it's me")
        print(text)
        print(f.readlines())

def append_to_file():
    
    with open("test.txt", mode="a") as f:
        text = f.write("\nI am the best")
        print(text)
        

if __name__ == "__main__":
    main()