class Stack(object):
    def __init__(self):
        self.stack_list = []

    def pop(self):
        self.stack_list.pop()

    def push(self, val):
        self.stack_list.append(val)


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """

        #move all elements from s2 to s1
        while self.stack2.stack_list:
            self.stack1.push(self.stack2.stack_list.pop())

        # push element to stack2
        self.stack2.push(x)

        #move all elements from s1 to s2
        while self.stack1.stack_list:
            self.stack2.push(self.stack1.stack_list.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        print self.stack2.stack_list
        if not self.stack2.stack_list:
            return None
        return self.stack2.stack_list.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        print self.stack2.stack_list
        if not self.stack2.stack_list:
            return None
        return self.stack2.stack_list[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1.stack_list == []

obj = MyQueue()
obj.push(1)
obj.push(2)
print obj.peek()
print obj.pop()
print obj.empty()
# print obj.stack1.stack_list
# print obj.peek()
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()