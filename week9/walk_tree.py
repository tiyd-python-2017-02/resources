from sys import argv
import os.path
import os

def find_file(start, filename):
    # if you find a file called filename, print it out (then see if you
    # can print its path)
    while start.endswith(os.sep):
        start = start[:-len(os.sep)]
    for f in os.listdir(start):
        if f == filename:
            print(start + os.sep + f)
        if os.path.isdir(start + os.sep + f):
            find_file(start + os.sep + f, filename)
        
find_file(argv[1], argv[2])


