from sqlite3 import connect
from utl.csvrw import create, insert, printTable
from utl.dict_factory import dict_factory

# Calculate the average
def average(cur):
  sums = {} # Get sum
  times = {} # Get num of appearances
  for row in cur:
    times[str(row["id"])] = times.get(str(row["id"]), 0) + 1 # Increment the value of that id by 1
    sums[str(row["id"])] = sums.get(str(row["id"]), 0) + row["mark"] # Add the mark to the value of that id
  return {i: sums[i] / times[i] for i in sums} # Return the average

DB_FILE = "discobandit.db"

db = connect(DB_FILE)
db.row_factory = dict_factory
c = db.cursor()

# Query for the students and their marks
query = """
  SELECT name, students.id, mark
  FROM students, courses
  WHERE students.id = courses.id;
"""

# Display student name, id, and mark
for row in db.execute(query):
  print(row)

# Create a table of id and average named stu_avg
create("stu_avg", ["id", "average"], db)

# Get a dictionary of averages corresponding to id keys
avgs = average(db.execute(query))

# Add each average and its corresponding id into table
for stu in avgs:
  insert([stu, avgs[stu]], "stu_avg", db)

# Print the stu_avg table
print("\nstu_avg table")
printTable("stu_avg", db)

# Save and exit the database
db.commit()
db.close()