def div1(x, y):
    print "%s/%s = %s" % (x, y, x / y)


def div2(x, y):
    print "%s//%s = %s" % (x, y, x // y)


div1(5, 2)
div1(5., 2)
div2(5, 2)
div2(5., 2.)
div2(5., 2)

#By default, Python 2 automatically performs integer arithmetic if both operands are integers.
# As a result, 5/2 yields 2, while 5./2 yields 2.5.
# double slash operator ALWAYS perform INTEGER division