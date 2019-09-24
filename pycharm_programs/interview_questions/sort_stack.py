
class Stack:
    def __init__(self):
        self.stacklist = []
    def push(self, val):
        self.stacklist.append(val)
    def peek(self):
        return self.stacklist[-1]
    def pop(self):
        temp = self.stacklist[-1]
        del self.stacklist[-1]
        return temp
    def print_stack(self):
        for i in xrange(len(self.stacklist)-1,-1,-1):
            print self.stacklist[i]
    def is_empty(self):
        return self.stacklist == []


s = Stack()
s.push(4)
s.push(1)
s.push(7)
s.push(5)
s.push(3)

s2 = Stack()

while(not s.is_empty()):
    temp = s.pop()
    if s2.is_empty():
        s2.push(temp)
        continue
    while (s2.peek() > temp):
        s.push(s2.pop())
    s2.push(temp)






