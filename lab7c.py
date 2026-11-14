# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Nov 14, 2026
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np  # Step 1: Import NumPy

# TODO 1: Create numArray according to instructions given in README.md file.
# - Create a 1D array numArray and initialize it with 100 random numbers

numArray = np.random.rand(100)

# TODO 2: Perform the follow operations on numArray as seen in README.md file.
# - Slice and print first 10 values

print(numArray[0 : 10])

# - Slice and print last 10 values

print(numArray[-10 :])

# - Slice and print 30 values starting from index 21

print(numArray[20 : 50])

# - With one statement, change all values to 101 from index 50 to 65.

numArray[50 : 65] = 101
print(numArray[49 : 70])