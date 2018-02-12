

class A(object):
    def _fun1(self):
        print 'A'

class B(object):
    def _fun1(self):
        print 'B'

class C(B,A):
    pass

c=C()
print dir(c)
c._fun1()