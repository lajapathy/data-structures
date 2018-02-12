import os
#Write function to print all prime numbers unitl a :limit". BE AS EFFICIENT AS POSSIBLE

def is_prime(n):
    if n==2 or n==1:
        return True
    for i in xrange(2,n):
        if n%i == 0:
            return False

    return True

def primes(limit):
    i=1
    while i<limit:
        if is_prime(i) : yield i
        i+=1

for n in primes(50):
   print n,


str1 = ''.join([`i` for i in xrange(10)])
print str1

print os.path.dirname(os.path.expanduser('~'))
print os.path.basename(os.path.expanduser('~'))
print os.path.split('/ws/lama/scr/p.py')
print os.path.split('/home/k/TEST/PYTHON/p.py')
print os.path.join('/home/k/TEST/PYTHON/','p.py')