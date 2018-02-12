import os

rootdir ='/Users/lajapathymadhusudhanan/documents/test_os'

# for subdir, dirs, files in os.walk(rootdir):
#     os.chdir(rootdir)
#     for file in files:
#             print file
#             f=open(file,'r')
#             lines=f.readlines()
#             f.close()
#             f=open(file,'w')
#             for line in lines:
#                 newline = "No you are not"
#                 f.write(newline)
#             f.close()


def iterate_directory(root_dir):
    for directory_name, sub_directory_names, files in os.walk(root_dir):
        print directory_name
        print sub_directory_names
        print files
        print '************'




iterate_directory('/Users/lajapathymadhusudhanan/PycharmProjects')
print os.path.join('/Users/lajapathymadhusudhanan/PycharmProjects','chop')























