import itertools
import pdb

def combination(list1, list2):
    pdb.set_trace()
    return [zip(x,list2) for x in itertools.permutations(list1,list2)]

print(combination([1,2], [3,4,5]))