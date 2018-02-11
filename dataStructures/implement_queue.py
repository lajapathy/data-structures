#Implement a queue ↴ with 2 stacks ↴ .
# Your queue should have an enqueue and a dequeue function and it should be "first in first out" (FIFO).

class Stack(object):
    def __init__(self):
        self.items=[]
        self.min = None

    def push(self,new_item):
        if not self.min:
            self.min=new_item
        else:
            self.min=min(self.min,new_item)
        self.items.append(new_item)

    def pop(self):
        return self.items.pop()


class Queue(object):

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,element):
        while(self.stack2.items != []):
            self.stack1.push(self.stack2.pop())
        self.stack1.push(element)

    def dequeue(self):
        while(self.stack1.items != []):
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    