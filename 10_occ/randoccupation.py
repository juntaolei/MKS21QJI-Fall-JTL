from csv import DictReader as dr
from random import choices as rc
from collections import OrderedDict

def getoccupations(file):
  dic = {}
  for row in dr(open(file)):
    dic[row["Job Class"]] = float(row["Percentage"])
  return dic

def randoccupation(dic):
  tmp = OrderedDict(dic.copy())
  tmp.pop("Total")
  keys = list(tmp.keys())
  values = [value[0] for value in tmp.values()]
  return rc(keys, values)[0]