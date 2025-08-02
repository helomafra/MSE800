# Week1- Activity 3: Temperature Analysis Using Python and NumPy
# Develop a Python project to perform the following tasks:
# Calculate and print the average temperature for the week using NumPy.
# Temperature data (in °C): [18.5, 19, 20, 25.0, 2, 30, 13.9]
# Determine and display the highest and lowest recorded temperatures.
# Convert all temperatures to Fahrenheit and print the converted values.
# (Use the formula: F = C × 9/5 + 32)
# Identify and print the indices of days where the temperature exceeded 20°C.
 
import numpy as np

temperature = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# Find the highest and lowest recorded temperatures
max_temp = np.max(temperature)
min_temp = np.min(temperature)
print(f"Max temperature: {max_temp}°C")
print(f"Min temperature: {min_temp}°C")

# Convert to Fahrenheit 
temperature_fahrenheit = temperature * 9/5 + 32
print(f"Temperatures in Fahrenheit: {temperature_fahrenheit}")

# Find indices where temperature exceeded 20°C
# Side note: I need the [0] because np.where returns a tuple of arrays. As this is a 1d array, I need the [0] to get the first (and only) array from the tuple.
indices_above_20 = np.where(temperature > 20)[0]
print(f"Days with temperature above 20°C: {indices_above_20}")


