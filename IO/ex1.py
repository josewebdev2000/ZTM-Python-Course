# IO Example

# Ways to read files in Python

def main() -> None:
    cursor_move()
    read_by_line()
    read_file_lines()

def read_by_line() -> None:
    
    tf = open("test.txt")
    print(tf.readline())
    tf.close()

def read_file_lines() -> None:
    tf = open("test.txt")
    print(tf.readlines())
    tf.close()

def cursor_move() -> None:
    """Show example of how to move file cursor with Python"""
    
    tf = open("test.txt")
    
    print(tf.read())
    # Move cursor to the first line
    tf.seek(0)
    
    print(tf.read())
    tf.seek(0)
    
    print(tf.read())
    tf.close()

if __name__ == "__main__":
    main()