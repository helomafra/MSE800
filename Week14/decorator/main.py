# Week 14 - activity 2: Create a Decorator to Measure Execution Time
# Develop a Python project that uses the "time.sleep" method together with a decorator 
# to measure a function's execution time. Share your understanding via GitHub and explain 
# why we have used decorators and when we need to use them in your code as a comment.

import time

# WHAT IS A DECORATOR?
# A decorator is a function that modifies or extends the behavior of another function
# without changing the original function's code. It's like "wrapping" a function with extra functionality.


# WHEN TO USE DECORATORS?
# - Measure execution time (like in this example)
# - Log function calls
# - Validate input parameters
# - Cache results of expensive functions
# - Add authentication/authorization
# - Count how many times a function was called


def measure_time(func):
    """
    Decorator that measures the execution time of a function.
    
    This decorator:
    1. Captures the time before the function executes
    2. Executes the original function
    3. Captures the time after
    4. Calculates and displays the difference
    """
    def wrapper(*args, **kwargs):
        # Record the time BEFORE executing the function
        start_time = time.time()
        
        # Execute the original function with its arguments
        result = func(*args, **kwargs)
        
        # Record the time AFTER executing the function
        end_time = time.time()
        
        # Calculate the elapsed time
        execution_time = end_time - start_time
        
        # Display the result
        print(f"⏱️  The function '{func.__name__}' took {execution_time:.2f} seconds to execute")
        
        # Return the result of the original function
        return result
    
    return wrapper


# Applying the decorator using the @ syntax
# This is equivalent to writing: slow_function = measure_time(slow_function)
@measure_time
def slow_function(seconds):
    """
    Simple function that simulates a time-consuming operation using time.sleep
    """
    print(f"💤 Sleeping for {seconds} seconds...")
    time.sleep(seconds)  # Pauses execution for the specified number of seconds
    print("✅ Woke up!")
    return f"Function completed after {seconds} seconds"


@measure_time
def another_function():
    """
    Another example of a function that uses the decorator
    """
    print("🔄 Processing data...")
    time.sleep(1.5)
    print("✅ Data processed!")
    return "Success"


# Main function to demonstrate usage
def main():
    print("=" * 50)
    print("Decorator Demo: Measuring Execution Time")
    print("=" * 50)
    print()
    
    # Test 1: Function that sleeps for 2 seconds
    print("Test 1:")
    result1 = slow_function(2)
    print(f"Result: {result1}")
    print()
    
    # Test 2: Function that sleeps for 1.5 seconds
    print("Test 2:")
    result2 = another_function()
    print(f"Result: {result2}")
    print()
    
    print("=" * 50)


if __name__ == "__main__":
    main()
