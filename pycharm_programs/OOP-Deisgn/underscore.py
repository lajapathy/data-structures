

class A(object):
    def __method1(self):
        print 'Inside method1 of A'
        pass

    def __lajju__(self):
        print 'A'
        pass

    def _jack(self):
        print 'A jack'
        pass

class B(A):
    def dummy(self):
        pass

    def __method1(self):
        print 'Inside method1 of b'
        pass

    def _jack(self):
        print 'B jack'
        pass


    def __lajju__(self):
        print 'C'
        self.__method1()
        pass


print dir(B)
B().__lajju__()
B()._jack()
A()._jack()

# _something() - private - Will be inherited (but not INTENDED to) - Will not be overridden
# __something() -  Will be inherited, but classname will be prepended (HENCE making it PRIVATE)- so Overriding not possible.
# __something__() - Do not use this. If used, this will act like normal methods

class AA:
    def __init__(self):
        self.__var1 = 123
    def printVar1(self):
        print self.__var1

x = AA()
#print x.__var1 # This will throw error