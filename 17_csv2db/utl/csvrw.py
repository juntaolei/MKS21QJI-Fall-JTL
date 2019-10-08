from csv import DictReader

# Creates a table if it does not exist
def create(tbl_name, headers, db):
  tbl_headers = " (" + ",".join("{0} BLOB".format(i) for i in headers) + ")"
  db.execute("CREATE TABLE IF NOT EXISTS " + tbl_name + tbl_headers)

# Add all entries from csv into a table
def insertAll(file, tbl_name, db):
  f = DictReader(open(file))
  create(tbl_name, f.fieldnames, db)
  for row in f:
    field = " VALUES("
    for value in row.values():
      if any(i.isdigit() for i in value):
        field += value + ","
      else: field += '"{0}"'.format(value) + ","
    db.execute("INSERT INTO " + tbl_name + field[:-1] + ")")

# print the value of a table
def printTable(tbl_name, cur):
  cur.execute("SELECT * FROM " + tbl_name)
  for row in cur.fetchall():
    print(dict(row))