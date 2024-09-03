import numpy as np
from scipy.stats import skew, kurtosis

data = [4, 8, 15, 16, 23, 42]
mean = np.mean(data)
print(f"Mean: {mean}")

# Calculating the variance
variance = np.var(data)
print(f"Variance: {variance}")

# Calculating the skewness
skewness = skew(data)
print(f"Skewness: {skewness}")

kurtosis_value = kurtosis(data)
print(f"Kurtosis: {kurtosis_value}")
