# length of the longest common substring of two given strings.

s1='AGGTAB'
s2='GXTXAYB'
op=''
def lcs(s1,s2,i,j):
    global op
    if (i==0)|(j==0):
        return 0
    if s1[i-1]==s2[j-1]:
        op+=s1[i-1]
        return 1+lcs(s1,s2,i-1,j-1)

    else:
        return max(lcs(s1,s2,i,j-1),lcs(s1,s2,i-1,j))

l = lcs(s1,s2,len(s1),len(s2))
print l
print op[:l][::-1]
