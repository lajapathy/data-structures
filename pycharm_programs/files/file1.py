

f = open('test1','r')

for line in f.readlines():
    print line

for line in f.readlines():
    print line

        ####### Only difference between r+ and w+ is that r+ will throw and error when the file is not present
####### Whereas w+ will create a new file