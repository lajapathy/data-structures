#Given a string, print all possible substrings

g_ss=[]

def sub_string(str1):
    global g_ss
    if str1 is None:
        return
    if len(str1)==1:
        return str1
    print str1
    print str1[1:]
    return my_append(str1[0],sub_string(str1[1:]))

def my_append(c,str1):
    global g_ss
    if str1 is None:
        return [c]
    str_list=[]
    for i in xrange(len(str1)):
        str_list.append(str1[:i]+'c'+str1[i:])
    g_ss.extend(str_list)

sub_string('mdhg')
print g_ss