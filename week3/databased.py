import psycopg2
from sys import argv



def print_help():
    print("Usage: python3 databased.py what_to_do\nvalid options for what_to_do are: add, delete, update")

def add_record(cur):
    name = input("What name? ")
    dob = int(input("what dob? "))
    cur.execute("INSERT INTO student (name, dob) VALUES (%s, %s)", (name, dob))

def delete_record(cur):
    show_records(cur)
    id = int(input("what id? "))
    cur.execute("DELETE FROM student WHERE id=%s", (id,))
    


def update_record(cur):
    pass

def show_records(cur):
    cur.execute("SELECT * FROM student;")
    #get the next element (here it is the first time)
    for record in cur:
        print(record)

#    current = cur.fetchone()
#
#    while current != None:
#        print(current)
#        #get the next element
#        current = cur.fetchone()

    

conn = psycopg2.connect("dbname=sql_tour user=sam.boyarsky host=/tmp/")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS student (id serial PRIMARY KEY, name varchar, dob integer);")



if len(argv) > 1:
    if argv[1] == "add":
        add_record(cur) 
    elif argv[1] == "delete":
        delete_record(cur)
    elif argv[1] == "update":
        update_record(cur)
    elif argv[1] == "show":
        show_records(cur)
    else:
        print_help()
else:
    print_help()

conn.commit()
cur.close()
conn.close()
