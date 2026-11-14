# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Nov 14, 2026
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

import numpy as np  

# TODO 1: Copy the code from your lab7a.py file and paste here.

numbers = (20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49)

array1 = np.array(numbers)

array2 = np.arange(20,50,1)

array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

array4 = np.array(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]).reshape(2,3,2)

# TODO 2: Reshape array 1 into a 5x6 shape.   

array1 = np.array(numbers).reshape(5,6)

# TODO 3: Reshape array 2 into a 2x3x5 matrix

array2 = np.arange(20,50,1).reshape(2,3,5)

# TODO 4: Create array5 according to instructions given in README.md file.
# - Create a matrix that has 5 rows and 5 columns and initialize diagonal values to (45, 7, 61, 8, 9).  The rest of the values should be zeros

array5 = np.diag((45, 7, 61, 8, 9))

# TODO 5: Create array6 according to instructions given in README.md file.
# - Create a 7x7 matrix and initialize with values sampled from a normal distribution

array6 = np.random.randn(7,7)

print(array1)
print(array2)
print(array5)
print(array6)

