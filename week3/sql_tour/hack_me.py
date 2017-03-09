import psycopg2
from sys import argv

def print_help():
    print("Usage: python3 hack_me.py what_to_do\nvalid options for what_to_do are: add, delete, update")

if len(argv) > 1:
    if argv[1] == "add":
        print("#do add stuff")
    elif argv[1] == "delete":
        print("#do delete stuff")
    elif argv[1] == "update":
        print("#do update stuff")
    else:
        print_help()
else:
    print_help()


# Connect to an existing database
conn = psycopg2.connect("dbname=sql_tour user=sam.boyarsky host=/tmp/")

# Open a cursor to perform database operations
cur = conn.cursor()

#sql = "INSERT INTO test (num, data) VALUES ({}, '{}')".format(int(input("enter a number")), input("enter some data") )
#print(sql)
#cur.execute(sql)

cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (int(input("enter a number")), input("enter some data") ) )

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()
