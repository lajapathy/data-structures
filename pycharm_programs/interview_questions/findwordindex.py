
s1 = 'dogcatdogcardogcatmax'
list1 = ['dog','max','cat','car']

def findIndex(s1, list1):
    dict1={}
    for word in list1:
        list2 = s1.split(word)
        for i