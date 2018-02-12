
import os

def walkthrough(dir):
    for item in os.listdir(dir):
        if os.path.isfile(item):
            print str(dir)+'/'+str(item)
        else:
            walkthrough(dir+item)

walkthrough('/Users/lajapathymadhusudhanan/PycharmProjects/lunch-talk-jan25/')