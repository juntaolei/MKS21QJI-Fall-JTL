# Jun Tao Lei
# SoftDev1 pd9
# K#06 -- Occupation Weighted Randomizer / Dictionary / Pick an occupation based on a pre-existing probability.
# 2019-09-14

import csv
import random

def randoccupation(file):
    d = {}
    for row in csv.DictReader(open(file)):
        if (row["Job Class"] != "Total"):
            d[row["Job Class"]] = float(row["Percentage"])
    keys, values = zip(*d.items())
    return random.choices(keys, values)[0]

print(randoccupation("occupations.csv"))
