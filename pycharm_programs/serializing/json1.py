import json

d = u'{"a":1,"b":2}'
obj = json.loads(d)
print repr(obj)

e = {1:2,3:4}
print json.dumps(e)