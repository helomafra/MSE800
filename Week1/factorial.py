# Week1- Activity 1: Calculate the Factorial of a Number Using a Loop
 
# Develop the first project for MSE800 with using following task:
# What happens if the user enters 0? Try to handle this case in your code.
# Try adding error checking for negative numbers.
 
def factorial(number):
  result = 1
  if number == 0: 
    return result
  if number == 1:
    return result
  else: 
    for i in range(1, number + 1):
      result = result * i
    return result

def get_valid_input():
  while True:
    try:
      number = int(input("Enter a number: "))
      if number < 0:
        print("Error: number must be positive!")
        continue
      return number
    except ValueError:
      print("Error: Invalid input. Please enter a valid integer number.")

if __name__ == "__main__":
  number = get_valid_input()
  result = factorial(number)
  print(f"Factorial of {number} is {result}")
