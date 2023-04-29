# reduce example

# reduce(action, list, accumulator_var)

# Return a single result from performing the same operation to all elements of a list
from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9,10]

def incrementor(acc, item):
    return acc + item

result = reduce(incrementor, my_list, 20)
print(result)