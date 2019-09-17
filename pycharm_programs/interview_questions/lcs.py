
# def lcs(s1, s2, res=''):
#     if not s1 or not s2:
#         return ''
#     if s1[-1]==s2[-1]:
#         #import pdb;pdb.set_trace()
#         return lcs(s1[:-1], s2[:-1], res) + res + s1[-1]
#     res1 = lcs(s1[:-1], s2, res)
#     res2 = lcs(s1, s2[:-1], res)
#     if not res1 and res2:
#         return res2
#     if not res2 and res1:
#         return res1
#     if len(res1) > len(res2):
#         return res1
#     if len(res1) < len(res2):
#         return res2











def lcs(s1, s2):
    if not s1 or not s2:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + lcs(s1[:-1], s2[:-1])
    return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))


def lcs_iterative(s1, s2):
    result = 0
    lcs_array = [[0 for i in xrange(len(s2)+1)] for j in xrange(len(s1)+1)]

    for i in xrange(len(s1)+1):
        for j in xrange(len(s2) + 1):
            if i==0 or j==0:
                lcs_array[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                lcs_array[i][j] = 1+ lcs_array[i-1][j-1]
                result = max(result, lcs_array[i][j])
            else:
                lcs_array[i][j] = 0
    return result


def LCSubStr(X, Y, m, n):
    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first
    # row and first column entries have no
    # logical meaning, they are used only
    # for simplicity of the program.

    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]

    # To store the length of
    # longest common substring
    result = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result













print lcs('abcdxyz', 'xyzabcd')
print lcs_iterative('aafdfghi', 'bfadgic')
print LCSubStr('abcdxyz', 'xyzabcd', 7, 7)
