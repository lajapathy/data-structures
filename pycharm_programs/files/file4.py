'''
Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths
of all the files in the tree
'''

import os

def findfiles(dirname):
    for currdir,sub_directories,files in os.walk(os.getcwd()):
        print currdir
        print os.path.join(os.getcwd(),dirname)
        if currdir == os.path.join(os.getcwd(),dirname):
            print "sss"
            for file in files:
                print os.path.join(os.getcwd(),currdir,file)

findfiles("test")
