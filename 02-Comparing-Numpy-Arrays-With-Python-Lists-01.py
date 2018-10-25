# Importing libraries
import numpy as np
import time

# Numpy arrays
A = np.random.randn(10000000)
B = np.random.randn(10000000)

# Python lists
C = range(10000000)
D = range(10000000)

# Storing time 
TIME_NP = 0
TIME_LT = 0

# For storing the result
RESULT = 0

# Starting timer
tic = time.time()

# Calculating using np.dot method
RESULT = np.dot(A,B)

# Stopping timer
toc = time.time()

# Storing the time
TIME_NP = toc-tic

# Starting the timer
tic = time.time()

# Calculating using loop
for i in range(len(C)):
  RESULT += C[i] * D[i]
  
# Stopping the timer
toc = time.time()

# Storing the timer
TIME_LT = toc-tic

# Printing the result
print(TIME_NP)
print(TIME_LT)