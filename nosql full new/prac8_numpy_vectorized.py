# PRACTICAL 8 - Vectorized processing using NumPy
# Install if required: pip install numpy

import numpy as np

# Example 1: vectorized addition
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

result = a + b

print("Array A:", a)
print("Array B:", b)
print("Result:", result)


# Example 2: marks processing without any loop
marks = np.array([45, 60, 72, 85, 90])

new_marks = marks + 5
percentage = new_marks / 100 * 100
passed = new_marks >= 50

print("Original Marks:", marks)
print("Marks after Bonus:", new_marks)
print("Percentage:", percentage)
print("Passed:", passed)

print("Average Marks:", np.mean(new_marks))
print("Highest Marks:", np.max(new_marks))
