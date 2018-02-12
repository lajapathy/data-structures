from underscore2 import *

a=A()
a.method1()
#b=_B()
#b.method2()
a._method3()
a._A__method4()

class C:
    def _single_method(self):
        print("single")
    def __double_method(self): # for mangling
        print("C")
class D(C):
    def __double_method(self): # for mangling
        print("D")

d=D()
d._C__double_method()