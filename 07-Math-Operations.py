import numpy as np

m = np.random.rand(10,10)
n = np.random.rand(10,10)
p = 4.0
q = np.array([[3.5,4.2,3.6]])

# Add two matrices
Result = n + m # Alternatively we can use the np.add function also

# Subtract two matrices
Result = n - m

# Multiplication of two matrices
Result = np.multiply(n,m)

# Dot product of two matrices
Result = np.dot(n,m)

# Inverse of a matrix
Result = np.linalg.inv(n)

# Transpose of a matrix
Result = np.transpose(n) # Alternatively we can use the n.T method also

# Trigonometric Functions
Result = np.sin(n*(np.pi/180))

Result = np.cos(n*(np.pi/180))

# Average
Result = np.average(q)

# Mean
Result = np.mean(q)

# Median
Result = np.median(q)

# Standard Deviation
Result = np.std(q)

# Variance
Result = np.var(q)

# Floor 
Result = np.floor(q)

# Ceil
Result = np.ceil(q)