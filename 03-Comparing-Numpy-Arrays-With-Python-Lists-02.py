# Importing libraries
import numpy as np
import time
import sys


# Python list
S = range(1000)

# Numpy array
D = np.arange(1000)


# Printing the results
print(sys.getsizeof(S)*len(S))
print(D.size*D.itemsize)