import csv

titles = {}

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        rows = row["problem"].strip().upper()
        if rows in titles:
            titles[rows] += 1
        else:
            titles[rows] = 1

for rows in sorted(titles, key=lambda title: titles[title], reverse=True):
    print(rows, titles[rows])
