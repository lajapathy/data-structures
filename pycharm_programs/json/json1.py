import json

d = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
print d
e = json.dumps(d)
print e

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATA:', repr(data)

unsorted = json.dumps(data)
print 'JSON:', json.dumps(data)
print 'SORT:', json.dumps(data, sort_keys=True)