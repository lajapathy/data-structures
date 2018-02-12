class First(object):
    def __init__(self):
        print "first"

class Second(First):
    def __init__(self):
        super(Second,self).__init__()
        print "second"

class Third(First):
    def __init__(self):
        print "third"

class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print "that's it"

#print Fourth.__mro__
# MRO for Fourth : Fourth -> Second -> First -> object -> Third -> First -> object
#Remove duplicates : Fourth -> Second -> Third -> First -> object (First occurences of duplicates are removed)
Fourth()
