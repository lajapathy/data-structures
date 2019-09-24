class A:
    x=5
class B:
    x=7
class C(A,B):
    @classmethod
    def test(cls):
        print cls.x

    @staticmethod
    def test2():
        print C.x

print C.x
C.test()
C.test2()
obj = C()
print dir(obj)
print obj.x