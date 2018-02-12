files_list = ['ddd','fff']
for x in range(10000):
    f = open('foo.txt', 'w')
    #f.close()
    files.append(f)




import os


cwd = os.getcwd()
cwd.strip('bin')
gConfigFile = os.path.join(cwd,gConfigFile)