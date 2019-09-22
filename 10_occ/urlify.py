def urlify(dic, url):
  tmp = dic.copy()
  for key in tmp:
    tmp[key] = [tmp[key], url + key]
  return tmp