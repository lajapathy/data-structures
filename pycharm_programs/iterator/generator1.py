def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print line,

filenames = ['a1.txt','b1.txt']
pattern = 'd'
lines = readfiles(filenames)
print lines
lines = grep(pattern, lines)
print lines

printlines(lines)