
import subprocess
from subprocess import Popen, PIPE

x = subprocess.Popen('ls')
print x
#x.wait()
#print 'done'

proc2 = subprocess.check_output('ls')
print x.returncode

proc3 = subprocess.check_output('exit 0',shell=True)



p = Popen(['program', 'arg1'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"input data that is passed to subprocess' stdin")
rc = p.returncode