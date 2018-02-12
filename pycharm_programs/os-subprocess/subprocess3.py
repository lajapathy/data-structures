
import subprocess



cmd='printe \'lajju\''
fp1 = open('tmp','w+')
fp1.write(cmd)
p = subprocess.Popen('python',stdout=subprocess.PIPE,stdin = subprocess.PIPE,stderr = subprocess.PIPE)
p_out,p_err = p.communicate(cmd)
print p_out
print '---'
print p_err