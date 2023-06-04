"""
Question:
    Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
    Use zlib.compress() and zlib.decompress() to compress and decompress a string.
"""

import zlib

def main():
    
    some_string = "hello world!hello world!hello world!hello world!"
    some_string = bytes(some_string, "utf-8")
    compressed_string = zlib.compress(some_string)
    
    print(compressed_string)
    
    print(zlib.decompress(compressed_string))
if __name__ == "__main__":
    main()