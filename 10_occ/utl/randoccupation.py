# Jun Tao Lei (Of TeamKubica With Calvin Chu)
# SoftDev1 pd9
# K#10 -- Template Displaying Random Occupations / Dictionary + Flask + Jinja2 / Display a table of occupations and a random occupation.
# 2019-09-20

from csv import DictReader as dr
from random import choices as rc

# Read the csv file and added occupations to a dictionary row by row.
def getoccupations(file):
  dic = {}
  for row in dr(open(file)):
    dic[row["Job Class"]] = [float(row["Percentage"])]
  return dic

# Gets the percentages from the dictionary and use choices() to pick an occupation.
def randoccupation(dic):
  tmp = dic.copy()
  tmp.pop("Total") # Remove Total and 99.8 from the temporary dictionary.
  keys = list(tmp.keys())
  values = [value[0] for value in tmp.values()]
  # Associates occupations to corresponding percentages.
  return rc(keys, values)[0] # Return an occupation based on the percentages.