"""
Question:

    Please write a binary search function which searches an item in a sorted list. 
    The function should return the index of element to be searched in the list.

Hints:

    Use if/elif to deal with conditions.

"""

def main():
    
    nums = tuple(range(1, 500 + 1))
    
    print(binary_search(nums, 240))
    print(binary_search(nums, -50))

def binary_search(sorted_list, element):
    """Return the index of the requested element in the list."""
    
    # Find first and last elements of the list
    first_index = 0
    last_index = len(sorted_list) - 1
    
    index_to_look_for = None
    
    # Condition to keep looking for the number
    while last_index >= first_index and index_to_look_for == None:
        
        # Find index of item at the middle of the array
        middle_index = (first_index + last_index) // 2
        
        # If the item at the middle is equal to the element, then the middle index is the
        # Index we're looking for
        if sorted_list[middle_index] == element:
            index_to_look_for = middle_index
        
        # In case the item at the middle is greater than the element we're looking for
        # cut of the half of the list that is greater than the middle index
        elif sorted_list[middle_index] > element:
            last_index = middle_index - 1
        
        # In case the item at the middle is lower than the element we're looking for
        # cut of the half of the list that is lower than the middle index
        else:
            first_index = middle_index + 1
    
    return index_to_look_for    
        

if __name__ == "__main__":
    main()