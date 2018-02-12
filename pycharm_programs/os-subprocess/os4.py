#Prints all files in given path
import os

for currpath,dir_list,file_list in os.walk(os.getcwd()):
    print currpath
    print dir_list
    print file_list
    print '*******************'
