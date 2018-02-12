
#LCS using DP

s1='bbgde'
s2='fhbbgdrgde'
mat=[[0 for j in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]

def lcs_dp(s1,s2):

    lcs=0
    for i in xrange(len(s1)):
        for j in xrange(len(s2)):
            if s1[i]==s2[j]:
                mat[i][j]=mat[i-1][j-1]+1
                lcs=mat[i][j]
            else:
                mat[i][j]=max(mat[i][j-1],mat[i-1][j])
    return lcs

print lcs_dp(s1,s2)