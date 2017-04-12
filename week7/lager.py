import sys
outputFile = sys.stderr

def setOutFile(filename):
    global outputFile
    outputFile = open(filename, "a")

def warn(text):
    print(text, file=outputFile)
