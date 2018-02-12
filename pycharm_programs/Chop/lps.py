import pdb

def lps(str1, i, j):
    if i==j:
        return 1
    if str1[i]==str1[j] and j==i+1:
        return 2
    if str1[i]==str1[j]:
        return lps(str1,i+1,j-1) + 2
    return max(lps(str1,i,j-1), lps(str1,i+1,j))

#print(lps("cababbbbj", 0, len("cababbbbj")-1))

def lps_dp(str1):
    n=len(str1)
    result = [[0 for x in range(n)] for x in range(n)]
    #pdb.set_trace()
    for substring_length in range(2, n+1):
        for last_char in range(n-substring_length+1):
            first_char = substring_length+last_char-1

print(lps_dp("cababbbbj"))


