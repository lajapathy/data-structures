#Find if there is a duplicate character in a given string

def findDup(str1):
    if str1=='':
        return 'Empty string'
    for i in xrange(len(sorted(str1))-1):
        if sorted(str1)[i]==sorted(str1)[i+1]:
            return False
    return True


print findDup('mmmbbb')