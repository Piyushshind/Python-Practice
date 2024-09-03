import numpy as np
from scipy import stats

data = [4, 8, 15, 16, 23, 42, 23]

mean = np.mean(data)
print(f"Mean: {mean}")

median = np.median(data)
print(f"Median: {median}")

# Calculating the mode
mode_result = stats.mode(data, keepdims=True)  # `keepdims=True` keeps the result as an array
mode_value = mode_result.mode[0]               
mode_count = mode_result.count[0]             
print(f"Mode: {mode_value} with a count of {mode_count}")
