# os.walk(some path)
# Generates the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory
# in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
###### Note the words "generate" and "yield". THIS METHOD DOES NOT RETURN ANYTHING

# dirpath is a STRING, the path to the directory. dirnames is a LIST of the names of the subdirectories in dirpath
# (excluding '.' and '..'). filenames is a LIST of the names of the non-directory files in dirpath.


# dirpath is ABSOLUTE, whereas dirnames and filenames are  RELATIVE
import os

def insert_username_into_filename(filename):
    print os.path.expanduser('.')
    print os.walk(os.path.expanduser('~/PycharmProjects/'))
    for root,dirs,files in os.walk(os.path.expanduser('~/PycharmProjects/')):
        for file in files:
            print os.path.join(root,file)
        os.path.expanduser()


insert_username_into_filename('stats_tree.py')