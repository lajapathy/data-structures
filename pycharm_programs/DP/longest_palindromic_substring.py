def lps_recur(str1):
    n=len(str1)
    if len(str1)<=2:
        return str1
    if str1==str1[::-1]:
        return str1
    return max_len(
        lps_recur(str1[:n-1]),
        lps_recur(str1[1:n])
    )

def max_len(str1, str2):
    if len(str1)>=len(str2):
        return str1
    return str2

def lps_dp(str1):
    n=len(str1)
    result_substring = ''
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            if j==i:
                result[i][j]=1
            elif j==i+1:
                result[i][j]=2
            elif str1[i:j+1]==str1[i:j+1][::-1]:
                result[i][j]=result[i][j-1]+1
            else:
                result[i][j] = result[i][j - 1]
    return result

print(lps_recur("dcdabade"))
print(lps_dp("dcdabade"))
