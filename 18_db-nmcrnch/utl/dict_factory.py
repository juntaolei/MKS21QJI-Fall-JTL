def dict_factory(cur, row):
  return {header[0]: row[i] for i, header in enumerate(cur.description)}