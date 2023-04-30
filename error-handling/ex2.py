# Error Handling Example 2

def divide(n1, n2):
    
    try:
        return n1 / n2
    except (TypeError, ZeroDivisionError) as e:
        print(f'Please enter a valid number: {e}')

print(divide(10, 0))