

def foo(a,b,c,*args):
    print "a=%s" % (a,)
    print "b=%s" % (b,)
    print "c=%s" % (c,)
    print "args=%s" % (args,)

#argdict = dict(a="testa", b="testb", c="testc", excessarg="string")
#print argdict
#foo(**argdict)

#### NOTE : ** unpacks dictionary and * unpacks tuple

def foo1(*args):
    print "args=%s" % (args,)
    print type(args)
    for tuple in args:
        print tuple

foo1([3,5],[4,6])
t=tuple()
l=list()



