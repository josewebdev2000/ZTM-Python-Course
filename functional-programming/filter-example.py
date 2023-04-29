# filter() function

# filter(filtering_func, list)

# Get a checker function and loop through a list and return a list with elements that pass the check

def check_even(num):
    return num % 2 == 0

nums = [1,2,3,4,5,6,7,8,9,10]

even_nums = list(filter(check_even, nums))
print(even_nums)