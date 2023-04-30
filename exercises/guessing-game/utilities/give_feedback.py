# Check if a number is greater, equal, or lower to a given number
def check_number(num_to_check: int, standard_num: int) -> str:
    """Check user's guess"""
    
    if num_to_check > standard_num:
        return "H"
    
    elif num_to_check == standard_num:
        return "E"
    
    else:
        return "L"
    