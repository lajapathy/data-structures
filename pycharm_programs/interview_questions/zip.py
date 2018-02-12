x='abc'
y='abcde'
z='ab'
list1=[x,y,z]

# for i,val in enumerate(zip(x,y,z)):
#     print(i,val)
#
# for i,val in enumerate(zip(*list1)):
#     print(i,val)

def get_substring(s1, s2):
    i=0
    while(i<len(s1) and i<len(s2)):
        if s1[i] == s2[i]:
            i+=1
        else:
            break
    return s1[:i]

def lcs(strs):
    reduce(get_substring, strs)
#print(lcs("abc", "abcde"))


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    first_half_sum = 0
    second_half_sum = 0
    x = abs(x)
    if len(str(x)) % 2 == 0:
        if str(x)[int(len(str(x)) / 2) - 1] != str(x)[int(len(str(x)) / 2)]:
            return False
        for i in range(0, int(len(str(x)) / 2) - 1):
            first_half_sum += int(str(x)[i])
        for i in range(int(len(str(x)) / 2) + 1, len(str(x))):
            second_half_sum += int(str(x)[i])
        if first_half_sum == second_half_sum:
            return True
        return False
    else:
        for i in range(0, int(len(str(x)) / 2)):
            first_half_sum += int(str(x)[i])
        for i in range(int(len(str(x)) / 2) + 1, len(str(x))):
            second_half_sum += int(str(x)[i])
        if first_half_sum == second_half_sum:
            return True
        return False

print(isPalindrome(34544543))