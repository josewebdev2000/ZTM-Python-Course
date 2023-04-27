# Interpret data that comes from STDIN as an integer

birth_year = int(input("What year were you born? "))
current_year = int(input("What year is it? "))

age = current_year - birth_year

print(f"Your age is: {age}")