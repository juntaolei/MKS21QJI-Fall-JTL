# Jun Tao Lei (Of TeamKubica With Calvin Chu)
# SoftDev1 pd9
# K#10 -- Template Displaying Random Occupations / Dictionary + Flask + Jinja2 / Display a table of occupations and a random occupation.
# 2019-09-20

# Append an url to the values associated with each key.
def urlify(dic, url):
  for key in dic:
    key = dic[key].append(url + key)
  return dic