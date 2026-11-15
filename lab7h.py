# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Ryan Ciupak
# Date: Nov 14, 2026
# Purpose: Create Histograms.
# Usage: ./lab7h.py

import matplotlib.pyplot as plt
import pandas as pd

imdb = pd.read_csv("imdb_top_250.csv")

years = pd.Series(imdb["Year"])

years = years.sort_values()

unique = years.unique()
count = years.value_counts()

if len(years)>10:
    years = years.head(10)

fig, ax = plt.subplots()
ax.hist(years)
plt.title("Histogram")
plt.xlabel("Year")
plt.ylabel("Number of movies")
plt.savefig("histogram_1.png")

