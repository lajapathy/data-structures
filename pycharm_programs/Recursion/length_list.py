# given a list, return its length.
def str_len(str1):
    if len(str1) == 0:
        return 0
    else:
        return 1 + str_len(str1[1:])

def list_len(list1):
    if len(list1)==0:
        return 0
    else:
        return 1 + list_len(list1[1:])

print str_len('lll')
print list_len([])