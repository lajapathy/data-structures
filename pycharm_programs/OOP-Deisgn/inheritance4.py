class First(object):
  def __init__(self):
    super(First, self).__init__()
    print("first")

class Second(object):
  def __init__(self):
    super(Second, self).__init__()
    print("second")

class Third(First, Second):
  def __init__(self):
    super(Third, self).__init__()
    print("that's it")


x=Third()
#print Third.__mro__

# DEPTH-First and Left-to-Right
# Third --> First --> object --> Second --> object
# After removing all duplicates, except for the last one, we get :
#
# Third --> First --> Second --> object
# So, lets follow what happens when we instantiate an instance of the Third class, e.g. x = Third().
#
# According to MRO __init__ of Third is called first.
# Next, according to the MRO, inside the __init__ method super(Third,
# self).__init__() resolves to the __init__ method of First, which gets called.
# Inside __init__ of First super(First, self).__init__() calls the __init__ of Second, because that is what the MRO dictates!
# Inside __init__ of Second super(Second, self).__init__() calls the __init__ of object, which amounts to nothing. After that "second" is printed.
# After super(First, self).__init__() completed, "first" is printed.
# After super(Third, self).__init__() completed, "that's it" is printed.
