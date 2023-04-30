# Take a number from the user that must belong to a given range

def take_num(prompt_message: str) -> int:
    
    got_error = True
    
    while got_error:
        
        try:
            num = int(input(prompt_message))
        
        except TypeError:
            print("You must enter a number\nTry again\n")
        
        else:
            got_error = False
    
    return num

def take_num_range(prompt_message: str,min_num: int, max_num: int) -> int:
    
    got_error = True
    
    while got_error:
        
        try:
            num = int(input(prompt_message))
            
            if isinstance(num, int) or isinstance(num, float):
                if num < min_num or num > max_num:
                    raise ValueError(f"Number must be within the range ({min_num},{max_num})")
        
        except TypeError:
            print("You must enter a number\nTry again\n")
        
        except ValueError as e:
            print(str(e) + "\n")
            print("Try again\n")
        
        else:
            got_error = False
    
    return int(num)
    