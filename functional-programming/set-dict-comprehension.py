# Set and Dictionary Comprehension

# Set Comprehension works the same way as list comprehension
# Dict Comprehension works like:

# my_dict = {key:value for key, value in zip(iter1, iter2)} when iter1 and iter2 are not dicts
# my_dict = {key:value for key, value in iter.items()} when iter is dict

def main():
    
    set_c()
    print()
    dict_c()

def set_c():
    
    my_set = {n for n in range(10)}
    my_set2 = {n for n in my_set if n % 2 != 0}
    
    print(my_set)
    print(my_set2)

def dict_c():
    
    nums = [num for num in range(1,10 + 1)]
    triple_nums = [num * 3 for num in nums]
    
    num_n_triple = {num : triple for num, triple in zip(nums, triple_nums)}
    print(num_n_triple)
    
    even_num_triple = {num : triple for num, triple in num_n_triple.items() if num % 2 == 0}
    print(even_num_triple)

if __name__ == "__main__":
    main()