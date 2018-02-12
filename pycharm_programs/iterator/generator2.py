# Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.

a1 = open('a1.txt')
b1 = open('b1.txt')
files_list = [a1,b1]

def get_lines_from_files_normal(files):
    return [line for line in [file.readlines() for file in files]]

def get_lines_from_files(files):
    for file in files_list:
        for line in file:
            yield line

#for line in get_lines_from_files(files_list):
#    print line

for line in get_lines_from_files_normal(files_list):
    print line


