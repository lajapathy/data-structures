
#Write a function rev_string(my_str) that uses a stack to reverse the characters in a string.

import sys,os
sys.path.append(os.path.expanduser('~/PycharmProjects/dataStructures'))




from stack import Stack

def rev_string(str1):
    s = Stack()
    for c in str1:
        s.push(c)
    str1 = ''
    while s.peek():
        str1 += s.pop()
    return str1

print rev_string('lajju')