from array import array

# Lists of limited size
# Take up less memory and perform faster
# Use in case you don't want to use generators
# Need a specific data type to hold
# Makes code work faster 
# Uses less memory

def main() -> None:
    
    arr = array('i', [1,2,3])
    print(arr)
    print(arr[0])

if __name__ == "__main__":
    main()