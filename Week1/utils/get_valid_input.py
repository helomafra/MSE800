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