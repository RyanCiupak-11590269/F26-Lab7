# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Nov 14, 2026
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py

import pandas as pd
import matplotlib.pyplot as plt

imdb = pd.read_csv("imdb_top_250.csv")

summary = imdb.describe()
print(summary)

head = imdb.head(10)
tail = imdb.tail(10)
print(f"The first 10 entries: \n{head}\n The last 10 entries: \n{tail}")

earliest = imdb["Year"].min()
latest = imdb["Year"].max()
print(f"The earliest movie was released: {earliest}\n The latest movie was released: {latest}")

genres = imdb["Genre"].str.split("|").explode().str.strip().unique()
print(f"The different genres are: \n{genres}")

count = (imdb["Origin"] != "USA").sum()
print(f"The number of movies not made in the USA is: {count}")

top_10 = imdb.sort_values(by = "IMDB rating", ascending=False).head(10)
print(f"The top 10 movies are: {top_10}")

def get_decade(year):
    if pd.isna(year):
        return None
    return (int(year // 10) * 10)

imdb["Decade"] = imdb["Year"].apply(get_decade)

ratings = imdb.groupby("Decade")["IMDB rating"].mean()

fig, ax = plt.subplots()
ax.scatter(ratings.index, ratings.values)
plt.savefig("scatterplot_1.png")
