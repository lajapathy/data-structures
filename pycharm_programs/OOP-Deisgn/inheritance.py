class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

##################Read file inheritance4.py before doing this !!!!!!!!!!!

#Solution for d.go()
#Depth first, left to right traversal
#MRO for this example, for an instance of class D : D, B, A, object, C, A, object
#Duplicate removal : D, B, C, A, object

#a.go()
#b.go()
#c.go()
d.go()
#e.go()

#a.stop()
#b.stop()
#c.stop()
#d.stop()
#e.stop()

#a.pause()
#b.pause()
#c.pause()
#d.pause()
#e.pause()