# TODO
import cs50
from sys import argv, exit
import csv

# Check command line argument
if len(argv) != 2:
    print("Error: No CSV file name entered")
    exit(1)

# Create empty database
open("students.db", "w").close()

# Open the database for SQLite
db = cs50.SQL("sqlite:///students.db")

# Create a table in the students database to store name
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")

# Open the CSV file to read data
with open(argv[1],"r") as students:

    # Create Dictreader
    reader = csv.DictReader(students)

    for row in reader:
       namelist = row['name'].split()

       if len(namelist) == 2:
           namelist.append(namelist[1])
           namelist[1] = None

       db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", namelist[0], namelist[1], namelist[2], row['house'], row['birth'])





