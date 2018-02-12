
def innermost_parens(str1):
    start = 0
    end = 0
    for i in xrange(len(str1)):
        if str1[i] == '(':
            start = i
        elif str1[i] == ')':
            end = i
            break

    if end == 0 :
        print 'unbalanced paranthesis'
        return

    print str1[start:end+1]

innermost_parens("1 + (2 * (4 * (2 + (8 * 7)) - 1))")