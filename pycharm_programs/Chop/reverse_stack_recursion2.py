

def reverse_stack(s,t=[]):
    if len(s)==0:
        print 'inside if'
        return t
    print 'outside if'
    t.append(s.pop())
    return reverse_stack(s,t)


print reverse_stack([1,2,3,4,5])