class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cats = (Cat("Whiskers", 5), Cat("Mittens", 6), Cat("Simba", 2))


# 2 Create a function that finds the oldest cat
def get_oldest_cat(cats):
    
    oldest_age = 0
    curr_cat = None
    
    for cat in cats:
        if cat.age > oldest_age:
            oldest_age = cat.age
            curr_cat = cat
    
    return curr_cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest_cat = get_oldest_cat(cats)
print(f"The oldest cat is {oldest_cat.age} years old.")