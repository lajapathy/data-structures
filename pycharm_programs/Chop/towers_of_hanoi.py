
from stack import stack

def t_hanoi(stack1,stack2,stack3):
    stack2.push(stack1.pop())
    stack3.push(stack1.pop())


stack1=stack()
stack2=stack()
stack3=stack()

stack1.push(5)
stack1.push(4)
stack1.push(3)
stack1.push(2)
stack1.push(1)



