class queue(object):
    def __init__(self):
        self.qlist = []

    def enqueue(self, val):
        self.qlist.insert(0, val)

    def dequeue(self):
        return self.qlist.pop()

    def return_top(self):
        return self.qlist[-1]


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = queue()
        self.q2 = queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        # enqueue new element to q2
        self.q2.enqueue(x)
        # dequeue from q1 and enqueue in q2

        while self.q1.qlist:
            self.q2.enqueue(self.q1.dequeue())
        # swap q1 and q2
        temp = self.q1.qlist
        self.q1.qlist = self.q2.qlist
        self.q2.qlist = temp

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q1.dequeue()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1.return_top()

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return (not self.q1.qlist) and (not self.q2.qlist)

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(7)
print obj.top()
obj2 = MyStack()
print obj2.empty()
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()