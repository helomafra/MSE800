def factorial(number):
  result = 1
  if number < 0: 
    print("Error: number must be positive!")
    return
  elif number == 0: 
    print("Factorial of 0 is 1")
    return result
  elif number == 1:
    print("Factorial of 1 is 1")
    return result
  else: 
    for i in range(1, number + 1):
      result = result * i
    return result

if __name__ == "__main__":
  number = input("Enter a number:")
  number = int(number)
  result = factorial(number)
  print(f"Factorial of {number} is {result}")
