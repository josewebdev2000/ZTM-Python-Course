# List Comprehension

# le_list = [param for param in iterable]
# le_list = [param for param in iterable if condition else opposite_condition]

# Fill up lists in one statement

def main():
    
    no_list_c()
    print()
    list_c()
    print()
    list_c_challenge()

def no_list_c():
    """Traditional way to fill up a list."""
    
    my_list = []
    
    for char in 'hello':
        my_list.append(char)
    
    print(f"Traditional way: {my_list}")

def list_c():
    
    my_list = [char for char in 'hello']
    print(f"List Comprehension: {my_list}")

def list_c_challenge():
    my_list = [char for char in 'hello']
    my_list2 = [num for num in range(0,100)]
    my_list3 = [num * 3 for num in my_list2]
    my_list4 = [num for num in my_list3 if num % 2 == 0]
    
    print(my_list)
    print(my_list2)
    print(my_list3)
    print(my_list4)

if __name__ == "__main__":
    main()
