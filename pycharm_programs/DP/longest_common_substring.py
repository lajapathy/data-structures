

def lcs_count_recursive(s1, s2):
    m=len(s1)
    n=len(s2)
    if m==0 or n==0:
        return 0
    if m==1 and s1 in s2:
        return 1
    if n==1 and s2 in s1:
        return 1
    if s1[m-1]==s2[n-1]:
        return 1+lcs_recursive(s1[:m-1], s2[:n-1])
    return max(
        lcs_recursive(s1, s2[:n-1]),
        lcs_recursive(s1[:m-1], s2))

def lcs_recursive(s1, s2):
    m=len(s1)
    n=len(s2)
    if m==0 or n==0:
        return ''
    if m==1 and s1 in s2:
        return s1
    if n==1 and s2 in s1:
        return s2
    if s1[m-1]==s2[n-1]:
        return s1[m-1]+lcs_recursive(s1[:m-1], s2[:n-1])
    return max(
        lcs_recursive(s1, s2[:n-1]),
        lcs_recursive(s1[:m-1], s2))

def lcs_dp(s1, s2):
    m=len(s1)
    n=len(s2)
    result = [[0 for x in range(m)] for x in range(n)]
    for i in range(m-1):
        for j in range(n-1):
            if i==0 and j==0:
                if s1[i]==s2[j]:
                    result[i][j]=1
            elif i==0 or j==0:
                result[i][j] = 0
            elif s1[i]==s2[j]:
                result[i][j] = 1 + result[i-1][j-1]
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1])
    return result


print(lcs_recursive("abcdefg", "adfk")[::-1])
print(lcs_count_recursive("abcdgh", "edfhr"))
print(lcs_dp("abcdgh", "edfhr"))