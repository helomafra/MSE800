# Week 1- Activity2: Sum of Even Numbers
# Write a Python program to calculate the sum of all positive even numbers between 1 and a given number n (inclusive). Share your GitHub link here when you have done.
 
# Rewrite the program using a while loop.
# Also modify it to find the sum of positive odd numbers instead. Print all even numbers as well as the total sum.

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

def get_sum_of_even_numbers(number):
  sum = 0
  i = 1
  while (i <= number):
    if i % 2 == 0:
      sum += i
      print(f"Even number: {i}")
    i += 1
  return sum

def get_sum_of_odd_numbers(number):
  sum = 0
  i = 1
  while (i <= number):
    if i % 2 != 0:
      sum += i
      print(f"Odd number: {i}")
    i += 1
  return sum

if __name__ == "__main__":
  number = get_valid_input()
  result_even = get_sum_of_even_numbers(number)
  result_odd = get_sum_of_odd_numbers(number)
  print(f"The sum of even numbers between 1 and {number} is {result_even}")
  print(f"The sum of odd numbers between 1 and {number} is {result_odd}")