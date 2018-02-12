
def find_sum(list1, target):
    tail=0
    sum=0
    for i in range(len(list1)):
        sum=sum+list1[i]
        while(sum>target):
            sum = sum - list1[tail]
            tail += 1
        if sum==target:
            return tail,i
    return -1

print(find_sum([3,8,5,6], 11))

