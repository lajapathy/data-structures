import time
import subprocess

cmd = 'python'
python_proc = subprocess.Popen(cmd, stdin = subprocess.PIPE, stderr = subprocess.PIPE, stdout = subprocess.PIPE)
out, err = python_proc.communicate(input = 'print \'lajju\'')

print type(out)
print out

print type(err)
print err

print 'Part2 . Sleeping for 2 seconds'
time.sleep(2)


cmd2 = 'python'
commands_file = open('python-cmds.txt','r')
python_proc2 = subprocess.Popen(cmd2,stdin = commands_file, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
out,err = python_proc2.communicate(python_proc2.stdin)
print out

commands_file.seek(0)

python_proc2_outFile = open('python_proc2_output.txt','w')
python_proc2 = subprocess.Popen(cmd2,stdin = commands_file, stdout = python_proc2_outFile, stderr = python_proc2_outFile)
out,err = python_proc2.communicate(python_proc2.stdin)