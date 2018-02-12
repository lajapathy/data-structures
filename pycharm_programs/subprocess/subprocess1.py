
import subprocess
import os

print os.getcwd()
x = subprocess.Popen(['ls'])
print x
for line in x.stdout:
    print line

