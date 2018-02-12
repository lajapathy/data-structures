
import collections

#Counter class
c1 = collections.Counter({'a':3,'b':2,'c':4})
c2 = collections.Counter(['a','b','e','a','e'])
c3 = collections.Counter(c=1,d=2,e=3)

print c1
print c2
print c3

c4 = collections.Counter('abcdaab')

for letter in 'abcde':
    print '%s : %d' % (letter, c4[letter])

