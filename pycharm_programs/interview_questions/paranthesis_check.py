# code

class Stack:
    def __init__(self):
        self.stacklist = []

    def push(self, data):
        self.stacklist.append(data)

    def pop(self):
        return self.stacklist.pop()


paranthesisDict = {
    '{': '}',
    '(': ')',
    '[': ']'
}

s = Stack()


def checkParanthesis(str1):
    if not str1:
        return 'empty'
    for char in str1:
        if char in paranthesisDict:
            s.push(char)
            continue
        if char in paranthesisDict.values():
            try:
                if paranthesisDict[s.pop()] != char:
                    return 'unbalanced'
            except IndexError,e:
                return 'unbalanced'
        else:
            return 'unsupported'
    return 'balanced'

s = Stack()
print checkParanthesis('{([])}')
s = Stack()
print checkParanthesis('{([')
#crash scenarios
s = Stack()
print checkParanthesis('])}')
s = Stack()
print checkParanthesis('{}]')
s = Stack()
print checkParanthesis('')