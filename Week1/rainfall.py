# Week1- activity 4: Rainfall Analysis with NumPy
# Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

# Tasks: 
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
# Share your GitHub link on Teams when you have done.
 
import numpy as np

# Convert the list to a NumPy array and print it.
rainfall = np.array([0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5])
print(rainfall)

# Print the total rainfall for the week.
total_rainfall = np.sum(rainfall)
print(f"Total rainfall: {total_rainfall} mm")

# Print the average rainfall for the week.
average_rainfall = np.mean(rainfall)
print(f"Average rainfall: {average_rainfall} mm")

# Count how many days had no rain (0 mm).
no_rain_days = np.sum(rainfall == 0)
print(f"Days with no rain: {no_rain_days}")

# Print the days (by index) where the rainfall was more than 5 mm.    
more_than_5_mm = np.where(rainfall > 5)[0]
print(f"Days with rainfall more than 5 mm: {more_than_5_mm}")