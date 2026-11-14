# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: November 11, 2026
# Purpose: Create Arrays.
# Usage: ./lab7a.py

import numpy as np  

numbers = (20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49)

array1 = np.array(numbers)

array2 = np.arange(20,50,1)

array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

array4 = np.array(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]).reshape(2,3,2)

print(array1)
print(array2)
print(array3)
print(array4)
