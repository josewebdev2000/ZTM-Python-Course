# map() function

# map(action, list)

# Loop through each element in given list and perform operation on them

original_ints = [1,2,3,4,5]

def double_num(num):
    return num * 2

doubled_nums = list(map(double_num, original_ints))
print(doubled_nums)
