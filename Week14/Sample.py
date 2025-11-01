# Week 14 - activity 1: Decorator 
# Do the research and briefly explain how the following code works to demonstrate your understanding of the use of a decorator. Then, share your GitHub link and include your explanation as a paragraph comment within your code.
# Sample.py
 

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


# Extend a function without changing its code
@log_decorator
def add(a, b):
    return a + b

add(3, 5)
