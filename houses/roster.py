# TODO
from sys import argv, exit
import csv
import cs50

# Check command line argument
if len(argv) != 2:
    print("Error: Please enter the House Name")
    exit(1)

# Access the database
db = cs50.SQL("sqlite:///students.db")

# Execute query to extract data from the database
data = db.execute("SELECT * from students WHERE house = ? ORDER BY last, first",argv[1])

# print(data)
# the extracted data will be a list of dictionaries with each row being a dictionary consisting of key(column heading)-value pair
for row in data:
    if row['middle'] == None:
        print(row['first'], row['last']+", born", row['birth'])
    else:
        print(row['first'], row['middle'], row['last']+", born", row['birth'])