
# Print contents of file in reverse order

with open('reverse.txt','r') as f:
    for line in f.read().split('\n'):
        for c in reversed(line):
            print c,
        print ''
