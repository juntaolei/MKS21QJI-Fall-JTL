# Jun Tao Lei & Kenneth Chin (Regular Chairs)
# SoftDev1 pd9
# K#17 - No Trouble
# 2019-10-07

from sqlite3 import connect
from utl.csvrw import insertAll, printTable

# Setup the database
DB_FILE = "discobandit.db"

db = connect(DB_FILE)
c = db.cursor()

# Add the csv and create a table to store the csv if it does not exist
insertAll("data/courses.csv", "courses", db)
insertAll("data/students.csv", "students", db)

q = """
  SELECT name, students.id, mark
  FROM students, courses
  WHERE students.id = courses.id;
"""

foo = db.execute(q)

print(isinstance(foo.fetchall(), dict))

for row in foo.fetchall():
  print(dict(row))

# Print the database
print("courses table")
printTable("courses", db)
print("\nstudents table")
printTable("students", db)

# Save and exit the database
db.commit()
db.close()