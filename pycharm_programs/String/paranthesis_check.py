#Paranthesis checker

import os,sys
sys.path.insert(0,os.path.expanduser('~/PycharmProjects/dataStructures'))

from stack import Stack

def paranthesis_check(str1):
    braces_pairs = {'(':')','[':']','{':'}'}
    braces_stack = Stack()
    for c in str1:
        if c in ['(','[','{']:
            braces_stack.push(c)
            continue
        elif c in [')','}',']']:
            if braces_pairs[braces_stack.pop()] != c:
                return False
    return True

if paranthesis_check('{{([][])}()ss)}'):
    print 'valid'
else:
    print 'invalid'

