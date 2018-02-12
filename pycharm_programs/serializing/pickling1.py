import pickle

a = [1,5,10]
fp1 = open('pickle1','w')
pickle.dump(a,fp1)
fp1.close()
fp1 = open('pickle1','r')
b = pickle.load(fp1)
print b