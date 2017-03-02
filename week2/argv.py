from sys import argv

#argv is a list of command line arguments for this execution of the program.
#The 0th element will always be the name of the script.
print(argv)
print(type(argv))
if len(argv) > 1:
    for arg in argv:
        print(arg)

