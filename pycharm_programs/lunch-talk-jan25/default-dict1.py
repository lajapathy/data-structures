
from collections import defaultdict

d = {1:2, 3:4}
print d[1]
#print d[5]

class my_dict(dict):

    def __missing__(self, key):
        return 'default'

e = my_dict()
e[1] = 2
e[3] = 4
e[4] = ['aaa']
print e
print e[5]
print e

#f = defaultdict(<datatype>) - When we try to access a non-existent key, the default datatype(empty) is assigned
# as a value to that key

def fun1():
    return 50

f = defaultdict(fun1)

f[1] = 2
f[3] = 4
print f[5]
print f

#### Reading a list of tuples and building a dictionary out of it


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
#d = {}
for k, v in s:
    d[k].append(v)

print d