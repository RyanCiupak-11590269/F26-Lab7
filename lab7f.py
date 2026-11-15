# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Ryan Ciupak
# Date: Nov 14, 2026
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

import pandas as pd  

# TODO 1: Create dataframe from provided dictionaries in readme.md file.
# - Create a datatable from the three dictionaries provided in the README

data = [
    {"Apple" : "Green", "Carrot": "Red", "Radish": "Purple"},
    {"Okra": "Thin", "Potato": "blob", "Radish": "Round"},
    {"Apple": 2.1, "Okra": 3.5, "Carrot": 1.3, "Potato": 2.0, "Radish": 3.0}]
dataframe = pd.DataFrame(data)
print(dataframe)

# TODO 2: Create a data frame provided in dataframe.jpg file.

marks = pd.DataFrame({"Student Name" : pd.Series(["A", "B", "C", "D"], ["Maths", "English", "Urdu", "Science"]), 
         "Student Marks" : pd.Series([22, 344, 55, 77], ["Maths", "English", "Urdu", "Science"])})
print(marks)